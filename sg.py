# coding: utf-8
import random
import nltk
from collections import defaultdict
import pickle
import os

class SentenceGenerator:

     def __init__(self, level=3, datafile="data.pkl"):
          if os.path.isfile(datafile):
               with open(datafile, "rb") as f:
                    self.data = pickle.load(f)
          else:
               self.data = self.build_data(level, datafile)

     def build_data(self, level=3, outfile="data.pkl"):
          out1, out2, out3 = {}, {}, {}
          entries = nltk.corpus.cmudict.entries()
          for (word, syllable) in entries:
               a = ''.join(syllable[-level:])
               pos = nltk.pos_tag([word])[0][1]
               if a not in out1:
                    out1[a] = defaultdict(list)
               out1[a][pos].append(word)
               out2[word] = a
               out3[word] = pos
          with open(outfile, "wb") as f:
               pickle.dump((out1, out2, out3), f)

          return out1, out2, out3
     
     def rhyme(self, inp):
          t1, t2, t3 = self.data
          return t1[t2[inp]][t3[inp]]

     def rhyming(self, target, size=1):
          out = []
          for i in range(size):
               tmp = []
               for word in target.split():
                    tmp.append(random.choice(self.rhyme(word)))
               out.append(' '.join(tmp))
          return out
     
     
if __name__ == "__main__":
     import sys
     level = int(sys.argv[2])
     sg = SentenceGenerator(level)
     for x in sg.rhyming(sys.argv[1], int(sys.argv[3])):
          print(x)
