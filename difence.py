import json
import random

file = open('pokemon_full.json')
pokemon_full = file.read()

pokemon_full_list = json.loads(pokemon_full)

# amount = 0
# for pokemon in pokemon_full_list:
#     amount += 1
# N = random.randint(2, amount)

N = int(input('Введите количество покемонов участвующих  взабеге:'))

runners = random.sample(pokemon_full_list, N)
names = []
stats = []
speed = []
for runner in runners:
    names.append(runner['name'])
    stats.append(runner['stats'])
for stat in stats:
    speed.append(stat['speed'])
k = 0
number = 0
max_speed = 0
for i in speed:
    k += 1
    if i > max_speed:
        max_speed = i
        number = k-1
print('Самый быстрый покемон:', names[number], '; среди:', names)





