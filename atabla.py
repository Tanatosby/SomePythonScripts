import pandas as pd
f = open('file.txt')
dicce = dict()

def column(f,t):
  #f is the string that represents the title of the column to extract. 
  for l in f:
    lr = l.strip()
    if lr.startswith(t): 
      ll = lr.split()
      dicce[t] = [ll[1]]
      for i in range(len(2:ll)):
        dicce[t].append(i)

t1 = 'column 1'
t2 = 'column 2'
t3 = 'column 2'

column(f,t1)
column(f,t2)
column(f,t3)

df = pd.DataFrame(ficce)
df.to_excel('file.xlsx')

