import json

file = open('pokemon_full.json')
pokemon_full = file.read()

print('1. Общее количество символов:', len(pokemon_full))

amount = 0
for i in pokemon_full:
    if i.isalnum():
        amount += 1
print('2. Общее количество символов без пробелов и знаков препинания:', amount)

pokemon_full_list = json.loads(pokemon_full)
max_length = 0
name_of_pokemon = ''
max_number = 0
if __name__ == '__main__':
    for char in pokemon_full_list:
        if len(char["description"]) > max_length:
            max_length = len(char["description"])
            name_of_pokemon = char["name"]
        for ability in char['abilities']:
            if len(ability.split()) > max_number:
                max_number = len(ability.split())
                longest_ability = ability
print('3. Покемон с самым длинным описанием:', name_of_pokemon)
print('4. Умение с самым большим количеством слов: ', longest_ability)
