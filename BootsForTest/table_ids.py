import pandas as pd
dicc = {'IDs': []} 
dicc2 = {'IDs': []}
for i in range(2000,3001):
    dicc['IDs'].append(f'PR00{i}')

for i in range(3002,4030):
    dicc2['IDs'].append(f'PR00{i}')
df = pd.DataFrame(dicc)
df.to_csv('dicc1.csv', index= False)
df = pd.DataFrame(dicc2)
df.to_csv('dicc2.csv', index= False)



