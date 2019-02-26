import os
import xlwt
import os
import csv
import xlrd
import  numpy as np

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

def he_bing(t_path):
    Type_list = os.listdir(t_path)  # 返回该目录下面所有文件夹
    print(Type_list)
    T_list = []  # 类别所有的集合
    for mydir0 in Type_list:
        Partname = t_path + "/"+mydir0
        fullname = Partname +"/合并.xlsx"
        T_key = []
        T_value = []
        print(fullname)
        z = 0
        try:
            workbook = xlrd.open_workbook(fullname)
            sheet_names = workbook.sheet_names()
            booksheet0 = workbook.sheet_by_index(0)

            for i in range(0,800):
                row_0 = booksheet0.row_values(i)
                if z == 0:
                    z = z + 1
                    continue
                else:
                    if row_0[0] not in T_key:
                        T_key.append(row_0[0])
                        T_value.append(row_0[1])
                    else:
                        for y in range(len(T_key)):
                            if row_0[0] == T_key[y]:
                                T_value[y]=T_value[y]+row_0[1]
                z = z + 1
        except Exception as err:
            print(err)
        T_list.append([mydir0,dict(zip(T_key, T_value))])
        print(mydir0)
    return T_list
def duqu(path_1):
    Type_list0 = os.listdir(path_1)  # 返回该目录下面所有文件夹
    print(Type_list0)
    T_list0= []  # 类别所有的集合
    name_list0 = []
    Rule_list1 = []  # 存放前200规则
    Rule_list2 = []  # 存放每本小说前200规则的值
    for mydir0 in Type_list0:
        Partname0 = path_1 +"/"+ mydir0 + "/小说词性2元文法统计.csv"
        csv_reader0 = csv.reader(open(Partname0,encoding="utf-8"))
        Lz = 0

        Rule_1 = []
        Rule_2 = []
        for row_0 in csv_reader0:
            if Lz == 0:
                Lz = Lz + 1
                continue
            else:
                if len(row_0) != 0:
                    # print(row_0[1])
                    Rule_1.append(row_0[1])
                    Rule_2.append(row_0[2])
        if Rule_1.__len__()!=0:
            Rule_list1.append([mydir0,Rule_1])
    return Rule_list1

def corpus_segment(corpus_path,t_list):
    Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹
    # print(Type_list)
    T_list = []#类别所有的集合
    name_list=[]
    for mydir0 in Type_list:
        B = True
        Partname1 = corpus_path + mydir0 + "/"
        file_list = os.listdir(Partname1)  # 返回该目录下面所有文件夹
        H = []
        m = 1
        B=False
        fp = open('./词性Bi-Gram/' + mydir0 + '/不成功.txt', 'a+', encoding="utf-8")
        fp.write("小说名" + ",")
        Lz = 0
        Rule_list1 = []  # 存放前200规则
        Rule_list2 = []  # 存放每本小说前200规则的值
        Rule_1 = []
        for i in range(12):
            if mydir0 in t_list[i][0]:
                Rule_list1 =t_list[i][1]
                B=True
        if B==False:
            continue
        for p in range(18):
            Rule_list2.append(0)
            print(Rule_list1[p])
            fp.write(Rule_list1[p] + ",")
        fp.write("\n")
        for mydir in file_list:
            T_key = []
            T_value=[]
            fullname = Partname1 + mydir
            print(fullname)
            csv_reader =  csv.reader(open(fullname))
            z=0
            name_list.append(mydir[:-7])
            fp.write(mydir[:-7] + ",")
            with open(fullname, 'r', encoding="utf-8")as fp1:
                content = fp1.read()  # 读取文件内容
                x_q = ''  # 词类二元文法第一个词性
                x_h = ''  # 词类二元文法第而个词性
                pos_2n = []  # 词类二元文法,所有词性组合
                i = 1  # 标识符，判断词性是否前移、
                words = content.split(" ")
                for word in words:
                    if "wp" not in word:
                        if word != "":
                            if i == 1:
                                x_q = word[word.find("/"):]
                            else:
                                x_h = word[word.find("/"):]
                            if (i % 2 == 0):
                                pos_2n.append(x_q + x_h)
                                x_q = x_h
                                x_h = ''
                        i = i + 1
                # print(pos_2n)
                Z_numb=pos_2n.__len__()
                t = all_np(pos_2n)
                z = sorted(t.items(), key=lambda item: item[1], reverse=True)
                for i in range(z.__len__()):
                    # print(T_key[i])
                    # print(Rule_list1[k])
                    for j in range(18):
                        if z[i][0] in Rule_list1[j]:
                            Rule_list2[j]=round(float(z[i][1])/float(Z_numb),6)

            for o in range(18):
                fp.write(str(Rule_list2[o])+",")
            fp.write("\n")


if __name__ == "__main__":
    z=duqu("./词性组合")
    for i in range(z.__len__()):
        print(z[i])
    corpus_segment("./NLP_Pos/不成功词与词性/", z)