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
    for mydir0 in Type_list:
        H = []
        m = 1
        Partname = corpus_path + mydir0 + "/"
        f1 = open('./虚词统计/' + mydir0+'/不成功虚词统计.csv', 'a+',newline="")
        writer1 = csv.writer(f1)
        writer1.writerow(["虚词", "出现次数"])
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
        pos_2n = []  # 所有词性组合
        for mydir in file_list:
            # f2 = open('./TTR/' + mydir0+"/"+ mydir[:-7]+ '类符统计.csv', 'a+')
            # writer2 = csv.writer(f2)
            # writer2.writerow(["词性", '次数'])
            wordsum=0
            fullname=Partname+mydir
            print(mydir[:-7])
            with open(fullname, 'r', encoding="utf-8")as fp:
                content=fp.read()  # 读取文件内容
                x_q=''#取第一个词
                i=1#标识符，判断词性是否前移
                words=content.split(" ")
                for word in words:
                    if "wp" not in word:
                        if word!="":
                            if "d" in word[word.find("/"):]:#副词
                                x_q = word[:word.find("/")]
                                pos_2n.append(x_q)
                            if "u" in word[word.find("/"):]:#助词
                                x_q = word[:word.find("/")]
                                pos_2n.append(x_q)
                            if "p" in word[word.find("/"):]:#介词
                                x_q = word[:word.find("/")]
                                pos_2n.append(x_q)
                            if "e" in word[word.find("/"):]:#叹词
                                x_q = word[:word.find("/")]
                                pos_2n.append(x_q)
                            if "o" in word[word.find("/"):]:#拟声词
                                x_q = word [:word.find("/")]
                                pos_2n.append(x_q)
                # print(pos_2n)
        t=all_np(pos_2n)
        print(1)
        z=sorted(t.items(),key= lambda item:item[1],reverse=True)
        print(2)
        for i in range(1000):
            print([z[i][0], z[i][1]])
            writer1.writerow([z[i][0], z[i][1]])
        f1.close()
            # f2.close()
                # print([[z[0][0],z[0][1]],[z[1][0],z[1][1]],[z[2][0],z[2][1]],[z[3][0],z[3][1]],[z[4][0],z[4][1]],[z[5][0],z[5][1]],[z[6][0],z[6][1]],[z[7][0],z[7][1]],[z[8][0],z[8][1]],[z[9][0],z[9][1]]])

            #     if m==1:
            #         H=[[z[0][0],z[0][1]],[z[1][0],z[1][1]],[z[2][0],z[2][1]],[z[3][0],z[3][1]],[z[4][0],z[4][1]],[z[5][0],z[5][1]],[z[6][0],z[6][1]],[z[7][0],z[7][1]],[z[8][0],z[8][1]],[z[9][0],z[9][1]]]
            #     else:
            #         for i in range(10):
            #             B = False
            #             for j in range(H.__len__()):
            #                 if z[i][0] == H[j][0]:
            #                     H[j][1] = H[j][1] + z[i][1]
            #                     B = True
            #             if B == False:
            #                 H.append([z[i][0], z[i][1]])
            # m=m+1


            # f2.close()
if __name__ == "__main__":
    corpus_segment2("./NLP_Pos/不成功词与词性/")