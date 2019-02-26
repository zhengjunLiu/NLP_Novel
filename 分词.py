# import  pymysql
# import os
# LTP_DATA_DIR = 'D:\myprojects\LTP\ltp_data'  # ltp模型目录的路径
# cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
# pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
# ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
# par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
# srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl_win.model')  # 语义角色标注模型目录路径，模型目录为`srl`。注意该模型路径是一个目录，而不是一个文件。
# from pyltp import SentenceSplitter
# from pyltp import Segmentor
# from pyltp import Postagger
# from pyltp import NamedEntityRecognizer
# from pyltp import Parser
# from pyltp import SementicRoleLabeller
# conn = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='lzjwang',
#     db='novel',
#     charset='utf8'
# )
# cur = conn.cursor()
#
# def sentence_splitter(sentences):
#     sents = SentenceSplitter.split(sentences)  # 分句
#     print('\n'.join(sents))
#     return '\n'.join(sents)
#
#
# # 分词
# def segmentor(sentence):
#     segmentor = Segmentor()  # 初始化实例
#     segmentor.load(cws_model_path)  # 加载模型
#     words = segmentor.segment(sentence)  # 分词
#     # words = jieba.cut(sentence)
#     # print('\t'.join(words))
#     words_list = list(words)
#     print(words_list)
#     segmentor.release()  # 释放模型
#     # try:
#     #     for i in range(len(words_list)):
#     #         words_list.remove('\xa0\xa0')
#     #         words_list.remove('\r\r')
#     # except ValueError  as e:
#     #     print(e)
#     Kl=[]
#     for il in range(len(words_list)):
#         words_list[il]=str(words_list[il]).replace('\xa0\xa0',"lzj")
#     for ll in words_list:
#         if '\r\r' in ll:
#             words_list.remove(ll)
#     for lll in words_list:
#         if "lzj" not in lll:
#             Kl.append(lll)
#
#     print(Kl)
#     return Kl
#
# def posttagger(words):
#     postagger = Postagger()  # 初始化实例
#     postagger.load(pos_model_path)  # 加载模型
#     postags = postagger.postag(words)  # 词性标注
#     # for word, tag in zip(words, postags):
#     #     print(word + '/' + tag)
#     postagger.release()  # 释放模型
#     return postags
#
# def savefile(savepath,content):
#     with open(savepath,'a+',encoding="utf-8")as fp:
#         fp.write("   ".join(content))
#
# def savefile2(savepath, content, postg):
#     with open(savepath, 'a+', encoding="utf-8")as fp:
#         for word, tag in zip(content, postg):
#                 fp.write(word +"/"+tag+"   ")
# def pro(sent):
#     # if not os.path.exists("./NLP process/成功"):  # 判断存放目录是否存在
#     #     os.makedirs("./NLP process/成功")  # 不存在就创建
#     # if not os.path.exists("./NLP process/不成功"):  # 判断存放目录是否存在
#     #     os.makedirs("./NLP process/不成功")  # 不存在就创建
#     name=sent[0]+sent[2]
#     print(name)
#     cont=sent[3]
#     # sentens=sentence_splitter(cont)
#     word1=segmentor(cont)
#     pos=posttagger(word1)
#     print(word1)
#     # savefile("./NLP process/成功/"+name+"不去标点.txt",word1)
#     # savefile2("./NLP process/成功/" + name +"去标点.txt", word1,pos)
#
#
# if __name__ == "__main__":
#     sql_str = "select * from noveldata;"
#     cur.execute(sql_str)
#     rows = cur.fetchall()
#     i=1
#
#     word_list2=[]
#     pos2=[]
#     m=1
#     for row in rows:
#         name = row[0]
#         print(name)
#         cont = row[3]
#         # sentens=sentence_splitter(cont)
#         word1 = segmentor(cont)
#         word_list2.append(word1)
#         pos = posttagger(word1)
#         pos2.append(pos)
#         # print(word_list2)
#         # print(pos2[i-1])
#         if(i%10==0):
#             for j in range(i-9,i):
#
#                 savefile("./NLP process/成功/"+name+"前十章.txt",word_list2[j-1])
#                 savefile2("./NLP process/成功/" + name +"前十章词性.txt",word_list2[j-1],pos2[j-1])
#
#         i = i + 1
#
#     conn.commit()
#     cur.close()
#
