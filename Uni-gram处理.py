import os
import csv
import xlwt
import  numpy as np
# 标点二元文法

# 词类二元文法（去标点）
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
    tp = open("中文停用词1.txt", 'r', encoding="utf-8")
    stoplist = tp.read()

    Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹
    print(Type_list)
    for mydir0 in Type_list:
        H =[]
        m = 1
        Partname = corpus_path + mydir0 + "/"
        f1 = open('./Uni-gram-01/' + mydir0+'/不成功单词统计.csv', 'a+',newline="")
        writer1 = csv.writer(f1)
        writer1.writerow(["单词", "出现次数"])
        file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹


        for mydir in file_list:
            # f2 = open('./TTR/' + mydir0+"/"+ mydir[:-7]+ '类符统计.csv', 'a+')
            # writer2 = csv.writer(f2)
            # writer2.writerow(["词性", '次数'])
            pos_2n = []  # 所有词性组合
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
                            if  word[:word.find("/")] not in stoplist:#拟声词
                                x_q = word [:word.find("/")]
                                pos_2n.append(x_q)
                # print(pos_2n)
            t=all_np(pos_2n)
            z= sorted(t.items(), key=lambda x: x[1], reverse=True)
            print([mydir[:-7], z[:50]])
            if z.__len__()>=50:
                H.append({z[0][0]:  z[0][1],  z[1][0]:  z[1][1], z[2][0]:  z[2][1], z[3][0]:  z[3][1],z[4][0]:z[4][1],
                          z[5][0]:  z[5][1],  z[6][0]:  z[6][1], z[7][0]:  z[7][1], z[8][0]:  z[8][1],z[9][0]:z[9][1],
                          z[10][0]: z[10][1], z[11][0]: z[11][1],z[12][0]: z[12][1],z[13][0]: z[13][1], z[14][0]: z[14][1],
                          z[20][0]: z[20][1], z[21][0]: z[21][1],z[22][0]: z[22][1],z[23][0]: z[23][1], z[24][0]: z[24][1],
                          z[25][0]: z[25][1], z[26][0]: z[26][1],z[27][0]: z[27][1],z[28][0]: z[28][1], z[29][0]: z[29][1],
                          z[30][0]: z[30][1], z[31][0]: z[31][1],z[32][0]: z[32][1],z[33][0]: z[33][1], z[34][0]: z[34][1],
                          z[35][0]: z[35][1], z[36][0]: z[36][1],z[37][0]: z[37][1],z[38][0]: z[38][1], z[39][0]: z[39][1],
                          z[40][0]: z[40][1], z[41][0]: z[41][1],z[42][0]: z[42][1],z[43][0]: z[43][1], z[44][0]: z[44][1],
                          z[45][0]: z[45][1], z[46][0]: z[46][1],z[47][0]: z[47][1],z[48][0]: z[48][1], z[49][0]: z[49][1],
                          z[50][0]: z[50][1], z[51][0]: z[51][1], z[52][0]: z[52][1], z[53][0]: z[53][1], z[54][0]: z[54][1],
                          z[55][0]: z[55][1], z[56][0]: z[56][1], z[57][0]: z[57][1], z[58][0]: z[58][1], z[59][0]: z[59][1],
                          z[60][0]: z[60][1], z[61][0]: z[61][1], z[62][0]: z[62][1], z[63][0]: z[63][1], z[64][0]: z[64][1],
                          z[65][0]: z[65][1], z[66][0]: z[66][1], z[67][0]: z[67][1], z[68][0]: z[68][1], z[69][0]: z[69][1],
                          z[70][0]: z[70][1], z[71][0]: z[71][1], z[72][0]: z[72][1], z[73][0]: z[73][1], z[74][0]: z[74][1],
                          z[75][0]: z[75][1], z[76][0]: z[76][1], z[77][0]: z[77][1], z[78][0]: z[78][1], z[79][0]: z[79][1],
                          z[80][0]: z[80][1], z[81][0]: z[81][1], z[82][0]: z[82][1], z[83][0]: z[83][1], z[84][0]: z[84][1],
                          z[85][0]: z[85][1], z[86][0]: z[86][1], z[87][0]: z[87][1], z[88][0]: z[88][1], z[89][0]: z[89][1],
                          z[90][0]: z[90][1], z[91][0]: z[91][1], z[92][0]: z[92][1], z[93][0]: z[93][1], z[94][0]: z[94][1],
                          z[95][0]: z[95][1], z[96][0]: z[96][1], z[97][0]: z[97][1], z[98][0]: z[98][1], z[99][0]: z[99][1],
                          z[100][0]: z[100][1], z[101][0]: z[101][1], z[102][0]: z[102][1], z[103][0]: z[103][1], z[104][0]: z[104][1],
                          z[105][0]: z[105][1], z[106][0]: z[106][1], z[107][0]: z[107][1], z[108][0]: z[108][1], z[109][0]: z[109][1],
                          z[110][0]: z[110][1], z[111][0]: z[111][1], z[112][0]: z[112][1], z[113][0]: z[113][1], z[114][0]: z[114][1],
                          z[115][0]: z[115][1], z[116][0]: z[116][1], z[117][0]: z[117][1], z[118][0]: z[118][1], z[119][0]: z[119][1],
                          z[120][0]: z[120][1], z[121][0]: z[121][1], z[122][0]: z[122][1], z[123][0]: z[123][1], z[124][0]: z[124][1],
                          z[125][0]: z[125][1], z[126][0]: z[126][1], z[127][0]: z[127][1], z[128][0]: z[128][1], z[129][0]: z[129][1],
                          z[130][0]: z[130][1], z[131][0]: z[131][1], z[132][0]: z[132][1], z[133][0]: z[133][1], z[134][0]: z[134][1],
                          z[135][0]: z[135][1], z[136][0]: z[136][1], z[137][0]: z[137][1], z[138][0]: z[138][1], z[139][0]: z[139][1],
                          z[140][0]: z[140][1], z[141][0]: z[141][1], z[142][0]: z[142][1], z[143][0]: z[143][1], z[144][0]: z[144][1],
                          z[145][0]: z[145][1], z[146][0]: z[146][1], z[147][0]: z[147][1], z[148][0]: z[148][1], z[149][0]: z[149][1],
                          z[150][0]: z[150][1], z[151][0]: z[151][1], z[152][0]: z[152][1], z[153][0]: z[153][1], z[154][0]: z[154][1],
                          z[155][0]: z[155][1], z[156][0]: z[156][1], z[157][0]: z[157][1], z[158][0]: z[158][1], z[159][0]: z[159][1],
                        })
        lst = H[0]
        for i in range(1,H.__len__()):
            lst=Dic_combine(lst,H[i])
        l_dic = sorted(lst.items(), key=lambda x: x[1], reverse=True)
        try:
            for i in range(l_dic.__len__()):
                print([l_dic[i][0], l_dic[i][1]])
                writer1.writerow([l_dic[i][0], l_dic[i][1]])
            f1.close()
        except Exception as err:
            print(err)
    tp.close()

if __name__ == "__main__":
    # z = duqu("./虚词-01")
    corpus_segment2("./NLP_Pos/不成功词与词性/")