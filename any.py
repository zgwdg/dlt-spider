# coding=utf-8
# 期号|日期|前区|后区|奖池|销售|一等奖|一等奖追加|二等奖|二等奖追加|三等奖|四等奖|五等奖|六等奖|七等奖|八等奖|九等奖



dltData = open("result-dlt.txt","r").read().split("\n")

for vlist in dltData:
    h1 = vlist.split("|")[2]
    print(h1)



