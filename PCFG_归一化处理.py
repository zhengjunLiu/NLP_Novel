import os
import xlwt
import os
import csv
import xlrd
def Dic_combine (dica , dicb):
    dic = {}
    for key in dica:
        if dicb.get(key):
            dic[key] = int(dica[key]) + int(dicb[key])
        else:
            dic[key] = int(dica[key])
    for key in dicb:
        if dica.get(key):
            pass
        else:
            dic[key] = int(dicb[key])
    return dic


def corpus_segment(corpus_path):

    Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹
    print(Type_list)
    k=0
    for mydir0 in Type_list:
        try:
            T_list = []
            z_dic={}
            l_dic={}
            name_list=[]
            Partname=corpus_path+mydir0+"/"
            file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
            fp=open('./NLP_规则/非叶子节点weka/不成功/' + mydir0 + '.txt', 'a+', encoding="utf-8")
            fp.write("小说名"+",")
            csv_reader0 = csv.reader(open("./NLP_规则/非叶子节点统计/"+mydir0+".csv"))
            Lz = 0
            Rule_list1=[]#存放前200规则
            Rule_list2=[]#存放每本小说前200规则的值
            Rule_1 = []

            for row_0 in csv_reader0:
                if Lz == 0:
                    Lz = Lz + 1
                    continue
                else:
                    if len(row_0)!= 0:
                        print(row_0[0])
                        Rule_1.append(row_0[0])
            for p in range(200):
                fp.write(Rule_1[p]+",")
            fp.write("\n")
            Rule_list1.append(Rule_1)


            for mydir in file_list:
                T_key = []
                T_value=[]
                Rule_2 = []
                for p in range(200):
                    Rule_2.append("0")
                fullname = Partname + mydir
                # print(fullname)
                csv_reader =  csv.reader(open(fullname))
                z=0
                name_list.append(mydir[:-4])
                fp.write(mydir[:-4] + ",")
                for row_0 in csv_reader:
                    if z == 0:
                        z = z + 1
                        continue
                    else:
                        if len(row_0)!=0:
                            T_key.append(row_0[0])
                            T_value.append(row_0[1])
                sum =0
                # print(T_key)
                for i in range(T_value.__len__()):
                    sum=sum +int(T_value[i])
                print(sum)
                # print(T_key[0])
                for i in range(T_key.__len__()):
                    # print(T_key[i])
                    # print(Rule_list1[k])
                    for j in range(200):
                        if T_key[i] in Rule_1[j]:
                            Rule_2[j]=round(float(T_value[i])/float(sum),6)

                for o in range(200):
                    fp.write(str(Rule_2[o])+",")
                fp.write("\n")
        except Exception as err:
            print(err)


        # f = xlwt.Workbook()  # 创建工作簿
        # sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
        # sheet1.write(0,0,"小说名")
        # for j in range(200):
        #     sheet1.write(0,j+1,Rule_list1[k][j])
        #
        # for j in range(name_list.__len__()):
        #     print(name_list[j])
        #     sheet1.write(j,0,name_list[j])
        #     print(name_list[j])
        #     for i in range(200):
        #         sheet1.write(j+1,i+1,Rule_list2[j][i])
        #
        # f.save(r'./NLP_规则/叶子节点weka/不成功/'+mydir0+'.xls')
        # k = k + 1
if __name__ == "__main__":
    # corpus_segment("./NLP_规则/非叶子节点规则/不成功/")
    word = "/d"
    x_q = word[word.find("/"):]
    print(x_q)