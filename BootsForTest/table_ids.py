import pandas as pd
dicc = {'IDs': [],'email': []} 
for i in range(2000,4030):
    dicc['IDs'].append(f'PR00{i}')
    dicc['emai'].append(f'alumn{i}@gmail.com')

df = pd.DataFrame(dicc)
df.to_csv('dicc.csv', index= False)



