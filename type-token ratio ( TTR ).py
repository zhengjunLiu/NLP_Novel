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
def duqu(path_1):
    Type_list0 = os.listdir(path_1)  # 返回该目录下面所有文件夹
    print(Type_list0)
    T_list0= []  # 类别所有的集合
    name_list0 = []
    Rule_list1 = []  # 存放前200规则
    Rule_list2 = []  # 存放每本小说前200规则的值
    for mydir0 in Type_list0:
        Partname0 = path_1 +"/"+ mydir0
        csv_reader0 = csv.reader(open(Partname0))
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
                    Rule_1.append(row_0[0])
                    Rule_2.append(row_0[1])
        if Rule_1.__len__()!=0:
            Rule_list1.append([mydir0[:-9],Rule_1])
    return Rule_list1
def corpus_segment2(corpus_path):#TTR
    Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹

    print(Type_list)
    for mydir0 in Type_list:
        H = []
        m = 1
        Partname = corpus_path + mydir0 + "/"
        f1 = open('./TTR/' + mydir0+'/成功类符统计.csv', 'a+')
        writer1 = csv.writer(f1)
        writer1.writerow(["小说名", '标准化类符/形符比',"类别"])
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
        for mydir in file_list:
            # f2 = open('./TTR/' + mydir0+"/"+ mydir[:-7]+ '类符统计.csv', 'a+')
            # writer2 = csv.writer(f2)
            # writer2.writerow(["词性", '次数'])
            wordsum=0
            fullname=Partname+mydir
            with open(fullname, 'r', encoding="utf-8")as fp:
                content=fp.read()  # 读取文件内容
                x_q=''#取第一个词

                pos_2n=[]#所有词性组合
                i=1#标识符，判断词性是否前移
                words=content.split(" ")
                for word in words:
                    if "wp" not in word:
                        if word!="":
                            x_q = word[:word.find("/")]
                            pos_2n.append(x_q)
                # print(pos_2n)
                t=all_np(pos_2n)
                z=sorted(t.items(),key= lambda item:item[1],reverse=True)
            print(mydir[:-7])
            for i in range(z.__len__()):
                wordsum=wordsum+int(z[i][1])
                # writer2.writerow([z[i][0],z[i][1]])
            print(str(wordsum)+" "+str(z.__len__()))
            writer1.writerow([mydir[:-7], str(round(z.__len__()/wordsum,6)),"succ"])
        f1.close()

def corpus_segment1(corpus_path,T_list):#虚词
    Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹

    print(Type_list)
    for mydir0 in Type_list:
        H = []
        m = 1
        Rule_list2=[]
        Partname = corpus_path + mydir0 + "/"
        fp0 = open('./虚词-02/' + mydir0 + '/成功虚词.txt', 'a+', encoding="utf-8")
        fp0.write("小说名" + ",")
        for i in range(6):
            if mydir0 in T_list[i][0]:
                Rule_list1 =T_list[i][1]
        for p in range(200):
            Rule_list2.append(0)
            print(Rule_list1[p])
            fp0.write(Rule_list1[p] + ",")
        fp0.write("\n")
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
        for mydir in file_list:
            print(mydir[:-7])
            fp0.write(mydir[:-7]+ ",")
            wordsum=0
            fullname=Partname+mydir
            with open(fullname, 'r', encoding="utf-8")as fp:
                content=fp.read()  # 读取文件内容
                x_q=''#取第一个词
                wordsum=0
                pos_2n=[]#所有词性组合
                i=1#标识符，判断词性是否前移
                words=content.split(" ")
                for word in words:
                    if "wp" not in word:
                        wordsum=wordsum+1
                        if "d"  in word[word.find("/"):]:
                            x_q = word[:word.find("/")]
                            pos_2n.append(x_q)
                        if "u"  in word[word.find("/"):]:
                            x_q = word[:word.find("/")]
                            pos_2n.append(x_q)
                        if "p"  in word[word.find("/"):]:
                            x_q = word[:word.find("/")]
                            pos_2n.append(x_q)
                        if "e"  in word[word.find("/"):]:
                            x_q = word[:word.find("/")]
                            pos_2n.append(x_q)
                        if "o"  in word[word.find("/"):]:
                            x_q = word[:word.find("/")]
                            pos_2n.append(x_q)
                # print(pos_2n)
            t=all_np(pos_2n)
            z=sorted(t.items(),key= lambda item:item[1],reverse=True)
            for i in range(z.__len__()):
                # print(T_key[i])
                # print(Rule_list1[k])
                for j in range(200):
                    if z[i][0] in Rule_list1[j]:
                        Rule_list2[j]=round(float(z[i][1])/float(wordsum),6)
            for o in range(200):
                fp0.write(str(Rule_list2[o])+",")
            fp0.write("\n")
        fp0.close()
def corpus_segment3(corpus_path,T_list):#Unigram
    Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹

    print(Type_list)
    for mydir0 in Type_list:
        H = []
        m = 1
        Rule_list2=[]
        Partname = corpus_path + mydir0 + "/"
        fp0 = open('./Uni-gram-03/' + mydir0 + '/不成功Unigram.txt', 'a+', encoding="utf-8")
        fp0.write("小说名" + ",")
        for i in range(6):
            if mydir0 in T_list[i][0]:
                Rule_list1 =T_list[i][1]
        for p in range(200):
            Rule_list2.append(0)
            print(Rule_list1[p])
            fp0.write(Rule_list1[p] + ",")
        fp0.write("class")
        fp0.write("\n")
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
        for mydir in file_list:
            print(mydir[:-7])
            fp0.write(mydir[:-7]+ ",")
            wordsum=0
            fullname=Partname+mydir
            with open(fullname, 'r', encoding="utf-8")as fp:
                content=fp.read()  # 读取文件内容
                x_q=''#取第一个词
                wordsum=0
                pos_2n=[]#所有词性组合
                i=1#标识符，判断词性是否前移
                words=content.split(" ")
                for word in words:
                    if "wp" not in word:
                        wordsum=wordsum+1
                        x_q = word[:word.find("/")]
                        pos_2n.append(x_q)
                # print(pos_2n)
            t=all_np(pos_2n)
            z=sorted(t.items(),key= lambda item:item[1],reverse=True)
            for i in range(z.__len__()):
                # print(T_key[i])
                # print(Rule_list1[k])
                for j in range(200):
                    if z[i][0] in Rule_list1[j]:
                        Rule_list2[j]=round(float(z[i][1])/float(wordsum),6)
            for o in range(200):
                fp0.write(str(Rule_list2[o])+",")
            fp0.write("unsucc")
            fp0.write("\n")
        fp0.close()
if __name__ == "__main__":
    z = duqu("./Uni-gram-02")
    corpus_segment3("./NLP_Pos/不成功词与词性/",z)