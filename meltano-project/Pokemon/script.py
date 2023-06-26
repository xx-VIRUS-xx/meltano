import os
import pandas as pd
import csv

pokemon=['pikachu','charizard' , 'snorlax' , 'squirtle' ]
for i in pokemon:
 cmd='meltano config tap-pokeapi set airbyte_config pokemon_name ' + i
 cmd2='meltano run tap-pokeapi target-csv'
 os.system(cmd)
 os.system(cmd2)

f_list=[]
for dirpath, dirs, files in os.walk('/root/meltano/meltano-project/Pokemon/New-output'):
 for filename in files:
  fname = os.path.join(dirpath,filename)
  if fname.endswith('.csv'):
   f_list.append(fname)

df_csv_concat = pd.concat([pd.read_csv(file) for file in f_list ], ignore_index=True)

df_csv_concat.to_csv('pokemon_list.csv')

