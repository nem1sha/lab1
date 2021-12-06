import json

def read_file():
    file = open('pokemon_full.json')
    a = file.read()
    b = json.loads(a)
    return a, b

def count_symbols(a):
    return len(a)

def count_no_signs(a):
    count = 0
    for i in a:
        if i.isalnum():
            count += 1
    return count

def search_max_dscrp(b):
    max_length = 0
    name_of_pokemon = ''
    for char in b:
        if len(char["description"]) > max_length:
            max_length = len(char["description"])
            name_of_pokemon = char["name"]
    return name_of_pokemon

def search_longest_ability(b):
    max_number = 0
    ability = ''
    for skills in b:
        for skill in skills['abilities']:
            if len(skill.split()) > max_number:
                max_number = len(skill.split())
                ability = skill
    return ability

def print_results(a, b):
    print('1. Общее количество символов:', count_symbols(a))
    print('2. Общее количество символов без пробелов и знаков препинания:', count_no_signs(a))
    print('3. Покемон с самым длинным описанием:', search_max_dscrp(b))
    print('4. Умение с самым большим количеством слов: ', search_longest_ability(b))

if __name__ == '__main__':
    pokemon_full, pokemon_full_list = read_file()
    print_results(pokemon_full, pokemon_full_list)
