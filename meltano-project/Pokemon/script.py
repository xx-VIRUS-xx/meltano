import os
pokemon=['pikachu','charizard' , 'snorlax' , 'squirtle' ]
for i in pokemon:
 cmd='meltano config tap-pokeapi set airbyte_config pokemon_name ' + i
 cmd2='meltano run tap-pokeapi target-csv'
 os.system(cmd)
 os.system(cmd2) 
