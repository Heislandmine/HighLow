from HighAndLow import HighAndLow
import sys
import csv

itr = int(sys.argv[1])
result = []
for i in range(0, itr):
    dl = HighAndLow.Dealer()
    ag = HighAndLow.Agent()
    hl = HighAndLow.HighAndLow()

    result.append(hl.high_and_low(dl, ag))

f = open('result.csv', 'w')
writer = csv.writer(f, lineterminator="/n")
writer.writerow(result)
f.close()

