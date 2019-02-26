import xlrd
import numpy as np
import os
import  pandas as pd
import csv
import xlwt
from collections import Counter
f = open('./形容词统计/都市/不成功小说.csv', 'a+')
writer = csv.writer(f)
writer.writerow(["排名","词语","成功","出现次数","不成功","出现次数"])
def dictionarylist():
    T=[]
    workbook = xlrd.open_workbook(r"E:\NPL prosess\词频语料库\CorpusWordPOSlist.xls")
    sheet_names = workbook.sheet_names()
    booksheet0 = workbook.sheet_by_index(0)
    for i in range(0,14630):
        row_0 = booksheet0.row_values(i)
        if  "a" in row_0[2]  :
            T.append(row_0)
    arr=np.array(T)
        # print(arr)
    return arr
def corpus_segment2(corpus_path):
    G=Counter()
    i=1

    file_list=os.listdir(corpus_path)#返回该目录下面所有文件夹
    for mydir in file_list:
        # print(mydir[:-7])
        T2=[]
        c = Counter()
        fullname=corpus_path+mydir
        with open(fullname, 'r', encoding="utf-8")as fp:
            content=fp.read()  # 读取文件内容
            words=content.split(" ")
            for word in words:
                if "wp" not in word:
                    if "a" in word :
                        if word!="":
                            T2.append(word[:word.find("/")])

        # print(Counter(T2))
        if i==1:
            G=Counter(T2)
        else:
            G=G+Counter(T2)
        i=i+1
    print(G.most_common(150))
    return G.most_common(100)
if __name__ == "__main__":
    S_word_lst=corpus_segment2("./NLP_Pos/成功词与词性/")
    F_word_lst = corpus_segment2("./NLP_Pos/不成功词与词性/")
    dic=dictionarylist()
    F_word_lst=list(F_word_lst)
    S_word_lst = list(S_word_lst)
    # print(list(word_lst))
    # print(word_lst.values())
    v=0
    w=1
    a=[]
    anum=[]
    b=[]
    bnum = []
    # for i in range(F_word_lst.__len__()):
    #     writer.writerow([F_word_lst[i][0],F_word_lst[i][1]])
    for i in range(len(F_word_lst)):
        for j in range(dic.__len__()):
            a.append("")
            anum.append("")
            if F_word_lst[i][0]==dic[j][1]:
                v=v+float(dic[j][0])*w
                # print(F_word_lst[i][1])
                anum[j]=F_word_lst[i][1]
                a[j]=1
    print(v)
    v = 0
    for i in range(len(S_word_lst)):
        for j in range(dic.__len__()):
            b.append("")
            bnum.append("")
            if S_word_lst[i][0]==dic[j][1]:
                v=v+float(dic[j][0])*w
                bnum[j] = S_word_lst[i][1]
                b[j]=1
    print(v)
    for i in range(dic.__len__()):
        writer.writerow([i,dic[i][1],b[i],bnum[i],a[i],anum[i]])
    # print(dic.__len__())
