import os
import xlwt
import os
import csv
# import xlrd
# corpus_path="./NLP_规则/非叶子节点规则/成功/"
# Type_list = os.listdir(corpus_path)  # 返回该目录下面所有文件夹
# print(Type_list)
# for mydir0 in Type_list:
#     T_list = []
#     z_dic = {}
#     l_dic = {}
#     Partname = corpus_path + mydir0 + "/"
#     file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
#     for mydir in file_list:
#         T_key = []
#         T_value = []
#         fullname = Partname + mydir
#         print(fullname)
#         csv_reader = csv.reader(open(fullname))
#         # print(csv_reader)
#         i=0
#         for row_0 in csv_reader:
#             if i==0:
#                 continue
#
#             if len(row_0) != 0:
#                 print(row_0[0])
#                 print(row_0[1])
#             i=i+1
#         #         T_key.append(row_0[0])
#         #         T_value.append(row_0[1])

f2 = open('./规则.txt', 'a+', encoding="utf-8")
for i in range(1,601):
    f2.write("@attribute '规则"+str(i)+"' "+"numeric"+"\n")







