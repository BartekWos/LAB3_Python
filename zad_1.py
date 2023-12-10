# task 1
from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt


# a)
dataset = load_dataset("imodels/credit-card")
df = pd.DataFrame(dataset['train'])

# b)
df.drop_duplicates(inplace=True) # inplace directly aplly changes to df variable

# c)
corr_coeff = df['age'].corr(df['limit_bal'])
print(corr_coeff)

# d)
columns = df.columns.str.contains('bill_amt')  #check if bill_amt  is present in each column
df['bill_amt_X'] = df.loc[:, columns].sum(axis=1) # select data by labels and sum
print(df[0:5])

# e)
colum = df.columns.str.contains(r'\blimit_bal\b|\bage\b|\beducation:|\bbill_amt_X\b', regex=True)
fig, ax = plt.subplots()
ax.axis('off')
pd.plotting.table(ax, df.loc[:, colum].nlargest(10, 'age'), loc='center', cellLoc='center')
plt.show(block=False)

# f)
fig, ax = plt.subplots(1, 3, figsize=(15, 4))

ax[0].hist(df['limit_bal'],20)
ax[1].hist(df['age'], 20)
ax[2].hist2d(df['age'], df['limit_bal'], bins=40)

plt.show()
