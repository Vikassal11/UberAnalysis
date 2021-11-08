import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import Constants as co

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

A= (45, 31, 42, 35, 39)
B= (38, 31, 26, 28, 33)
C= (10, 15, 17, 21, 12)
D= (9, 14, 16, 22, 141)

ax1.plot(A,B)
ax2.scatter(C,D)
# fig, (ax1, ax2) = plt.subplots(ncols=2)
# plt.show()
