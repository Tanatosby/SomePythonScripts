'''
This script is for a real problem in my work that was the following one: 

We have a proccess in Banner ERP that is CAPP execution. This script achieve the number of run capps, and not run capps from a SRMBCMP.lis file

'''

import numpy as np
import pandas as pd

url = input('Ingrese url: ')
data = pd.read_excel(url)
datos = data['SMRBCMP']
datos.dropna(inplace=True)
mask = datos.str.contains('not', na=False)
mask1 = datos.str.contains('Compliance run', na=False)
notdf = datos[mask]
rundf = datos[mask1]
id_not = []
id_run =  []
for i in notdf:
    k = i.split()[0]
    id_not.append(k)
for j in rundf:
    l= j.split()[0]
    id_run.append(l)

unique_not = set(id_not)
unique_run = set(id_run)
print(f'los que no se han corrido son {len(unique_not)}')
print(f'los que se han corrido son {len(unique_run)}')
print(f'total es {len(unique_not)+len(unique_run)}')
