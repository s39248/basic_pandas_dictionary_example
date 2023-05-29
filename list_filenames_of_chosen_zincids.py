import pandas as pd
from biopandas.mol2 import PandasMol2
import os

path = "/Desktop/mol_files/"

list_files = os.listdir(path)
print(list_files)

#create dictionary with filename and zincids:
real_zincids={}
filenames={}
for index, list_files in enumerate(list_files):
	pmol = PandasMol2().read_mol2(path + list_files)
	real_zincids[index]=pmol.code
	filenames[index]=list_files

print(real_zincids)
print(filenames)


# function to return key for any value
def get_key(val):
	for key, value in real_zincids.items():
		if val == value:
			return key
	return "key doesn't exist"
    
#find keys for list of zincids:
zincid_chosen = ['ZINC08442796', 'ZINC05093851', 'ZINC33854447', 'ZINC49032005']
keys=[]
for f in zincid_chosen:
	keys.append(get_key(f))

print(keys)
print(len(keys))

#function to get values for any key:
def get_value(any_key):
    for key, value in real_zincids.items():
         if any_key == key:
             return value
    return "value doesn't exist"

#find values for keys:
values=[]
for x in keys:
	values.append(get_value(x))

print(values)
print(len(values))
