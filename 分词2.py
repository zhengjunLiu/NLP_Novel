import  pymysql
import  jieba
import  jieba.posseg
import  os
LTP_DATA_DIR = 'D:\myprojects\LTP\ltp_data'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl_win.model')  # 语义角色标注模型目录路径，模型目录为`srl`。注意该模型路径是一个目录，而不是一个文件。
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser
from pyltp import SementicRoleLabeller
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='lzjwang',
    db='qidian1',
    charset='utf8'
)
cur = conn.cursor()
def sentence_splitter(sentences):
    sents = SentenceSplitter.split(sentences)  # 分句
    print('\n'.join(sents))
    return '\n'.join(sents)

def segmentor(sentence):
    segmentor = Segmentor()  # 初始化实例
    segmentor.load(cws_model_path)  # 加载模型
    words = segmentor.segment(sentence)  # 分词
    # words = jieba.cut(sentence)
    # print('\t'.join(words))
    words_list = list(words)
    # print(words_list)
    segmentor.release()  # 释放模型

    return words_list

def posttagger(words):
    postagger = Postagger()  # 初始化实例
    postagger.load(pos_model_path)  # 加载模型
    postags = postagger.postag(words)  # 词性标注
    # for word, tag in zip(words, postags):
    #     print(word + '/' + tag)
    postagger.release()  # 释放模型
    return postags
def savefile(savepath,content):
    with open(savepath,'a+',encoding="utf-8")as fp:
        fp.write("   ".join(content))

def savefile2(savepath, content, postg):
    with open(savepath, 'a+', encoding="utf-8")as fp:
        for word, tag in zip(content, postg):
                fp.write(word +"/"+tag+"   ")

def savefile3(savepath, postg):
    with open(savepath, 'a+', encoding="utf-8")as fp:
        for tag in postg:
                fp.write(tag + "   ")
if __name__ == "__main__":
    # sql_str = "SELECT * from qd_links_bad,qd_books_bad  WHERE qd_books_bad.bookName=qd_links_bad.bookName;"
    sql_str = "SELECT * from qd_books_bad;"
    cur.execute(sql_str)
    rows = cur.fetchall()
    i = 1
    word_list2 = []
    pos2=[]
    m=1

    for row in rows:
        chapterid = row[3]
        if int(chapterid)<11:
            name = row[1]
            print(name+"/"+row[4])
            # cont = row[3]
            cont = "".join(str(row[5]).split())
            # sentens=sentence_splitter(cont)
            word1 = segmentor(cont)
            word_list2.append(word1)
            pos = posttagger(word1)
            pos2.append(pos)
            if(i%10==0):
                for j in range(i-9,i):
                    # print(row[3]+"/"+name)
                    # print(word_list2[j-1],"/",pos2[j - 1])
                    # savefile("./NLP_Pos/不成功词/" + name + "前十章.txt", word_list2[j - 1])
                    # savefile3("./NLP_Pos/不成功词性/" + name + "前十章.txt",pos2[j - 1])
                    if "仙侠" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/仙侠/" +name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "武侠" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/武侠/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "都市" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/都市/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "玄幻" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/玄幻/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "二次元" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/二次元/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "奇幻" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/奇幻/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "军事" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/军事/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "科幻" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/玄幻/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "历史" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/历史/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "灵异" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/灵异/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "体育" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/体育/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "现实" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/现实/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "游戏" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/游戏/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    if "短篇" in row[2]:
                        savefile2("./NLP_Pos/不成功词与词性/短篇/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                #########################################################################################################        #
                    # if "仙侠" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/仙侠/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "武侠" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/武侠/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "都市" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/都市/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "玄幻" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/玄幻/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "二次元" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/二次元/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "奇幻" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/奇幻/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "军事" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/军事/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "科幻" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/玄幻/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "历史" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/历史/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "灵异" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/灵异/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "体育" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/体育/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "现实" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/现实/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "游戏" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/游戏/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
                    # if "短篇" in row[2]:
                    #     savefile2("./NLP_Pos/成功词与词性/短篇/" + name + "前十章.txt", word_list2[j - 1], pos2[j - 1])
            i = i + 1
        m=m+1
    print(m)
    print(i)
        # words=jieba.cut(s)
        # print('\t'.join(words))
        # seg = jieba.posseg.cut(s)
        # l = []
        # for i in seg:
        #     print(i)
        #     l.append((i.word, i.flag))
        # print(l)
    conn.commit()
    cur.close()
