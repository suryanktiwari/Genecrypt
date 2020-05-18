import time
# from fitness import fit_bi_check
import random
import operator
from ngram_score import ngram_score


class Vignere:

    def __init__(self, KS, C):
        self.keyspace = KS
        self.cipher = C

    def add_pop(self, orderings):
        for key in orderings:
            # count, res = fit_bi_check(key)
            deciphered = self.convert(key)
            score = round(fitness.score(deciphered), 2)
            self.keyspace.append((key, score, deciphered))

    def print_pop(self):
        for x in self.keyspace:
            print(x)

    def get_last(self):
        return self.keyspace[len(self.keyspace)-1]

    def sorter(self):
        self.keyspace.sort(key=operator.itemgetter(1))

    def selectBest(self):
        self.keyspace = self.keyspace[-top_select:]
        # self.keyspace = self.keyspace[:top_select]


    def initialize(self, total):
        orderings = set()
        while total > 0:
            size = random.randrange(1, 20)
            order = [0] * size
            for i in range(0, size):
                order[i] = chr(random.randrange(0, 26)+65)
            orderings.add(tuple(order))
            total = total - 1
        print("initialized")
        return orderings

    def hill_climb(self):
        for tup in self.keyspace:
            i = random.randrange(0, 26)
            j = random.randrange(0, 26)
            tmp = list(tup[0])
            tmp[i], tmp[j] = tmp[j], tmp[i]
            deciphered = self.convert(tmp)
            score = round(fitness.score(deciphered), 2)
            if score > tup[1]:
                self.keyspace.append((tuple(tmp), score, deciphered))
                # print(" climbed ", end="")
                self.keyspace.remove(tup)
            # else:
            #     print(" didn't climb ", end="")

    def newChild(self):
        rankey = random.randint(0, top_select - 1)
        parent1 = self.keyspace[rankey][0]
        child = list(parent1)
        a = random.randrange(0, len(child))
        b = random.randrange(0, 26)
        child[a] = chr(b+65)
        return (child, rankey)

    def genetic(self):
        global generations
        cur_gen = 0
        while generations > cur_gen:
            if cur_gen % r_offspring_lim == r_offspring_lim - 1:  # random offspring generation
                # print("random offspring generation")
                self.add_pop(self.initialize(pop_limit - top_select))
            else:
                orderings = set()
                for i in range(0, pop_limit - top_select):
                    child, child_pos = self.newChild()
                    deciphered = self.convert(child)
                    score = round(fitness.score(deciphered), 2)
                    if score > self.keyspace[child_pos][1]:
                        self.keyspace[child_pos] = (tuple(child), score, deciphered)
                    orderings.add(tuple(child))
                self.add_pop(orderings)
            print("generation= ", cur_gen)
#             self.hill_climb()
            self.sorter()
            self.selectBest()
            self.print_pop()
            cur_gen = cur_gen + 1
            # generations = generations + 1
            print("//////////////////////////////////////////////////////////////////////////////////////////////")

    def convert(self, key):
        str = ""
        vig_key = self.generate_vignere_key(len(self.cipher), key)
        for w in range(0, len(self.cipher)):
            c = (ord(self.cipher[w]) - ord(vig_key[w]) + 26) % 26
            c += ord('A')
            str += chr(c)
        return str


    def generate_vignere_key(self, text_len, start_key):
        key_length = len(start_key)
        key = ''.join(start_key)
        if len(start_key) != text_len:
            remaining_chars = text_len - len(start_key)
            for i in range(remaining_chars):
                key_index = i% key_length
                key+= start_key[key_index]
            return key
        else:
            return key


pop_limit = 100
generations = 250
top_select = 70
# mut_prob = 0.2
r_offspring_lim = 10
# biasing_value = 2
fitness = ngram_score("english_quadgrams.txt")