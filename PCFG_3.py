from stanfordcorenlp import StanfordCoreNLP
from   nltk.tree import Tree
import re
import os
import numpy as np
import xlwt
import csv


def Pcfg(k):
    t = ""
    L = []
    for i in k:
        if " " not in i:
            if "/n" not in i:
                if i == "(":
                    if t == "":

                        L.append(i)
                    else:

                        L.append(t)
                        t = ""

                        L.append(i)
                    continue
                elif (i >= u'\u0041' and i <= u'\u005a') or (i >= u'\u0061' and i <= u'\u007a'):  # p判断是否是英文字母
                    t = t + i
                    continue
                elif '\u4e00' <= i <= '\u9fff':  # 判断中文
                    t = t + i
                    continue

                elif i == ")":
                    if t == "":

                        L.append(i)
                    else:

                        L.append(t)
                        t = ""

                        L.append(i)
                    continue
                elif i == "\r" or i == "\n":
                    continue
                else:
                    t = t + i
                    continue
                    #     print(L)
    return L


def process(P_list):
    a = []  # 括号栈
    b = []  # 短语栈
    word = ""  # 从短语栈中曲出的短语结构存放
    rule = []  # 存储规则
    W_rule = []  # 存储未满规则
    W_ruleI = []  # 规则节点前1位，
    W_ruleII = []  # 规则节点前2位，
    z = ""  # 临时规则存放
    for char in P_list:
        if char == "(":
            a.append(char)
            if z != '':
                W_rule.append(z)
                if b.__len__() > 1:
                    W_ruleI.append(b[-2])
                else:
                    W_ruleI.append("0")
                if b.__len__() < 3:
                    W_ruleII.append("0")
                else:
                    W_ruleII.append(b[-3])
                z = ""

            continue

        elif char == ")":
            word = b.pop()
            if len(a) > 0:
                a.pop()

            if ('\u4e00' <= word[-1] <= '\u9fff'):  # 判断中文
                rule.append(word)
                lenth = len(b[-1])
                if len(b) < 3:
                    b.insert(0, "0")
                if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                    #                     print(W_rule[-1][0:lenth])#核实是否有规则未满
                    if b[-1] == W_rule[-1][0:lenth] and b[-2] == W_ruleI[-1] and b[-3] == W_ruleII[
                        -1]:  # 判断其父节点是否和未满规则一致
                        ru = W_rule.pop()
                        W_ruleI.pop()
                        W_ruleII.pop()
                        z = ru + " " + ''.join(re.findall(r'[A-Za-z]', word))
                    else:
                        z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
                else:
                    z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
            elif (word[-1] >= u'\u0041' and word[-1] <= u'\u005a') or (word[-1] >= u'\u0061' and word[-1] <= u'\u007a'):
                rule.append(z)
                z = ""
                if len(b) < 1:
                    lenth = 0
                else:
                    lenth = len(b[-1])
                if b.__len__() < 1:
                    z = "0"

                else:
                    if len(b) < 2:
                        b.insert(0, "0")
                    if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                        #                         print(W_rule[-1][0:lenth])  # 核实是否有规则未满
                        if b[-1] == W_rule[-1][0:lenth] and b[-2] == W_ruleI[-1]:  # 判断其父节点是否和未满规则一致
                            ru = W_rule.pop()
                            W_ruleI.pop()
                            # W_ruleII.pop()
                            z = ru + " " + ''.join(re.findall(r'[A-Za-z]', word))
                        else:
                            z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
                    else:
                        z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
            else:
                rule.append(word)
                lenth = len(b[-1])
                if len(b) < 2:
                    b.insert(0, "0")
                if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                    #                     print(W_rule[-1][0:lenth])  # 核实是否有规则未满
                    if b[-1] == W_rule[-1][0:lenth] and b[-2] == W_ruleI[-1]:  # 判断其父节点是否和未满规则一致
                        ru = W_rule.pop()
                        W_ruleI.pop()

                        z = ru + " " + ''.join(re.findall(r'[A-Za-z]', word))
                    else:
                        z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
                else:
                    z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))

        else:
            b.append(char)

    return rule


def all_np(arr):
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result


def corpus_segment(corpus_path):
    Type_list = os.listdir(corpus_path)  # 返回该目录下面所有文件夹
    print(Type_list)
    for mydir0 in Type_list:
        Partname = corpus_path + mydir0 + "/"
        TypeEword_list = []
        TypeCword_list = []
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹

        for mydir in file_list:
            try:
                f2 = open('../NLP_规则/非叶子节点规则/成功/' + mydir0 + '/' + mydir[:-7] + '.csv', 'a+')
                f3 = open('../NLP_规则/叶子节点规则/成功/' + mydir0 + '/' + mydir[:-7] + '.csv', 'a+')
                writer2 = csv.writer(f2)
                writer3 = csv.writer(f3)
                writer2.writerow(["规则", '次数'])
                writer3.writerow(["规则", '次数'])
                Eword_list = []
                Cword_list = []
                print(mydir[:-7])
                fullname = Partname + mydir
                with open(fullname, 'r', encoding="utf-8")as fp:
                    content = fp.readlines()  # 读取文件内容
                    for word in content:

                        print(word)
                        pattern = re.compile(r"['](.*?)[']")
                        word = pattern.findall(word)
                        z = process(word)

                        print(z)
                        B = True
                        for word1 in z:
                            if len(word1) < 1:
                                continue;
                            if (word1[-1] >= u'\u0041' and word1[-1] <= u'\u005a') or (
                                    word1[-1] >= u'\u0061' and word1[-1] <= u'\u007a'):
                                Eword_list.append(word1)
                                TypeEword_list.append(word1)
                            else:
                                Cword_list.append(word1)
                                TypeCword_list.append(word1)

                    rule_list2 = all_np(Eword_list)
                    rule_list2 = sorted(rule_list2.items(), key=lambda item: item[1], reverse=True)
                    rule_list3 = all_np(Cword_list)
                    rule_list3 = sorted(rule_list3.items(), key=lambda item: item[1], reverse=True)

                    for i in range(rule_list2.__len__()):
                        writer2.writerow([rule_list2[i][0], rule_list2[i][1]])

                    for i in range(rule_list3.__len__()):
                        writer3.writerow([rule_list3[i][0], rule_list3[i][1]])
                f2.close()
                f3.close()
            except Exception as err:
                print(err)
                with open("日志.txt", 'a+', encoding="utf-8")as fp3:
                    fp3.write(mydir[:-7] + "/")


# with open("../NLP_短语/不成功/"+mydir0+"/"+mydir, 'a', encoding="utf-8")as fp1:#写入文件
#                 content=fp1.readlines()
#                 for word in content:
#                     print(word)
#                     if len(word)>3:
#
#                         # print ('Part of Speech:', nlp.pos_tag(sentence))
#                         # print ('Named Entities:', nlp.ner(sentence))
#             #             print('Named Entities:', k)
#                         z=process(word)
#                         print(z)
# #                         fp1.write(repr(f)+"\n")



if __name__ == "__main__":
    #     nlp=StanfordCoreNLP(r'D:/myproject/stanford_nlp',lang='zh')
    #     sentence = '他们遵守着人类设定的三大机器人原则，为人类服务。'
    # k=nlp.parse(word)
    corpus_segment("../NLP_短语/成功/")





    # # T=['(', 'ROOT', '(', 'IP', '(', 'NP', '(', 'PN他们', ')', ')', '(', 'VP', '(', 'VP', '(', 'VV遵守', ')', '(', 'AS着', ')', '(', 'NP', '(', 'NP', '(', 'CP', '(', 'IP', '(', 'NP', '(', 'NN人类', ')', ')', '(', 'VP', '(', 'VV设定', ')', ')', ')', '(', 'DEC的', ')', ')', '(', 'QP', '(', 'CD三', ')', ')', '(', 'ADJP', '(', 'JJ大', ')', ')', '(', 'NP', '(', 'NN机器人', ')', ')', ')', '(', 'NP', '(', 'NN原则', ')', ')', ')', ')', '(', 'PU，', ')', '(', 'VP', '(', 'PP', '(', 'P为', ')', '(', 'NP', '(', 'NN人类', ')', ')', ')', '(', 'VP', '(', 'VV服务', ')', ')', ')', ')', '(', 'PU。', ')', ')', ')']
    # z=process(f)
    # print(z)
    # tree=Tree.fromstring(t)
    # tree.draw()
    #     nlp.close()

    # print ('Dependency Parsing:', nlp.dependency_parse(sentence))