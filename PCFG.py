import  pymysql
# from stanfordcorenlp import StanfordCoreNLP
# from   nltk.tree import Tree
LTP_DATA_DIR = 'D:\myprojects\LTP\ltp_data'  # ltp模型目录的路径
from pyltp import SentenceSplitter
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
def savefile(savepath, content):
    with open(savepath, 'a+', encoding="utf-8")as fp:
        for word in content:
                fp.write(word)
if __name__ == '__main__':

    sql_str = "SELECT * from qd_books_bad;"
    cur.execute(sql_str)
    rows = cur.fetchall()
    i = 1
    word_list2 = []
    pos2 = []
    m = 1

    for row in rows:
        chapterid = row[3]
        if int(chapterid) < 11:
            name = row[1]
            print(name + "/" + row[4])
            # cont = row[3]
            cont = "".join(str(row[5]).split())
            # sentens=sentence_splitter(cont)
            word1 = sentence_splitter(cont)
            word_list2.append(word1)
            if (i % 10 == 0):
                for j in range(i - 9, i):
                    # print(row[3]+"/"+name)
                    # print(word_list2[j-1],"/",pos2[j - 1])
                    # savefile("./NLP_Pos/不成功词/" + name + "前十章.txt", word_list2[j - 1])
                    # savefile3("./NLP_Pos/不成功词性/" + name + "前十章.txt",pos2[j - 1])
                    if "仙侠" in row[2]:
                        savefile("./NLP_Pos/不成功句子/仙侠/" + name + "前十章.txt", word_list2[j - 1])
                    if "武侠" in row[2]:
                        savefile("./NLP_Pos/不成功句子/武侠/" + name + "前十章.txt", word_list2[j - 1])
                    if "都市" in row[2]:
                        savefile("./NLP_Pos/不成功句子/都市/" + name + "前十章.txt", word_list2[j - 1])
                    if "玄幻" in row[2]:
                        savefile("./NLP_Pos/不成功句子/玄幻/" + name + "前十章.txt", word_list2[j - 1])
                    if "二次元" in row[2]:
                        savefile("./NLP_Pos/不成功句子/二次元/" + name + "前十章.txt", word_list2[j - 1])
                    if "奇幻" in row[2]:
                        savefile("./NLP_Pos/不成功句子/奇幻/" + name + "前十章.txt", word_list2[j - 1])
                    if "军事" in row[2]:
                        savefile("./NLP_Pos/不成功句子/军事/" + name + "前十章.txt", word_list2[j - 1])
                    if "科幻" in row[2]:
                        savefile("./NLP_Pos/不成功句子/玄幻/" + name + "前十章.txt", word_list2[j - 1])
                    if "历史" in row[2]:
                        savefile("./NLP_Pos/不成功句子/历史/" + name + "前十章.txt", word_list2[j - 1])
                    if "灵异" in row[2]:
                        savefile("./NLP_Pos/不成功句子/灵异/" + name + "前十章.txt", word_list2[j - 1])
                    if "体育" in row[2]:
                        savefile("./NLP_Pos/不成功句子/体育/" + name + "前十章.txt", word_list2[j - 1])
                    if "现实" in row[2]:
                        savefile("./NLP_Pos/不成功句子/现实/" + name + "前十章.txt", word_list2[j - 1])
                    if "游戏" in row[2]:
                        savefile("./NLP_Pos/不成功句子/游戏/" + name + "前十章.txt", word_list2[j - 1])
                    if "短篇" in row[2]:
                        savefile("./NLP_Pos/不成功句子/短篇/" + name + "前十章.txt", word_list2[j - 1])
            i = i + 1
        m = m + 1
    # with StanfordCoreNLP(r'D:\myprojects\stanford_nlp',lang='zh') as nlp:
    #     sentence = '清华大学位于北京。'
        # print( 'Tokenize:', nlp.word_tokenize(sentence))
        # print ('Part of Speech:', nlp.pos_tag(sentence))
        # print ('Named Entities:', nlp.ner(sentence))
        # t=nlp.parse(sentence)
        # print('Named Entities:', t)
        #
        # tree=Tree.fromstring(t)
        # tree.draw()
        # print ('Dependency Parsing:', nlp.dependency_parse(sentence))