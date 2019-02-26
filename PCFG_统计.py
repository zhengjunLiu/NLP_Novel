import os
import xlwt
import os
import csv
import xlrd
def Dic_combine (dica , dicb):#合并字典
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
    for mydir0 in Type_list:
        T_list = []#类别所有的集合
        z_dic={}#第一次合并的字典
        l_dic={}#返回的后续字典
        Partname=corpus_path+mydir0+"/"
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
        for mydir in file_list:
            T_key = []
            T_value=[]
            fullname = Partname + mydir
            print(fullname)
            csv_reader =  csv.reader(open(fullname))
            z=0
            for row_0 in csv_reader:
                if z == 0:
                    z = z + 1
                    continue
                else:
                    if len(row_0)!=0:
                        T_key.append(row_0[0])
                        T_value.append(row_0[1])
                z=z+1
            T_list.append(dict(zip(T_key,T_value)))#将每本小说加入列表
        for i in range(len(T_list)):
            if i ==0:
                continue
            elif i==1:
                z_dic =Dic_combine(T_list[i-1],T_list[i])
            else:
                l_dic=Dic_combine(z_dic,T_list[i])

        l_dic=sorted(l_dic.items(), key=lambda x: x[1], reverse=True)
        f2 = open('./NLP_规则/叶子节点统计/不成功/'+mydir0+'.csv', 'a+')
        writer2 = csv.writer(f2)
        writer2.writerow(["规则", '次数'])
        for i in range(l_dic.__len__()):
            writer2.writerow([l_dic[i][0],l_dic[i][1]])

if __name__ == "__main__":
    corpus_segment("./NLP_规则/叶子节点规则/不成功/")