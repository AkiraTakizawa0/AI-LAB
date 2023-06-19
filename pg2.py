import pandas as pd

df = pd.read_csv("EnjoySports.csv", header=0)
dataset = df.values.tolist()
s = dataset[0][0:-1]
print(f"Initial Specific hypothesis {s}")
g = [['?' for i in range(len(s))] for j in range(len(s))]
print(f"Initial general hypothesis is {g}")

ins = 1

for row in dataset:
    if row[-1] == 'Yes':
        for j in range(len(s)):
            if row[j] != s[j]:
                s[j] = '?'
                g[j][j] = '?'
    elif row[-1] == 'No':
        for j in range(len(s)):
            if row[j] != s[j]:
                g[j][j] = s[j]
            else:
                g[j][j] = '?'
    print(f"Instance {ins}")
    ins += 1
    print(f"Specific Boundary is {s}")
    print(f"General Boundary is {g}")

print(f"Final Specific hypothesis is {s}")
print(f"Final general hypothesis is {g}")