import xlrd
import numpy as np
import os
import  pandas as pd
import csv
import xlwt
from collections import Counter
f = open('./词性统计/游戏/成功小说加句子.csv', 'a+')
f2 = open('./词性统计/游戏/不成功小说加句子.csv', 'a+')
writer = csv.writer(f)
writer2 = csv.writer(f2)
writer.writerow(["小说名","r","v","nh","n","u","nt","p","e","nd","m","d","i","wp","a","句子数"])
writer2.writerow(["小说名","r","v","nh","n","u","nt","p","e","nd","m","d","i","wp","a","句子数"])
# def dictionarylist():
#     T=[]
#     workbook = xlrd.open_workbook(r"E:\NPL prosess\词频语料库\CorpusWordPOSlist.xls")
#     sheet_names = workbook.sheet_names()
#     booksheet0 = workbook.sheet_by_index(0)
#     for i in range(0,14630):
#         row_0 = booksheet0.row_values(i)
#         if  "r" in row_0[2]  :
#             T.append(row_0)
#     arr=np.array(T)
#         # print(arr)
#     return arr
def corpus_segment2(corpus_path):
    G=Counter()
    i=1
    T=[]
    file_list=os.listdir(corpus_path)#返回该目录下面所有文件夹
    for mydir in file_list:
        # print(mydir[:-7])
        juzi=0
        Gantanci=0
        adj=0
        adv=0
        Numb=0
        V=0
        N=0
        nd=0#方位名词
        nt=0#s时间名词
        P=0#介词
        r=0#代词
        wp=0#标点
        nh=0#人名
        u=0#助词
        i=0#成语14
        c = Counter()
        fullname=corpus_path+mydir
        with open(fullname, 'r', encoding="utf-8")as fp:
            content=fp.read()  # 读取文件内容
            words=content.split(" ")
            for word in words:
                if "wp"  in word:
                    if "！"  in word:
                        juzi=juzi+1
                    if "？"  in word :
                        juzi = juzi + 1
                    if "。"  in word :
                        juzi = juzi + 1
                    wp=wp+1
                if "r" in word :
                    r=r+1
                if "v" in word:
                    V = V + 1
                if "a" in word:
                    adj = adj + 1
                if "i" in word:
                    i = i + 1
                if "d" in word:
                    adv = adv + 1
                if "m" in word:
                    Numb = Numb + 1
                if "nd" in word:
                    nd = nd + 1
                if "e" in word:
                    Gantanci = Gantanci + 1
                if "p" in word:
                    P = P + 1
                if "nt" in word:
                    nt = nt + 1
                if "u" in word:
                    u = u + 1
                if "n" in word:
                    N = N + 1
                if "nh" in word:
                    nh = nh + 1

        T.append([mydir[:-7],{"r":r,"v":V,"nh":nh,"n":N,"u":u,"nt":nt,"p":P,"e":Gantanci,"nd":nd,"m":Numb,"d":adv,"i":i,"wp":wp,"a":adj},juzi])

    # print(T)
    return T
if __name__ == "__main__":
    S_word_lst=corpus_segment2("./NLP_Pos/成功词与词性/游戏/")
    F_word_lst = corpus_segment2("./NLP_Pos/不成功词与词性/游戏/")

    # F_word_lst=list(F_word_lst)
    # S_word_lst = list(S_word_lst)

    for i in range(S_word_lst.__len__()):
        if S_word_lst[i][2]==0:
            S_word_lst[i][2]=1
        writer.writerow([S_word_lst[i][0],S_word_lst[i][1]["r"]/S_word_lst[i][2],S_word_lst[i][1]["v"]/S_word_lst[i][2],S_word_lst[i][1]["nh"]/S_word_lst[i][2],S_word_lst[i][1]["n"]/S_word_lst[i][2],S_word_lst[i][1]["u"]/S_word_lst[i][2],S_word_lst[i][1]["nt"]/S_word_lst[i][2],S_word_lst[i][1]["p"]/S_word_lst[i][2],S_word_lst[i][1]["e"]/S_word_lst[i][2],S_word_lst[i][1]["nd"]/S_word_lst[i][2],S_word_lst[i][1]["m"]/S_word_lst[i][2],S_word_lst[i][1]["d"]/S_word_lst[i][2],S_word_lst[i][1]["i"]/S_word_lst[i][2],S_word_lst[i][1]["wp"]/S_word_lst[i][2],S_word_lst[i][1]["a"]/S_word_lst[i][2],S_word_lst[i][2]])
        print(S_word_lst[i])


    for i in range(F_word_lst.__len__()):
        if F_word_lst[i][2]==0:
            F_word_lst[i][2]=1
        writer2.writerow([F_word_lst[i][0],F_word_lst[i][1]["r"]/F_word_lst[i][2],F_word_lst[i][1]["v"]/F_word_lst[i][2],F_word_lst[i][1]["nh"]/F_word_lst[i][2],F_word_lst[i][1]["n"]/F_word_lst[i][2],F_word_lst[i][1]["u"]/F_word_lst[i][2],F_word_lst[i][1]["nt"]/F_word_lst[i][2],F_word_lst[i][1]["p"]/F_word_lst[i][2],F_word_lst[i][1]["e"]/F_word_lst[i][2],F_word_lst[i][1]["nd"]/F_word_lst[i][2],F_word_lst[i][1]["m"]/F_word_lst[i][2],F_word_lst[i][1]["d"]/F_word_lst[i][2],F_word_lst[i][1]["i"]/F_word_lst[i][2],F_word_lst[i][1]["wp"]/F_word_lst[i][2],F_word_lst[i][1]["a"]/F_word_lst[i][2],F_word_lst[i][2]])
        print(F_word_lst[i])
    f.close()
    f2.close()
    # print(word_lst.values())
    # v=0
    # w=1
    # a=[]
    # b=[]
    # # for i in range(F_word_lst.__len__()):
    # #     writer.writerow([F_word_lst[i][0],F_word_lst[i][1]])
    # for i in range(len(F_word_lst)):
    #     for j in range(dic.__len__()):
    #         a.append("")
    #         if F_word_lst[i][0]==dic[j][1]:
    #             v=v+float(dic[j][0])*w
    #             a[j]=2
    # print(v)
    # v = 0
    # for i in range(len(S_word_lst)):
    #     for j in range(dic.__len__()):
    #         b.append("")
    #         if S_word_lst[i][0]==dic[j][1]:
    #             v=v+float(dic[j][0])*w
    #             b[j]=1
    # print(v)
    # for i in range(dic.__len__()):
    #     writer.writerow([i,dic[i][1],b[i],a[i]])
    # # print(dic.__len__())
