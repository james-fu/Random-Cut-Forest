import matplotlib.pyplot as plt
import csv
import datetime as dt
from code.random_cut_forest import RandomCutForest
import numpy as np
import math
import time

def open_csv():
    x1 = []
    y1 = []
    zip_x_y =[]
    with open('data/dataset.csv') as fil:
        data = csv.reader(fil)
        for i in data:
            x1 += [int(i[0])]
            y1 += [float(i[1])]
            zip_x_y += [tuple([int(i[0]), float(i[1])])]
    return x1, y1, zip_x_y


x, y, data = open_csv()

q = time.time()
r = RandomCutForest(data, sensitive=1)
r.start()
print(time.time() - q)
a = []
b = []
for i in r.get_result():
    a += [i[0]]
    b += [i[1]]

x = list(map(lambda time: dt.datetime.fromtimestamp(time), x))
a = list(map(lambda time: dt.datetime.fromtimestamp(time), a))


plt.subplot(2, 1, 1)
plt.plot(x, y)
# plt.ylim(-.5,1.1)
# plt.ylim(-300,300)
plt.title('Incoming data')
plt.ylabel('Temperature(x/15)')

plt.subplot(2, 1, 2)
plt.plot(a, b)
# plt.ylim(0,1)
plt.title('Anomaly')
plt.xlabel('Abstract time')
plt.ylabel('Anomaly value')
plt.show()





# ---------------------- debuging ----------------------
# data = [(0,1),
#         (1,2),
#         (2,-2),
#         (3,5),
#         (4,10),
#         (5,-12),
#         (6,7),
#         (7,20),
#         (8,1),
#         (9,2)]
#
# r = RandomCutForest(data, sensitive=1)
# r.start()
# r.get_result()

