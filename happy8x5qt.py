# coding=utf-8
import random

# 选5 4胆全拖  总共152

resultdic = {}
# 中奖金额结果
jpamount = []

# 中奖概率结果
jppercent = []

# 选择的胆码数量(4)
choiseNumberCount = 4

# 模拟购买多少期
qishu = 1

# 每期多少张

zhangshu = 10

# 中奖规则
package = {
    "zd0": 0,
    "zd1": 0,
    "zd2": 54,
    "zd3": 534,
    "zd4": 17260,
}


def red(msg):
    return "\033[31;1m{}\033[0m".format(msg)


def extra_same_elem(lst, *lsts):
    iset = set(lst)
    for li in lsts:
        s = set(li)
        iset = iset.intersection(s)
    return list(iset)


def getResultPotInfo():
    rpot = random.sample(range(1, 81), 20)
    rpot.sort()
    return rpot


def getInfo(choiseNumberCount):
    clist = random.sample(range(1, 81), choiseNumberCount)
    clist.sort()
    return clist


def openJP(cList, rList):
    lst = extra_same_elem(cList, rList)
    lst.sort()
    print("中奖胆码：" + str(lst))
    return lst


def getBounes(num):
    bou = 0
    if num == 0 or num == 1:
        pass
    elif num == 2:
        bou = package.get("zd2")
    elif num == 3:
        bou = package.get("zd3")
    elif num == 4:
        bou = package.get("zd4")
    return bou



vl = 0
for vq in range(qishu):
    print("====================第{}期===========================".format(vq+1))
    resultPotList = getResultPotInfo()
    print("开奖号码" + str(resultPotList))
    for vz in range(zhangshu):
        print("")
        print("第[{}]注-开始选号并开奖。。。。。。".format(vz+1))
        # time.sleep(3)
        choiseNumberList = getInfo(choiseNumberCount)
        print("我选择的4胆码" + str(choiseNumberList))
        HitNumbersList = openJP(choiseNumberList, resultPotList)
        amount = getBounes(len(HitNumbersList))
        print("总共中了："+ str(len(HitNumbersList)) + "个胆，总奖金为："+ str(amount) +"元，收益率："+str(round((((amount /152)-1) *100),2)) +"%")
        jpamount.append(amount)
        # jppercent.append(round((((amount /152)-1) *100),2))
        vl += amount
    print("=====================================================")

print("总投入{}，总收益{}，收益率{}%".format((qishu*152*zhangshu),red(vl),red(((vl/(qishu*152*zhangshu))-1)*100)))
print(jpamount)
print("0:{} 54:{} 534:{} 17260:{}".format(jpamount.count(0),jpamount.count(54),jpamount.count(534),jpamount.count(17260)))
resultdic["0"] = round(jpamount.count(0)/(qishu*zhangshu)*100,2)
resultdic["54"] = round(jpamount.count(54)/(qishu*zhangshu)*100,2)
resultdic["534"] = round(jpamount.count(534)/(qishu*zhangshu)*100,2)
resultdic["17260"] = round(jpamount.count(17260)/(qishu*zhangshu)*100,2)

print(resultdic)
