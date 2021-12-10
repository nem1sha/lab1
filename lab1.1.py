import json

def read_file(file):
    pokemon_full = file.read()
    pokemon_full_list = json.loads(pokemon_full)
    return pokemon_full, pokemon_full_list

def count_symbols(pokemon_full):
    return len(pokemon_full)

def count_no_signs(pokemon_full):
    count = 0
    for i in pokemon_full:
        if i.isalnum():
            count += 1
    return count

def search_max_dscrp(pokemon_full_list):
    max_length = 0
    name_of_pokemon = ''
    for char in pokemon_full_list:
        if len(char["description"]) > max_length:
            max_length = len(char["description"])
            name_of_pokemon = char["name"]
    return name_of_pokemon

def search_longest_ability(pokemon_full_list):
    max_number = 0
    ability = ''
    for skills in pokemon_full_list:
        for skill in skills['abilities']:
            if len(skill.split()) > max_number:
                max_number = len(skill.split())
                ability = skill
    return ability

def print_results(exercise_1, exercise_2, exercise_3, exercise_4):
    print('1. Общее количество символов:', exercise_1)
    print('2. Общее количество символов без пробелов и знаков препинания:', exercise_2)
    print('3. Покемон с самым длинным описанием:', exercise_3)
    print('4. Умение с самым большим количеством слов: ', exercise_4)

if __name__ == '__main__':
    file = open('pokemon_full.json')
    pokemon_full, pokemon_full_list = read_file(file)
    exercise_1 = count_symbols(pokemon_full)
    exercise_2 = count_no_signs(pokemon_full)
    exercise_3 = search_max_dscrp(pokemon_full_list)
    exercise_4 = search_longest_ability(pokemon_full_list)
    print_results(exercise_1, exercise_2, exercise_2, exercise_4)

