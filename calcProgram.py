# coding=utf-8
import random
from itertools import product
# 1 dlt 2 ssq
goType = 1

# total Count
tCount = 100

# r red  b blue
r = 11
b = 11

totalAmount = 0
# 4,12,16,17,18,21,22,24,28,29,31+1,3,4,5,6,7,8,9,10,11,12

# 4,12,16,22,29+2,6
# dltjp = {
#     "0+2":"9,5",
#     "1+2":"9,5",
#     "2+1":"9,5",
#     "2+2":"8,15",
#     "3+0":"9,5",
#     "3+1":"8,15",
#     "3+2":"6,200",
#     "4+0":"7,100",
#     "4+1":"5,300",
#     "4+2":"4,3000",
#     "5+0":"3,10000",
#     "5+1":"2,5000000",
#     "5+2":"1,10000000",
# }


dlt_jackpot = {
    "1":["5+2"],
    "2":["5+1"],
    "3":["5+0"],
    "4":["4+2"],
    "5":["4+1"],
    "6":["3+2"],
    "7":["4+0"],
    "8":["3+1","2+2"],
    "9":["3+0","1+2","2+1","0+2"],
}

dltjp = {
    "0+2":"9,5",
    "1+2":"9,5",
    "2+1":"9,5",
    "2+2":"8,15",
    "3+0":"9,5",
    "3+1":"8,15",
    "3+2":"6,200",
    "4+0":"7,100",
    "4+1":"5,300",
    "4+2":"4,3000",
    "5+0":"3,10000",
    "5+1":"2,200000",
    "5+2":"1,10000000",
}


def getresult(redb, blueb, redBoll, blueBoll, times = 1):
    if times == 1:
        rred = random.sample(range(1, redb+1), redBoll)
        rred.sort()
        rblue = random.sample(range(1, blueb+1), blueBoll)
        rblue.sort()
        res = str(rred).split(']')[0].split('[')[1] + "  +  " + str(rblue).split('[')[1].split(']')[0]
        return res.replace(" ","")
    else:
        kl = []
        for tms in range(times -1):
            rred = random.sample(range(1, redb+1), redBoll)
            rred.sort()
            rblue = random.sample(range(1, blueb+1), blueBoll)
            rblue.sort()
            res = str(rred).split(']')[0].split('[')[1] + "  +  " + str(rblue).split('[')[1].split(']')[0]
            kl.append(res.replace(" ",""))
        return kl



def createNumberList():
    if goType == 1:
        result = getresult(35, 12, 5, 2)
    elif goType == 2:
        result = getresult(33, 16, 6, 1)
    else:
        print("Type ERROR")
    return result.replace(" ", "")



def createNumberforClient():
    if goType == 1:
        result100 = getresult(35, 12, r, b, tCount)
    elif goType == 2:
        result100 = getresult(33, 16, r, b, tCount)
    else:
        print("Type ERROR")
    return result100




def getJPCount(red,bule):
    if goType == 1:
        k = 5
        t = 2
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


def getCount(key):
    rb = key.split("-")[0]
    bb = key.split("-")[1]
    getJPCount(rb,bb)

def calcUtilC(a, b):
    if b < a:
        return 0
    elif a == 0:
        return 1
    else:
        k = 1
        p = b
        for i in range(a):
            k *= p
            p -= 1
        t = 1
        for i in range(1, a + 1):
            t *= i
        return int(k / t)


def calcCountForPreLevel(hitrc,hitbc,levelr,levelb):
    if goType == 1:
        ak = calcUtilC(int(levelr),hitrc)
        bk = calcUtilC(5-int(levelr),r - hitrc)
        ck = calcUtilC(int(levelb),hitbc)
        dk = calcUtilC(2-int(levelb),b - hitbc)
        return int(ak*bk*ck*dk)
    elif goType == 2:
        pass
    else:
        print("Type ERROR")


def colloctJPnum(rjpc,bjpc):
    global totalAmount
    if goType == 1:
        j1, j2, j3, j4, j5, j6, j7, j8, j9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        tta = 0
        for jplevel in dlt_jackpot.keys():
            hitnum = 0
            totalAmount1 = 0
            for jpleveldetail in dlt_jackpot[jplevel]:
                hitnum += calcCountForPreLevel(rjpc,bjpc,jpleveldetail.split("+")[0],jpleveldetail.split("+")[1])
            if hitnum != 0:
                jj = dltjp["{}".format(jpleveldetail)].split(",")[1]
                totalAmount1 += int(jj)*hitnum
                if jplevel == "1":
                    j1 += hitnum
                elif jplevel == "2":
                    j2 += hitnum
                elif jplevel == "3":
                    j3 += hitnum
                elif jplevel == "4":
                    j4 += hitnum
                elif jplevel == "5":
                    j5 += hitnum
                elif jplevel == "6":
                    j6 += hitnum
                elif jplevel == "7":
                    j7 += hitnum
                elif jplevel == "8":
                    j8 += hitnum
                elif jplevel == "9":
                    j9 += hitnum
                tta += totalAmount1
        totalAmount += tta
        print("一等奖:{}, 二等奖:{}, 三等奖:{}, 四等奖:{}, 五等奖:{}, 六等奖:{}, 七等奖:{}, 八等奖:{}, 九等奖:{}, 总奖金:{}".format(j1, j2, j3, j4, j5, j6, j7, j8, j9, tta))


def checkJackPotLevel(type):

    return True

def checkJackPot(clients,jPNumber):
    jprs = set(jPNumber.split("+")[0].split(","))
    jpbs = set(jPNumber.split("+")[1].split(","))
    for cln in clients:
        rset = set(cln.split("+")[0].split(","))
        bset = set(cln.split("+")[1].split(","))
        Yesrs = jprs & rset
        Yesbs = jpbs & bset
        Yesrl = ','.join(Yesrs)
        Yesbl = ','.join(Yesbs)
        rjpc = 0
        bjpc = 0
        if Yesrl != "":
            rjpc = len(Yesrs)
        if Yesbl != "":
            bjpc = len(Yesbs)
        if checkJackPotLevel("{}+{}".format(rjpc,bjpc)):
            colloctJPnum(rjpc,bjpc)


# 生成开奖号码

JPNumber = createNumberList()
print("开奖号码：{}".format(JPNumber))

# 生成随机购买号码
Clietns  = createNumberforClient()
print("购买号码：{}".format(Clietns))

checkJackPot(Clietns,JPNumber)
# checkJackPot(["4,12,16,17,18,21,22,24,28,29,31+1,3,4,5,6,7,8,9,10,11,12"],"4,12,16,22,29+2,6")
# 4,12,16,17,18,21,22,24,28,29,31+1,3,4,5,6,7,8,9,10,11,12

# 4,12,16,22,29+2,6
ttc,ttp = getPrice(r,b)
print("最终总奖金：{}  总共{}注,花费{}".format(totalAmount, ttc*tCount, ttp*tCount))
print("收益率：{} %    收益：{}元".format((totalAmount/(ttp*tCount)-1)*100,(totalAmount - ttp*tCount)))
