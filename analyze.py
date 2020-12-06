import sys
import numpy as np
import matplotlib.pyplot as plot

if __name__ == "__main__":
    path = sys.argv[1]

    # あらかじめすべての行を展開する
    with open(path, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    
    records = []

    # データの整形を行う
    for line in lines:
        if len(line) <= 1:
            continue
        records.append(line.strip().split(";"))
    
    with open(path + ".re.csv", "w", encoding="SJIS") as f:
        for record in records:
            f.write(",".join(record) + "\n")

    # numpyのDatetime型に変換
    for record in records[1:]:
        record[0] = record[0].replace(" ", "T")
        record[1] = record[1].replace(" ", "T")

        record[0] = np.datetime64(record[0])
        record[1] = np.datetime64(record[1])
    