# -*- coding: utf-8 -*-
import re
import os
import numpy as np
import xlwt
import csv
import re
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
def process(P_list):
    a=[]#括号栈
    b=[]#短语栈
    word=""#从短语栈中曲出的短语结构存放
    rule=[]#存储规则
    W_rule=[]#存储未满规则
    W_ruleI=[]#规则节点前1位，
    W_ruleII = []  # 规则节点前2位，
    z=""#临时规则存放
    for char in P_list:
        if char =="(":
            a.append(char)
            if z != '':
                W_rule.append(z)
                W_ruleI.append(b[-2])
                if b.__len__()<3:
                    W_ruleII.append("0")
                else:
                    W_ruleII.append(b[-3])
                z=""

            continue

        elif char==")":
            word=b.pop()
            a.pop()
            if('\u4e00' <= word[-1]<= '\u9fff'  ):#判断中文
                rule.append(word)
                lenth=len(b[-1])

                if W_rule.__len__()!=0:#判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                    print(W_rule[-1][0:lenth])#核实是否有规则未满
                    if b[-1]==W_rule[-1][0:lenth] and b[-2]==W_ruleI[-1] and b[-3]==W_ruleII[-1]:#判断其父节点是否和未满规则一致
                        ru=W_rule.pop()
                        W_ruleI.pop()
                        W_ruleII.pop()
                        z=ru+" "+ ''.join(re.findall(r'[A-Za-z]', word))
                    else:
                        z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
                else:
                    z = b[-1] +" "+ ''.join(re.findall(r'[A-Za-z]', word))
            elif (word[-1] >= u'\u0041' and word[-1] <= u'\u005a') or (word[-1] >= u'\u0061' and word[-1] <= u'\u007a'):
                rule.append(z)
                z=""
                if len(b)<1:
                    lenth=0
                else:
                    lenth = len(b[-1])
                if b.__len__()<1:
                    z="0"

                else:

                    if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                        print(W_rule[-1][0:lenth])  # 核实是否有规则未满
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

                if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                    print(W_rule[-1][0:lenth])  # 核实是否有规则未满
                    if b[-1] == W_rule[-1][0:lenth] and b[-2] == W_ruleI[-1] :  # 判断其父节点是否和未满规则一致
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
# with open("../NLP_短语/二次元/一切从斗破苍穹开始前十章.txt", 'r', encoding="utf-8")as fp1:
#     t=fp1.readlines()
#     print(t[0])
# a=[1,2,3,4]
# b=[4,2,6,8]
# c=a+b
# t=all_np(c)
# print(t)
# T=['(', 'ROOT', '(', 'IP', '(', 'NP', '(', 'PN他们', ')', ')', '(', 'VP', '(', 'VP', '(', 'VV遵守', ')', '(', 'AS着', ')', '(', 'NP', '(', 'NP', '(', 'CP', '(', 'IP', '(', 'NP', '(', 'NN人类', ')', ')', '(', 'VP', '(', 'VV设定', ')', ')', ')', '(', 'DEC的', ')', ')', '(', 'QP', '(', 'CD三', ')', ')', '(', 'ADJP', '(', 'JJ大', ')', ')', '(', 'NP', '(', 'NN机器人', ')', ')', ')', '(', 'NP', '(', 'NN原则', ')', ')', ')', ')', '(', 'PU，', ')', '(', 'VP', '(', 'PP', '(', 'P为', ')', '(', 'NP', '(', 'NN人类', ')', ')', ')', '(', 'VP', '(', 'VV服务', ')', ')', ')', ')', '(', 'PU。', ')', ')', ')']
# z=process(T)
# print(z)
# Eword_list=[]
# Cword_list=[]
# for word1 in z:
#     if (word1[-1] >= u'\u0041' and word1[-1]<=u'\u005a') or (word1[-1] >= u'\u0061' and word1[-1]<=u'\u007a'):
#         Eword_list.append(word1)
#     else:
#         Cword_list.append(word1)
#
#
# print(Eword_list)
# print(Cword_list)
#
# rule_list2=all_np(Eword_list)
# rule_list2= sorted(rule_list2.items(), key=lambda item:item[1],reverse=True)
# rule_list3=all_np(Cword_list)
# rule_list3= sorted(rule_list3.items(), key=lambda item:item[1],reverse=True)
# print(rule_list2)
# print(rule_list3)
# f2 = open('./测试.csv', 'a+')
# writer2 = csv.writer(f2)
# writer2.writerow(["规则", '次数'])
# if (len(rule_list2)>len(rule_list3)):
#     for i in range(rule_list2.__len__()):
#         if i+3>len(rule_list3):
#             rule_list3.append(["",""])
#         writer2.writerow([rule_list2[i][0],rule_list2[i][1],rule_list3[i][0],rule_list3[i][1]])
# else:
#     for i in range(rule_list3.__len__()):
#         if i+3>len(rule_list2):
#             rule_list2.append(["",""])
#         writer2.writerow([rule_list2[i][0],rule_list2[i][1],rule_list3[i][0],rule_list3[i][1]])
# f2.close()
def process(P_list):
    a=[]#括号栈
    b=[]#短语栈
    word=""#从短语栈中曲出的短语结构存放
    rule=[]#存储规则
    W_rule=[]#存储未满规则
    W_ruleI=[]#规则节点前1位，
    W_ruleII = []  # 规则节点前2位，
    z=""#临时规则存放
    for char in P_list:
        if char =="(":
            a.append(char)
            if z != '':
                W_rule.append(z)
                if b.__len__()>1:
                    W_ruleI.append(b[-2])
                else:
                    W_ruleI.append("0")
                if b.__len__()<3:
                    W_ruleII.append("0")
                else:
                    W_ruleII.append(b[-3])
                z=""

            continue

        elif char==")":
            word=b.pop()
            if len(a)>0:
                a.pop()
            if('\u4e00' <= word[-1]<= '\u9fff'  ):#判断中文
                rule.append(word)
                lenth=len(b[-1])
                if len(b)<3:
                    b.insert(0,"0")
                if W_rule.__len__()!=0:#判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                    print(W_rule[-1][0:lenth])#核实是否有规则未满
                    if b[-1]==W_rule[-1][0:lenth] and b[-2]==W_ruleI[-1] and b[-3]==W_ruleII[-1]:#判断其父节点是否和未满规则一致
                        ru=W_rule.pop()
                        W_ruleI.pop()
                        W_ruleII.pop()
                        z=ru+" "+ ''.join(re.findall(r'[A-Za-z]', word))
                    else:
                        z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
                else:
                    z = b[-1] +" "+ ''.join(re.findall(r'[A-Za-z]', word))
            elif (word[-1] >= u'\u0041' and word[-1] <= u'\u005a') or (word[-1] >= u'\u0061' and word[-1] <= u'\u007a'):
                rule.append(z)
                z=""
                if len(b)<1:
                    lenth=0
                else:
                    lenth = len(b[-1])
                if b.__len__()<1:
                    z="0"

                else:
                    if len(b)<2:
                        b.insert(0,"0")
                    if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                        print(W_rule[-1][0:lenth])  # 核实是否有规则未满
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
                if len(b)<2:
                    b.insert(0,"0")
                if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                    print(W_rule[-1][0:lenth])  # 核实是否有规则未满
                    if b[-1] == W_rule[-1][0:lenth] and b[-2] == W_ruleI[-1] :  # 判断其父节点是否和未满规则一致
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
# corpus_path='../NLP_短语/成功/'
# Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹
# print(Type_list)
# for mydir0 in Type_list:
#     Partname=corpus_path+mydir0+"/"
#     TypeEword_list=[]
#     TypeCword_list=[]
#     file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
#     for mydir in file_list:
#         f2 = open('../NLP_规则/成功/'+mydir0+'/'+mydir+'.csv', 'a+')
#         writer2 = csv.writer(f2)
#         writer2.writerow(["规则", '次数',"规则", '次数'])
#         Eword_list=[]
#         Cword_list=[]
#         print(mydir[:-7])
#         fullname=Partname+mydir
#         with open(fullname, 'r', encoding="utf-8")as fp:
#             content=fp.readlines()  # 读取文件内容
#         print(content[0])
#         pattern = re.compile(r"['](.*?)[']")
#         content[0]=pattern.findall(content[0])
#         z=process(content[0])
#         print(z)
# # s="['(', 'ROOT', '(', 'IP', '(', 'IP', '(', 'IP', '(', 'NP', '(', 'DNP', '(', 'QP','(', 'CD三', ')', '(', 'CLP', '(', 'M分钟', ')', ')', ')', '(', 'DEG的', ')', ')', '(', 'NP', '(', 'NN时间', ')', ')', ')', '(', 'PU，', ')', '(', 'VP', '(', 'PP', '(', 'P对于', ')', '(', 'LCP', '(', 'NP', '(', 'QP', '(', 'CD大多数', ')', ')', '(', 'NP', '(', 'NN人', ')', ')', ')', '(', 'LC来说', ')', ')', ')', '(', 'PU，', ')', '(','ADVP', '(', 'AD都', ')', ')', '(', 'VP', '(', 'VC是', ')', '(', 'CP', '(', 'IP','(', 'VP', '(', 'ADVP', '(', 'AD极其', ')', ')', '(', 'VP', '(', 'VA短暂', ')', ')', ')', ')', '(', 'SP的', ')', ')', ')', ')', ')', '(', 'PU，', ')', '(', 'DNP', '(', 'LCP', '(', 'IP', '(', 'NP', '(', 'NN弹指', ')', ')', '(', 'VP', '(', 'ADVP', '(', 'AD一', ')', ')', '(', 'VP', '(', 'VV挥', ')', ')', ')', ')', '(', 'LC间', ')', ')', '(', 'SP罢了', ')', ')', ')', '(', 'PU！', ')', ')', ')']"
#
#

f2 = open('111.csv', 'a+')
writer2 = csv.writer(f2)
writer2.writerow(["规则", '次数'])

writer2.writerow(["ip  root","13" ])