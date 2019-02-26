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
def corpus_segment(corpus_path):#合并成功与不成功小说
    Type_list = os.listdir(corpus_path)  # 返回该目录下面所有文件夹
    print(Type_list)
    for mydir0 in Type_list:
        H = []
        m = 1
        Partname = corpus_path + mydir0 + "/"
        f3 = open('./Uni-gram-02/' + mydir0 + '_Uni-gram.csv', 'a+',newline='')
        writer3 = csv.writer(f3)
        writer3.writerow(["小说名", '标准化类符/形符比',"类别"])
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
        for mydir1 in file_list:

            fullname = Partname + mydir1
            print(fullname)
            try:
                csv_reader0 = csv.reader(open(fullname))
                Lz = 0
                for row_0 in csv_reader0:
                    if Lz == 0:
                        Lz = Lz + 1
                        continue
                    else:
                        if len(row_0)!=0:
                            writer3.writerow([row_0[0], row_0[1]])
            except OverflowError:
                print('wrong')

def corpus_segment2(corpus_path):#合并所有统计
    Type_list = os.listdir(corpus_path)  # 返回该目录下面所有文件夹
    print(Type_list)
    T_list=[]
    for mydir0 in Type_list:
        T_key = []
        T_value=[]
        m = 1
        Partname = corpus_path + mydir0 + "/"
        f3 = open('./Uni-gram-02/' + mydir0 + '_Uni-gram.csv', 'a+',newline='')
        writer3 = csv.writer(f3)
        writer3.writerow(["单词","出现次数"])
        z=[]
        file_list = os.listdir(Partname)
        for mydir1 in file_list:

                fullname = Partname + mydir1
                print(fullname)
                try:
                    csv_reader0 = csv.reader(open(fullname))
                    Lz = 0
                    for row_0 in csv_reader0:
                        if Lz == 0:
                            Lz = Lz + 1
                            continue
                        else:
                            if len(row_0)!=0:
                                if row_0[0] not in T_key:
                                    T_key.append(row_0[0])
                                    T_value.append(int(float(row_0[1])))
                                else:
                                    for y in range(len(T_key)):
                                        if row_0[0] == T_key[y]:
                                            T_value[y] = int(T_value[y]) + int(row_0[1])
                except OverflowError:
                    print('wrong')
        T_list=dict(zip(T_key, T_value))
        l_dic = sorted(T_list.items(), key=lambda x: x[1], reverse=True)
        for i in range(200):
            writer3.writerow([l_dic[i][0],l_dic[i][1]])
if __name__ == "__main__":
    corpus_segment2("./Uni-gram-01/")