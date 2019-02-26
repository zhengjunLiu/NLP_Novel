import os
import csv
import xlwt
import  numpy as np
# 标点二元文法

# 词类二元文法（去标点）

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
def corpus_segment2(corpus_path):
    Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹

    print(Type_list)
    for mydir in Type_list:
        H = []
        m = 1
        Partname = corpus_path + mydir + "/"
        f2 = open('./词性Bi-Gram/'+mydir +'/成功小说词性Bi-Gram统计.csv', 'a+')
        writer2 = csv.writer(f2)
        writer2.writerow(["词性", '次数'])
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
        for mydir in file_list:
            print(mydir[:-7])
            fullname=Partname+mydir
            with open(fullname, 'r', encoding="utf-8")as fp:
                content=fp.read()  # 读取文件内容
                x_q=''#词类二元文法第一个词性
                x_h=''#词类二元文法第而个词性
                pos_2n=[]#词类二元文法,所有词性组合
                i=1#标识符，判断词性是否前移、

                words=content.split(" ")
                for word in words:
                    if "wp" not in word:
                        if word!="":
                            if i==1:
                                x_q=word[word.find("/"):]
                            else:
                                x_h=word[word.find("/"):]
                            if (i%2==0):
                                pos_2n.append(x_q+" "+x_h)
                                x_q=x_h
                                x_h=''
                        i=i+1
                # print(pos_2n)
                t=all_np(pos_2n)
                z=sorted(t.items(),key= lambda item:item[1],reverse=True)
                print([[z[0][0],z[0][1]],[z[1][0],z[1][1]],[z[2][0],z[2][1]],[z[3][0],z[3][1]],[z[4][0],z[4][1]],[z[5][0],z[5][1]],[z[6][0],z[6][1]],[z[7][0],z[7][1]],[z[8][0],z[8][1]],[z[9][0],z[9][1]]])

                if m==1:
                    H=[[z[0][0],z[0][1]],[z[1][0],z[1][1]],[z[2][0],z[2][1]],[z[3][0],z[3][1]],[z[4][0],z[4][1]],[z[5][0],z[5][1]],[z[6][0],z[6][1]],[z[7][0],z[7][1]],[z[8][0],z[8][1]],[z[9][0],z[9][1]]]
                else:
                    for i in range(10):
                        B = False
                        for j in range(H.__len__()):
                            if z[i][0] == H[j][0]:
                                H[j][1] = H[j][1] + z[i][1]
                                B = True
                        if B == False:
                            H.append([z[i][0], z[i][1]])
            m=m+1
        try:
            print(H)
            for i in range(H.__len__()):
                writer2.writerow([H[i][0],H[i][1]])
            f2.close()
        except Exception  as e:  # 处理Error1异常
            print(e)
#             writer.writerow([mydir[:-9],z[0][0],z[1][0],z[2][0],z[3][0],z[4][0],z[5][0],z[6][0],z[7][0],z[8][0],z[9][0]])
#
#             writer.writerow([mydir[:-9],z[0][0],z[0][1],z[1][0],z[1][1],z[2][0],z[2][1],z[3][0],z[3][1],z[4][0],z[4][1],z[5][0],z[5][1],z[6][0],z[6][1],z[7][0],z[7][1],z[8][0],z[8][1],z[9][0],z[9][1]])
# 3元文法（去标点）


def corpus_segment3(corpus_path):
    Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹
    print(Type_list)
    for mydir in Type_list:
        H = []
        m = 1
        Partname = corpus_path + mydir + "/"
        f3 = open('./Tri-Gram/'+mydir +'/成功小说词性Bi-Gram统计.csv', 'a+')
        writer3 = csv.writer(f3)
        writer3.writerow(["词性", "出现次数"])
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
        for mydir in file_list:
            print(mydir[:-7])
            fullname=Partname+mydir
            with open(fullname, 'r', encoding="utf-8")as fp:
                content=fp.read()  # 读取文件内容
                x_q=''#词类3元文法第一个词性
                x_m=''#词类3元文法第二个词性
                x_h=''#词类3元文法第三个词性
                pos_2n=[]#词类二元文法,所有词性组合
                i=1#标识符，判断词性是否前移

                words=content.split(" ")

                for word in words:
                    if "wp" not in word:
                        if word!="":
                            if i==1:
                                x_q=word[:word.find("/")]
                            elif i ==2:
                                x_m=word[:word.find("/")]
                            else:
                                x_h = word[:word.find("/")]
                            if (i%3==0):
                                pos_2n.append(x_q+" "+x_m+" "+x_h)
                                x_q=x_m
                                x_m=x_h
                                x_h=''
                        i=i+1
                # print(pos_2n)
                t=all_np(pos_2n)
                z=sorted(t.items(),key= lambda item:item[1],reverse=True)
                print([[z[0][0],z[0][1]],[z[1][0],z[1][1]],[z[2][0],z[2][1]],[z[3][0],z[3][1]],[z[4][0],z[4][1]],[z[5][0],z[5][1]],[z[6][0],z[6][1]],[z[7][0],z[7][1]],[z[8][0],z[8][1]],[z[9][0],z[9][1]]])

                if m==1:
                    H=[[z[0][0],z[0][1]],[z[1][0],z[1][1]],[z[2][0],z[2][1]],[z[3][0],z[3][1]],[z[4][0],z[4][1]],[z[5][0],z[5][1]],[z[6][0],z[6][1]],[z[7][0],z[7][1]],[z[8][0],z[8][1]],[z[9][0],z[9][1]]]
                else:
                    for i in range(10):
                        B = False
                        for j in range(H.__len__()):
                            if z[i][0] == H[j][0]:
                                H[j][1] = H[j][1] + z[i][1]
                                B = True
                        if B == False:
                            H.append([z[i][0], z[i][1]])
            m=m+1
        try:
            print(H)
            for i in range(H.__len__()):
                writer3.writerow([H[i][0],H[i][1]])
            f3.close()
        except Exception  as e:  # 处理Error1异常
            print(e)
            # print(z)
            # writer.writerow([mydir[:-9],z[0][0],z[1][0],z[2][0],z[3][0],z[4][0],z[5][0],z[6][0],z[7][0],z[8][0],z[9][0]])
            # writer.writerow([mydir[:-9],z[0][0],z[0][1],z[1][0],z[1][1],z[2][0],z[2][1],z[3][0],z[3][1],z[4][0],z[4][1],z[5][0],z[5][1],z[6][0],z[6][1],z[7][0],z[7][1],z[8][0],z[8][1],z[9][0],z[9][1]])
# 4元文法（去标点）


if __name__ == "__main__":
    corpus_segment2("./NLP_Pos/成功词与词性/")
    # corpus_segment3("./NLP_Pos/成功词与词性/")

