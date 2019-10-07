from HighAndLow import HighAndLow
import sys
import csv

itr = int(sys.argv[1])
p_type = int(sys.argv[2])
csv_header = ["MatchNo", "OpenCard", "NextCard", "Predict", "PredictResult"]

f = open('../result.csv', 'w')
writer = csv.writer(f, lineterminator="\n")
writer.writerow(csv_header)

for i in range(0, itr):
    dl = HighAndLow.Dealer()
    ag = HighAndLow.Agent(p_type)
    hl = HighAndLow.HighAndLow()

    result = hl.high_and_low(dl, ag, i)
    for n in range(len(result)):
        writer.writerow(result[n])

f.close()