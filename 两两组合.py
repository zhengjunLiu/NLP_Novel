import xlrd
import numpy as np
import os
import pandas as pd
import csv
import xlwt
from collections import Counter

def hebinglist(path,lenth):
    T = []
    workbook = xlrd.open_workbook(path)
    sheet_names = workbook.sheet_names()
    booksheet0 = workbook.sheet_by_index(0)
    for i in range(0, lenth):
        print(i)
        row_0 = booksheet0.row_values(i)
        T.append(row_0)
    arr = np.array(T)
    # print(arr)
    return arr

def HB(path_save,path_l,path_s,numbel,numbe2):
    fp1 = open(path_save, 'a+', newline='')
    writer1 = csv.writer(fp1)

    S_word_lst = hebinglist(path_l, numbel,)
    # F_word_lst = hebinglist("./weka/都市/都市_p叶子.xlsx",221)
    F_word_lst2 = hebinglist(path_s,numbe2 )
    for i in range(len(F_word_lst2)):
        T = []
        for j in range(len(S_word_lst)):
            if F_word_lst2[i][0] == S_word_lst[j][0]:
                for p in range(401):
                    T.append(S_word_lst[j][p])
                for p in range(1, 202):
                    T.append(F_word_lst2[i][p])
                print(F_word_lst2[i][0])
        if T.__len__()==0:
            continue
        writer1.writerow(T)
    fp1.close()


if __name__ == "__main__":
    # fp = open('./weka/都市/游戏_p叶子合并pos.txt', 'a+', encoding="utf-8")
    # HB('./weka/都市/都市_Unigram+Pcfg_叶子+虚词.csv',"./weka/都市/都市_Unigram+Pcfg_叶子.xlsx","./weka/都市/都市_虚词.xlsx",471,1072)
    HB('./weka/二次元/二次元_Unigram+Pcfg_叶子+虚词.csv',"./weka/二次元/二次元_Unigram+Pcfg_叶子.xlsx","./weka/二次元/二次元_虚词.xlsx",326,326)
    # HB('./weka/历史/历史_Unigram+Pcfg_叶子+虚词.csv',"./weka/历史/历史_Unigram+Pcfg_叶子.xlsx","./weka/历史/历史_虚词.xlsx",145,571)
    # HB('./weka/奇幻/奇幻_Unigram+Pcfg_叶子+虚词.csv',"./weka/奇幻/奇幻_Unigram+Pcfg_叶子.xlsx","./weka/奇幻/奇幻_虚词.xlsx",190,190)
    # HB('./weka/玄幻/玄幻_Unigram+Pcfg_叶子+虚词.csv',"./weka/玄幻/玄幻_Unigram+Pcfg_叶子.xlsx","./weka/玄幻/玄幻_虚词.xlsx",1170,1643)
    # HB('./weka/游戏/游戏_Unigram+Pcfg_叶子+虚词.csv',"./weka/游戏/游戏_Unigram+Pcfg_叶子.xlsx","./weka/游戏/游戏_虚词.xlsx",221,464)











































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































