# -*- coding: UTF-8-*-
import  jieba
import  jieba.posseg
import  os
from stanfordcorenlp import StanfordCoreNLP
from   nltk.tree import Tree
import re
import numpy as np
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
# conn = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='lzjwang',
#     db='qidian1',
#     charset='utf8'
# )
# cur = conn.cursor()
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
def Pcfg(k):
    t = ""
    L = []
    for i in k :
        if " " not in i:
            if "/n" not in i:
                if i=="(":
                    if t=="":
                        # print(i+"/")
                        L.append(i)
                    else:
                        # print(t+"/")
                        L.append(t)
                        t=""
                        # print(i+"/")
                        L.append(i)
                    continue
                elif (i >= u'\u0041' and i<=u'\u005a') or (i >= u'\u0061' and i<=u'\u007a'):#p判断是否是英文字母
                    t=t+i
                    continue
                elif '\u4e00' <= i <= '\u9fff':#判断中文
                    t = t + i
                    continue

                elif i==")":
                    if t=="":
                        # print(i+"/")
                        L.append(i)
                    else:
                        # print(t+"/")
                        L.append(t)
                        t=""
                        # print(i+"/")
                        L.append(i)
                    continue
                elif i=="\r"or i=="\n":
                    continue
                else:
                    t = t + i
                    continue

    return L
def process(P_list):
    a = []  # 括号栈
    b = []  # 短语栈
    word = ""  # 从短语栈中曲出的短语结构存放
    rule = []  # 存储规则
    W_rule = []  # 存储未满规则
    W_ruleI = []  # 规则节点前1位，
    W_ruleII = []  # 规则节点前2位，
    z = ""  # 临时规则存放
    for char in P_list:
        if char == "(":
            a.append(char)
            if z != '':
                W_rule.append(z)
                if b.__len__() > 1:
                    W_ruleI.append(b[-2])
                else:
                    W_ruleI.append("0")
                if b.__len__() < 3:
                    W_ruleII.append("0")
                else:
                    W_ruleII.append(b[-3])
                z = ""

            continue

        elif char == ")":
            word = b.pop()
            if len(a) > 0:
                a.pop()

            if ('\u4e00' <= word[-1] <= '\u9fff'):  # 判断中文
                rule.append(word)
                lenth = len(b[-1])
                if len(b) < 3:
                    b.insert(0, "0")
                if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                    #                     print(W_rule[-1][0:lenth])#核实是否有规则未满
                    if b[-1] == W_rule[-1][0:lenth] and b[-2] == W_ruleI[-1] and b[-3] == W_ruleII[
                        -1]:  # 判断其父节点是否和未满规则一致
                        ru = W_rule.pop()
                        W_ruleI.pop()
                        W_ruleII.pop()
                        z = ru + " " + ''.join(re.findall(r'[A-Za-z]', word))
                    else:
                        z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
                else:
                    z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
            elif (word[-1] >= u'\u0041' and word[-1] <= u'\u005a') or (word[-1] >= u'\u0061' and word[-1] <= u'\u007a'):
                rule.append(z)
                z = ""
                if len(b) < 1:
                    lenth = 0
                else:
                    lenth = len(b[-1])
                if b.__len__() < 1:
                    z = "0"

                else:
                    if len(b) < 2:
                        b.insert(0, "0")
                    if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                        #                         print(W_rule[-1][0:lenth])  # 核实是否有规则未满
                        if b[-1] == W_rule[-1][0:lenth] and b[-2] == W_ruleI[-1]:  # 判断其父节点是否和未满规则一致
                            ru = W_rule.pop()
                            W_ruleI.pop()
                            # W_ruleII.pop()
                            z = ru + " " + ''.join(re.findall(r'[A-Za-z]', word))
                        else:
                            z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
                    else:
                        z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
            else:
                rule.append(word)
                lenth = len(b[-1])
                if len(b) < 2:
                    b.insert(0, "0")
                if W_rule.__len__() != 0:  # 判断是否需要将该节点加入之前为满规则 如  (ip（np(np你好)(np啊)))  需要将啊之前的np .加入到np->np之中
                    #                     print(W_rule[-1][0:lenth])  # 核实是否有规则未满
                    if b[-1] == W_rule[-1][0:lenth] and b[-2] == W_ruleI[-1]:  # 判断其父节点是否和未满规则一致
                        ru = W_rule.pop()
                        W_ruleI.pop()

                        z = ru + " " + ''.join(re.findall(r'[A-Za-z]', word))
                    else:
                        z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))
                else:
                    z = b[-1] + " " + ''.join(re.findall(r'[A-Za-z]', word))

        else:
            b.append(char)

    return rule
def sentence_splitter(sentences):
    sents = SentenceSplitter.split(sentences)  # 分句
    # print('\n'.join(sents))
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

#句法结构分析
    # nlp = StanfordCoreNLP(r'D:\myprojects\stanford_nlp', lang='zh')
    # # cont="月如银盘，漫天繁星。山崖之颠，萧炎斜躺在草地之上，嘴中叼中一根青草，微微嚼动，任由那淡淡的苦涩在嘴中弥漫开来…举起有些白皙的手掌，挡在眼前，目光透过手指缝隙，遥望着天空上那轮巨大的银月。“唉…”想起下午的测试，萧炎轻叹了一口气，懒懒的抽回手掌，双手枕着脑袋，眼神有些恍惚…“十五年了呢…”低低的自喃声，忽然毫无边际的从少年嘴中轻吐了出来。在萧炎的心中，有一个仅有他自己知道的秘密：他并不是这个世界的人，或者说，萧炎的灵魂，并不属于这个世界，他来自一个名叫地球的蔚蓝星球，至于为什么会来到这里，这种离奇经过，他也无法解释，不过在生活了一段时间之后，他还是后知后觉的明白了过来：他穿越了！随着年龄的增长，对这块大陆，萧炎也是有了些模糊的了解…大陆名为斗气大陆，大陆上并没有小说中常见的各系魔法，而斗气，才是大陆的唯一主调！在这片大陆上，斗气的修炼，几乎已经在无数代人的努力之下，发展到了巅峰地步，而且由于斗气的不断繁衍，最后甚至扩散到了民间之中，这也导致，斗气，与人类的日常生活，变得息息相关，如此，斗气在大陆中的重要性，更是变得无可替代！因为斗气的极端繁衍，同时也导致从这条主线中分化出了无数条斗气修炼之法，所谓手有长短，分化出来的斗气修炼之法，自然也是有强有弱。经过归纳统计，斗气大陆将斗气功法的等级，由高到低分为四阶十二级：天.地.玄.黄！而每一阶，又分初，中，高三级！修炼的斗气功法等级的高低，也是决定日后成就高低的关键，比如修炼玄阶中级功法的人，自然要比修炼黄阶高级功法的同等级的人要强上几分。斗气大陆，分辩强弱，取决于三种条件。首先，最重要的，当然是自身的实力，如果本身实力只有一星斗者级别，那就算你修炼的是天阶高级的稀世功法，那也难以战胜一名修炼黄阶功法的斗师。其次，便是功法！同等级的强者，如果你的功法等级较之对方要高级许多，那么在比试之时，种种优势，一触既知。最后一种，名叫斗技！顾名思义，这是一种发挥斗气的特殊技能，斗技在大陆之上，也有着等级之分，总的说来，同样也是分为天地玄黄四级。斗气大陆斗技数不胜数，不过一般流传出来的大众斗技，大多都只是黄级左右，想要获得更高深的斗技，便必须加入宗派，或者大陆上的斗气学院。当然，一些依靠奇遇所得到前人遗留而下的功法，或者有着自己相配套的斗技，这种由功法衍变而出的斗技，互相配合起来，威力要更强上一些。依靠这三种条件，方才能判出究竟孰强孰弱，总的说来，如果能够拥有等级偏高的斗气功法，日后的好处，不言而喻…不过高级斗气修炼功法常人很难得到，流传在普通阶层的功法，顶多只是黄阶功法，一些比较强大的家族或者中小宗派，应该有玄阶的修炼之法，比如萧炎所在的家族，最为顶层的功法，便是只有族长才有资格修炼的：狂狮怒罡，这是一种风属性，并且是玄阶中级的斗气功法。玄阶之上，便是地阶了，不过这种高深功法，或许便只有那些超然势力与大帝国，方才可能拥有…至于天阶…已经几百年未曾出现了。从理论上来说，常人想要获得高级功法，基本上是难如登天，然而事无绝对，斗气大陆地域辽阔，万族林立，大陆之北，有号称力大无穷，可与兽魂合体的蛮族，大陆之南，也有各种智商奇高的高级魔兽家族，更有那以诡异阴狠而著名的黑暗种族等等…由于地域的辽阔，也有很多不为人知的无名隐士，在生命走到尽头之后，性子孤僻的他们，或许会将平生所创功法隐于某处，等待有缘人取之，在斗气大陆上，流传一句话：如果某日，你摔落悬崖，掉落山洞，不要惊慌，往前走两步，或许，你，将成为强者！此话，并不属假，大陆近千年历史中，并不泛这种依靠奇遇而成为强者的故事.这个故事所造成的后果，便是造就了大批每天等在悬崖边，准备跳崖得绝世功法的怀梦之人，当然了，这些人大多都是以断胳膊断腿归来…总之，这是一片充满奇迹，以及创造奇迹的大陆！当然，想要修炼斗气秘籍，至少需要成为一名真正的斗者之后，方才够资格，而现在的萧炎隔那段距离，似乎还很是遥远…“呸。”吐出嘴中的草根，萧炎忽然跳起身来，脸庞狰狞，对着夜空失态的咆哮道：“把劳资穿过来当废物玩吗？草！”在前世，萧炎只是庸碌众生中极其平凡的一员，金钱，美人，这些东西与他根本就是两条平行线，永远没有交叉点，然而，当来到这片斗气大陆之后，萧炎却是惊喜的发现，因为两世的经验，他的灵魂，竟然比常人要强上许多！要知道，在斗气大陆，灵魂是天生的，或许它能随着年龄的增长而稍稍变强，可却从没有什么功法能够单独修炼灵魂，就算是天阶功法，也不可能！这是斗气大陆的常识。灵魂的强化，也造就出萧炎的修炼天赋，同样，也造就了他的天才之名。当一个平凡庸碌之人，在知道他有成为无数人瞩目的本钱之后，若是没有足够的定力，很难能够把握本心，很显然的，前世仅仅是普通人的萧炎，并没有这种超人般的定力，所以，在他开始修炼斗之气后，他选择了成为受人瞩目的天才之路，而并非是在安静中逐渐成长！若是没有意外发生的话，萧炎或许还真能够顶着天才的名头越长越大，不过，很可惜，在十一岁那年，天才之名，逐渐被突如其来的变故剥夺而去，而天才，也是在一夜间，沦落成了路人口中嘲笑的废物！……在咆哮了几嗓子之后，萧炎的情绪也是缓缓的平息了下来，脸庞再次回复了平日的落寞，事与至此，不管他如何暴怒，也是挽不回辛苦修炼而来的斗之气旋。苦涩的摇了摇头，萧炎心中其实有些委屈，毕竟他对自己身体究竟发生了什么事，也是一概不知，平日检查，却没有发现丝毫不对劲的地方，灵魂，随着年龄的增加，也是越来越强大，而且吸收斗之气的速度，比几年前最巅峰的状态还要强盛上几分，这种种条件，都说明自己的天赋从不曾减弱，可那些进入体内的斗之气，却都是无一例外的消失得干干净净，诡异的情形，让得萧炎黯然神伤…黯然的叹了口气，萧炎抬起手掌，手指上有一颗黑色戒指，戒指很是古朴，不知是何材料所铸，其上还绘有些模糊的纹路，这是母亲临死前送给他的唯一礼物，从四岁开始，他已经佩戴了十年，母亲的遗物，让得萧炎对它也是有着一份眷恋，手指轻轻的抚摸着戒指，萧炎苦笑道：“这几年，还真是辜负母亲的期望了…”深深的吐了一口气，萧炎忽然回转过头，对着漆黑的树林温暖的笑道：“父亲，您来了？”虽然斗之气只有三段，不过萧炎的灵魂感知，却是比一名五星斗者都要敏锐许多，在先前说起母亲的时候，他便察觉到了树林中的一丝动静。“呵呵，炎儿，这么晚了，怎么还待在这上面呢？”树林中，在静了片刻后，传出男子的关切笑声。树枝一阵摇摆，一位中年人跃了出来，脸庞上带着笑意，凝视着自己那站在月光下的儿子。中年人身着华贵的灰色衣衫，龙行虎步间颇有几分威严，脸上一对粗眉更是为其添了几分豪气，他便是萧家现任族长，同时也是萧炎的父亲，五星大斗师，萧战！“父亲，您不也还没休息么？”望着中年男子，萧炎脸庞上的笑容更浓了一分，虽然自己有着前世的记忆，不过自出生以来，面前这位父亲便是对自己百般宠爱，在自己落魄之后，宠爱不减反增，如此行径，却是让得萧炎甘心叫他一声父亲。“炎儿，还在想下午测验的事呢？”大步上前，萧战笑道。“呵呵，有什么好想的，意料之中而已。”萧炎少年老成的摇了摇头，笑容却是有些勉强。“唉…”望着萧炎那依旧有些稚嫩的清秀脸庞，萧战叹了一口气，沉默了片刻，忽然道：“炎儿，你十五岁了吧？”“嗯，父亲。”“再有一年，似乎…就该进行成年仪式了…”萧战苦笑道。“是的，父亲，还有一年！”手掌微微一紧，萧炎平静的回道，成年仪式代表什么，他自然非常清楚，只要度过了成年仪式，那么没有修炼潜力的他，便将会被取消进入斗气阁寻找斗气功法的资格，从而被分配到家族的各处产业之中，为家族打理一些普通事物，这是家族的族规，就算他的父亲是族长，那也不可能改变！毕竟，若是在二十五岁之前没有成为一名斗者，那将不会被家族所认可！“对不起了，炎儿，如果在一年后你的斗之气达不到七段，那么父亲也只得忍痛把你分配到家族的产业中去，毕竟，这个家族，还并不是父亲一人说了算，那几个老家伙，可随时等着父亲犯错呢…”望着平静的萧炎，萧战有些歉疚的叹道。“父亲，我会努力的，一年后，我一定会到达七段斗之气的！”萧炎微笑着安慰道。“一年，四段？呵呵，如果是以前，或许还有可能吧，不过现在…基本没半点机会…”虽然口中在安慰着父亲，不过萧炎心中却是自嘲的苦笑了起来。同样非常清楚萧炎底细的萧战，也只得叹息着应了一声，他知道一年修炼四段斗之气有多困难，轻拍了拍他的脑袋，忽然笑道：“不早了，回去休息吧，明天，家族中有贵客，你可别失了礼。”“贵客？谁啊？”萧炎好奇的问道。“明天就知道了.”对着萧炎挤了挤眼睛，萧战大笑而去，留下无奈的萧炎。“放心吧，父亲，我会尽力的！”抚摸着手指上的古朴戒指，萧炎抬头喃喃道。在萧炎抬头的那一刹，手指中的黑色古戒，却是忽然亮起了一抹极其微弱的诡异毫光，毫光眨眼便逝，没有引起任何人的察觉…"
    # cont="“轰隆隆”半空中传来轰鸣，但无人发现有任何闪电的痕迹，洁白的云朵更是透着诡异，其中无数条雷龙翻涌构成一张巨大的雷网。一座包围在山岭中的楼阁也在颤动呼应，山顶的女子双手一顿，如星辰耀眼的眸子也在片刻间涌动复杂的情绪。“你终究还是来了吗……”——————“大哥，这也太诡异了吧，怎么这几天都是这样的天气，怎么会突然青天白日打雷呢？”几个少年带着工具，走在山岭上。“想这么多干嘛，这样的异像，自然是由窥星阁处理，我们这些平头百姓可是管不到的，早点办完事回纪城吧。”“嗯？”老二突然拉了拉老大的手，老大疑惑的回头，就发现有一容貌俊秀的少年躺在路面上。老大心中暗道不好，走了几步上前查看后，顿时松了一口气，“这少年还好没有什么大碍，今天这天气还是这么奇怪，也就我们兄弟三人还逗留在山上，想来这少年郎是出自富贵人家，要是遇难而死，那可不得了。”怎么回事？少年手指微微颤动，奇怪，我不是死了吗？为什么还会有意识？难道我没死？呵，有意识又怎样？想到我这一生，就是个无从说起的悲剧吧。墨渊心中充满悲愤，但也没有办法，只能无奈叹息，自从自己向天许愿，希望永远是少年时，一切就没了回头路。想到自己因为这个愿望，让父母惧怕，认为自己是个怪物。妻子远离，孩子憎恨，让自己被孤立。即使想要终结生命，都会发生各种意外，被命运玩弄于股掌。明明想要挣脱，却一点办法都没有，也许自己就是命该如此吧。墨渊攥紧手掌，想着自己的过去，那悲惨的一生真是让他受尽苦楚。他沉浸于悲痛，以至于毫无防范的让一股庞大的记忆在一瞬间涌入脑海。原来他是碰到穿越异世的潮流了。这片大陆名唤凌源，乃是诸天所辖的小世界。诸天全界人才济济，在上万年的发展中，创立了三大修炼体系，即智谋，武略，天机！且各有一宗门传承。主智谋的谋殿，主武略的四象宫，主天机的窥星阁。三大宗门凌驾于皇权之上，除总部外，更是各开设八大副宗统领诸天。原主这具身体也叫墨渊，是四象宫青龙圣子，年仅14就被四象宫钦定下任宫主之选。而这次原主的到来，就是应宫主之命，与七星阁来东副宫查看这次天生异象的详情。为的就是防范这是邪道之尊——邪阁出世的征兆。毕竟每次邪阁出世，都至少屠城上千，伤人数亿。可没想到，刚出传送阵，就被自己的下属偷袭，废了丹田，散尽武功，从此无法修行。然后动用挪移符，将自己扔到此处。更没想到的是因为挪移符的失误，原主直接从高空落下，加速了心脉衰竭，直接身死道消，以至于被墨渊占了身体。墨渊迅速查看完原主记忆不禁感叹，人生就是这么起伏，也许没人想到，前一秒高高在上的圣子，下一秒就是一个废人。可是墨渊能明显感受到自己丹田处传来的热气，这是怎么回事？不是丹田尽废吗？墨渊心中充满疑惑，闭上双眼，仔细感受丹田，发觉其中似乎出现莫名力量滋润，这股力量与雷云之中分毫不差。难道我遇到了传说中的破而后立？相传，上古时代，天地灵气充足，原本世界人人从武，虽有废人，但可借助灵气冲刷，破而后立。之后世界，因邪阁势力大盛，天地震怒，锁封灵气于万物之中，灵力匮乏，破而后立几乎变为传说。然诸天之上大能之辈并未退缩，用数百载光阴创出智谋修炼，，后因有人成功窥探天机，所以出现天机修习。可让人没想到的是，这具身体竟然借助雷云聚集的能量，成功破而后立。让武道之路不至于就此中断。墨渊心中十分复杂，重生这种事情竟然会被我遇到，难道是老天爷还不能放过我吗？既然老天爷上辈子让我永为少年，造成无尽悲痛，那此次重生，我会为原主墨渊而活，为自己而活，以修炼为基，逃脱命运掌握，登临诸天巅峰。让自己不至于………“哎，公子你醒了。”老大看到墨渊握紧的双手，知道他已经清醒过来，连忙招呼兄弟们将他扶起，“公子叫什么名字？家住在凌源何处？”老大平视着墨渊，慢慢问道。墨渊看着老大，仔细考虑自己的一切，发现，即使现在回到四象宫，以如今的实力也一定会被剥夺圣子之位，且不知是谁要废他武功，势力大到即使在窥星阁面前伤人也可肆无忌惮，不得不防。敌暗我明，还是不要回去的好。还是留在东副宫好好修炼圣子的《青龙决》，等到时机成熟再离开。看这三兄弟倒也朴实，想来可以尝试向他们借住。墨渊抬起头默默摇了摇头，“我叫墨渊，我不是凌源大陆的人，我是外出游玩时突然晕倒在地上，但醒来时却出现在这里，我现在也无处可去了。”老大看着墨渊，盯了好一会，然后恍然大悟，“看来是雷云造成的原因。”“关雷云什么事？”“哦，忘了你不是这儿的人，那实际上是一种奇怪现象。每当雷云响起，总会造成一些无法理解的现象，听老一辈人说，雷云是有可颠覆世界的绝世人物出世所降下的天地异象。”墨渊虽然有覆天之心，但可不认为自己有这番能力让天降异象。毕竟自己前世只是个普通的人。“想来是这世道要乱了吧。”老二这是拿着柴刀走过来，蹲下身来说到，“既然公子无处可去，且身受重伤，就去我们家所在的纪城吧。”墨渊原本只是想借宿而已，因此答应了，可墨渊与他们进入纪城后，却被他们的盛情款待弄的手忙脚乱。怎么也没想到，这三兄弟居然太过于热情，墨渊只好不断拒绝，毕竟自己只是寻个住处而已，不想欠人情。但三兄弟却不干了，老三还不断嘀咕着:“好不容易有朋友了，他为什么拒绝呢？”之类的话语。墨渊一下子顿住了，他放下了手，看着热火朝天为他收拾的兄弟三人，无奈的笑了，“也许，这样也不错。至少安定下来了。”"
    # sens=sentence_splitter(cont)
    # sens=sens.split("\n")
    # f1 = open('实验.txt', 'a+')
    # z=[]
    # for sentence in sens:
    #     print(sentence)
    #     k = nlp.parse(sentence)
    #     # print('Named Entities:', k)
    #     f = Pcfg(k)
    #     # print(f)
    #     l=process(f)
    #     z.append(l)
    #     print(l)
    # nlp.close()
    # Eword_list = []
    # Cword_list = []
    # TypeEword_list = []
    # TypeCword_list = []
    # sum1=0
    # sum2 = 0
    # for senz in z:
    #     for word1 in senz:
    #
    #         if len(word1) < 1:
    #             continue;
    #         if (word1[-1] >= u'\u0041' and word1[-1] <= u'\u005a') or (
    #                         word1[-1] >= u'\u0061' and word1[-1] <= u'\u007a'):
    #             Eword_list.append(word1)
    #             sum1 = sum1 + 1
    #             TypeEword_list.append(word1)
    #         else:
    #             Cword_list.append(word1)
    #             sum2 = sum2 + 1
    #             TypeCword_list.append(word1)
    #
    # rule_list2 = all_np(Eword_list)
    # rule_list2 = sorted(rule_list2.items(), key=lambda item: item[1], reverse=True)
    # rule_list3 = all_np(Cword_list)
    # rule_list3 = sorted(rule_list3.items(), key=lambda item: item[1], reverse=True)
    # print(rule_list2)
    # print(rule_list3)
    # print(sum1)
    # print(rule_list2.__len__())
    # for i in range(rule_list2.__len__()):
    #     f1.write(str(rule_list2[i][0])+","+ str(rule_list2[i][1])+","+ str(round(float(rule_list2[i][1])/float(sum1),6))+"\n")
    # for i in range(rule_list3.__len__()):
    #     f1.write(str(rule_list3[i][0])+","+ str(rule_list3[i][1])+","+str(round(float(rule_list3[i][1])/float(sum2),6))+"\n")
#词性分析
    # sens=sentence_splitter(cont)
    # sens=sens.split("/n")
    # T=[]
    # T1=[]
    # words=[]
    # juzi = 0
    # Gantanci = 0
    # adj = 0
    # adv = 0
    # Numb = 0
    # V = 0
    # N = 0
    # nd = 0  # 方位名词
    # nt = 0  # s时间名词
    # P = 0  # 介词
    # r = 0  # 代词
    # wp = 0  # 标点
    # nh = 0  # 人名
    # u = 0  # 助词
    # i = 0  # 成语14
    # for cont in sens:
    #     print(cont)
    #     word1 = segmentor(cont)
    #     print(word1)
    #     pos = posttagger(word1)
    #     print(pos)
    #
    # for word, tag in zip(word1, pos):
    #     print(word + "/" + tag + "   ")
    #     words.append(word + "/" + tag)
    # sum1=0
    # for word in words:
    #     sum1=sum1+1
    #     if "wp"  in word:
    #         if "！"  in word:
    #             juzi=juzi+1
    #         if "？"  in word :
    #             juzi = juzi + 1
    #         if "。"  in word :
    #             juzi = juzi + 1
    #         wp=wp+1
    #     if "r" in word :
    #         r=r+1
    #     if "v" in word:
    #         V = V + 1
    #     if "a" in word:
    #         adj = adj + 1
    #     if "i" in word:
    #         i = i + 1
    #     if "d" in word:
    #         adv = adv + 1
    #     if "m" in word:
    #         Numb = Numb + 1
    #     if "nd" in word:
    #         nd = nd + 1
    #     if "e" in word:
    #         Gantanci = Gantanci + 1
    #     if "p" in word:
    #         P = P + 1
    #     if "nt" in word:
    #         nt = nt + 1
    #     if "u" in word:
    #         u = u + 1
    #     if "n" in word:
    #         N = N + 1
    #     if "nh" in word:
    #         nh = nh + 1
    # T.append([{"r":r,"v":V,"nh":nh,"n":N,"u":u,"nt":nt,"p":P,"e":Gantanci,"nd":nd,"m":Numb,"d":adv,"i":i,"wp":wp,"a":adj},sum1])
    # T1.append([{"r": round(r/sum1,6), "v": round(V/sum1,6), "nh": round(nh/sum1,6), "n": round(N/sum1,6), "u": round(u/sum1,6), "nt": round(nt/sum1,6), "p": round(P/sum1,6), "e": round(Gantanci/sum1,6), "nd": round(nd/sum1,6), "m": round(Numb/sum1,6), "d": round(adv/sum1,6),"i": round(i/sum1,6), "wp": round(wp/sum1,6), "a": round(adj/sum1,6)}, sum1])
    # print(T)
    # print(T1)