import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import GeneraldataAPI as gd

df = pd.read_csv(
    r'C:\Users\Dozie\Downloads\Compressed\access-2016-working-files\Access 2016 Working Files\InvoicesList.txt')
print(df)


d = pd.DataFrame(df, columns=['Invoice Num', 'Contract Num'])


xs = [i for i in gd.data.keys()]
ys = [i for i in gd.data.values()]
plt.plot(xs, ys)
#plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("daily minutes")
plt.show()
