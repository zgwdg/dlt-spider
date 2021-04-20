# coding=utf-8
import random
tCount = 100

loopCount = 10

preCive = 0


jp = 540


for p in range(loopCount):
    numPot = [x for x in range(1,11)]

    k = random.sample(numPot,5)

    print(k)

    hitCount = 0
    for z in range(tCount):
        c = random.sample(numPot, 5)
        # c = [4,3,6]
        flag = ""
        for p in c:
            if p not in k:
                flag="no"
                break
            else:
                flag="yes"
        if flag == "yes":
            # print("yes     {}".format(c))
            hitCount += 1

    print("共买{}注，中奖{}注，总收益{}元，总成本：{}元，收益率{}%".format(tCount,hitCount,hitCount*jp,tCount*2,((hitCount*jp)/(tCount*2) - 1)*100))
    preCive += hitCount*jp

print("共{}期，{}注，花费{}元，收益{}元".format(loopCount,loopCount*tCount,loopCount*tCount*2,preCive))






