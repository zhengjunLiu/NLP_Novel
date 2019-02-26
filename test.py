# # import numpy as np
# # def all_np(arr):
# #     arr = np.array(arr)
# #     key = np.unique(arr)
# #     result = {}
# #     for k in key:
# #         mask = (arr == k)
# #         print(mask)
# #         arr_new = arr[mask]
# #         print(arr_new)
# #         v = arr_new.size
# #         print(v)
# #         result[k] = v
# #     return result
# # print(all_np([1,2,3,4,5,6,4,5,6,3]))
# # s=[1,2,3,4,5,6,4,5,6,3]
# # s=np.array(s)
# # print(s[s==3])
#
# z=[[['/n/d/v', 80], ['/d/v/v', 78], ['/n/v/v', 66], ['/v/d/v', 62], ['/v/r/v', 62], ['/v/u/n', 60], ['/v/v/v', 58], ['/d/v/u', 57], ['/v/v/r', 57], ['/v/v/u', 57]],
#    [['/d/v/v', 93], ['/n/d/v', 93], ['/v/v/n', 71], ['/n/u/n', 70], ['/v/u/n', 70], ['/v/m/q', 65], ['/n/v/v', 64],['/d/d/v', 61], ['/m/q/n', 61], ['/v/v/v', 58]],
#    [['/v/u/n', 41], ['/d/v/v', 38], ['/n/d/v', 27], ['/v/v/u', 27], ['/n/v/u', 24], ['/n/u/n', 23], ['/d/v/u', 21],['/v/v/v', 21], ['/u/n/v', 20], ['/v/n/u', 20]]]
# h=z[0]
# for i in range(z[0].__len__()):
#     B = False
#     for j in range(h.__len__()):
#         if z[1][i][0]==h[j][0]:
#             h[j][1]=h[j][1]+z[1][i][1]
#             B=True
#     if B==False:
#         h.append((z[1][i][0],z[1][i][1]))
#
# print(h)


import sys
import os

from stanfordcorenlp import StanfordCoreNLP
from   nltk.tree import Tree
if __name__ == '__main__':
    with StanfordCoreNLP(r'D:\myprojects\stanford_nlp',lang='zh') as nlp:
        sentence = '清华大学位于北京。'
        # print( 'Tokenize:', nlp.word_tokenize(sentence))
        # print ('Part of Speech:', nlp.pos_tag(sentence))
        # print ('Named Entities:', nlp.ner(sentence))
        t=nlp.parse(sentence)
        print('Named Entities:', t)

        tree=Tree.fromstring(t)
        tree.draw()
        # print ('Dependency Parsing:', nlp.dependency_parse(sentence))

