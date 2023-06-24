Problem Statement : to integrate Pokemon API data with CSV target.

Extractor link: https://hub.meltano.com/extractors/tap-pokeapi/
Loader link: https://hub.meltano.com/loaders/target-csv/

Platform: AWS EC2 (Ubuntu)

Prerequisites:
- An AWS EC2 instance
- Docker installed
- Meltano installed

1. Initialize a meltano project 
   $ meltano init Pokemon
   $ cd Pokemon

2. Add extractor
   $ meltano add extractor tap-pokeapi

3. Add loader
   $ meltano add loader target-csv

4. Since Airbyte requires pokemon_name parameter to fetch desired Pokemon's data
   - For single Pokemon data 
     $ meltano config tap-pokeapi set airbyte_config pokemon_name pikachu
     $ meltano run tap-pokeapi target-csv

   - For multiple Pokemon data use script.py to automate the fetchin of multiple Pokemon data
     $ python3 script.py

5. Check output in output folder
