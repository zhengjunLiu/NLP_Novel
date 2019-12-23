# import os
# import csv
# import xlwt
# import  numpy as np
# # 小说字符数统计
# f=open('./小说字符统计//成功小说字符统计.csv','a+')
# writer=csv.writer(f)
# writer.writerow(["小说名","字符数","词数"])
# def corpus_segment(corpus_path):
#     file_list=os.listdir(corpus_path)#返回该目录下面所有文件夹
#     print(file_list)
#     for mydir in file_list:
#         print(mydir[:-7])
#         fullname=corpus_path+mydir
#         with open(fullname, 'r', encoding="utf-8")as fp:
#             content=fp.read()  # 读取文件内容
#             word1=[]#不去标点符号
#             word2=[]#去标点符号
#             words=content.split(" ")
#             for word in words:
#                 if word!="":
#                     word1.append(word)
#                     if "/wp" not in word:
#                         word2.append(word)
#             print(word1.__len__())
#             print(word2.__len__())
#             writer.writerow([mydir[:-7],word1.__len__(),word2.__len__()])
# 句子破碎度

# def corpus_segment(corpus_path):
#     Type_list=os.listdir(corpus_path)#返回该目录下面所有文件夹
#     print(Type_list)
#     for mydir in Type_list:
#         Partname=corpus_path+mydir+"/"
#         f = open('./句子破碎度统计/'+mydir+'/成功小说句子破碎度统计.csv', 'a+')
#         writer = csv.writer(f)
#         writer.writerow(["小说名", "句子数", "停顿数"])
#         file_list = os.listdir(Partname)  # 返回该目录下面所有文件夹
#         for mydir in file_list:
#             print(mydir[:-7])
#             fullname=Partname+mydir
#             with open(fullname, 'r', encoding="utf-8")as fp:
#                 content=fp.read()  # 读取文件内容
#                 word3=[]#标点符号集合
#                 word4=[]#句末点号
#                 words=content.split(" ")
#                 for word in words:
#                     if "wp" in word:
#                         if "，" in word:
#                             word3.append(word)
#                         if "："  in word:
#                             word3.append(word)
#                         if "、"  in word :
#                             word3.append(word)
#                         if "；"  in word:
#                             word3.append(word)
#                         if "！"  in word:
#                             word4.append(word)
#                             word3.append(word)
#                         if "？"  in word :
#                             word4.append(word)
#                             word3.append(word)
#                         if "。"  in word :
#                             word4.append(word)
#                             word3.append(word)
#                 writer.writerow([mydir[:-7],word4.__len__(),word3.__len__()])
#         f.close()
# if __name__ == "__main__":
#     corpus_segment("./NLP_Pos/成功词与词性/")
