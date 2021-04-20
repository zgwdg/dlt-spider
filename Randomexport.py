# coding=utf-8
import random

# 复式配置
red = 7
bule = 4

# 打印几注
Vcount = 5

# 1 dlt  2 ssq
goType = 1

def getResult(redBoll,blueBoll):
    redb = [x for x in range(redBoll)]
    redb.pop(0)
    blub = [x for x in range(blueBoll)]
    blub.pop(0)
    for i in range(Vcount):
        rred = random.sample(redb, red)
        rred.sort()
        rblue = random.sample(blub, bule)
        rblue.sort()
        print("第{}注为：".format(i+1) + str(rred).split(']')[0].split('[')[1] +"  +  "+ str(rblue).split('[')[1].split(']')[0])

def getPrice(red,bule):
    if goType == 1:
        k = 5
        t = 2
        (red - k)
    elif goType == 2:
        k = 6
        t = 1
        pass
    else:
        print("Type Error!")
    p = [x for x in range(red + 1)]
    p.pop(0)
    p.sort()
    ok = 1
    for i in p[red - k:]:
        ok *= i
    om = 1
    for j in p[:k]:
        om *= j
    redc = int(ok / om)
    q = [y for y in range(bule + 1)]
    q.pop(0)
    q.sort()
    ot = 1
    for e in q[bule - t:]:
        ot *= e
    ov = 1
    for w in q[:t]:
        ov *= w
    bluec = int(ot / ov)
    return redc * bluec,redc * bluec * 2


if goType == 1:
    redBoll = 36
    blueBoll = 13
    print('大乐透分析预测结果（{}+{}）'.format(red,bule))
    getResult(redBoll,blueBoll)

elif goType == 2:
    redBoll = 33
    blueBoll = 16
    print('双色球分析预测结果（{}+{}）'.format(red,bule))
    getResult(redBoll, blueBoll)
else:
    print('Type Error！')

Pcount, Ppre = getPrice(red,bule)
Tpre = Ppre * Vcount
print("\n总共分析出{}大注(复式{}+{}), 每大注{}元, {}大注总共{}元, 每大注中有{}小注, {}大注中总共{}小注".format(Vcount, red, bule, Ppre, Vcount, Tpre, Pcount, Vcount, Vcount*Pcount))