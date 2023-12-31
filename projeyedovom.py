# list farzi
names = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

def selection_moratab(names):
    for i in range(len(names)-1):
        min_index = i
        for j in range(i+1, len(names)):
            if names[j]['Last Name'] < names[min_index]['Last Name']:
                min_index = j
            elif names[j]['Last Name'] == names[min_index]['Last Name']:
                if names[j]['First Name'] < names[min_index]['First Name']:
                    min_index = j
        names[i], names[min_index] = names[min_index], names[i]
    return names
# ...................................................................
esmhayemoratabshode = selection_moratab(names)
print(esmhayemoratabshode)
# ...................................................................
import matplotlib.pyplot as plt
import random
import time

def selections(people):
    n = len(people)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if people[j]['First Name'] < people[min_index]['First Name']:
                min_index = j
        people[i], people[min_index] = people[min_index], people[i]


def tolid_random(n):
    dade = []
    for _ in range(n):
        first_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        last_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        dade.append({'First Name': first_name, 'Last Name': last_name})
    return dade

def zaman_moratabsazi(dade):
    start_time = time.time()
    selections(dade)
    end_time = time.time()
    return end_time - start_time


dade_andaze = list(range(5, 200, 10))
sorting_times = []

for size in dade_sizes:
    dade = tolid_random(size)
    sorting_time = zaman_moratabsazi(dade)
    sorting_times.append(sorting_time)


plt.plot(dade_sizes, sorting_times)
plt.xlabel('tedad dade vorodi')
plt.ylabel('modat zaman calculate')
plt.title('tedad dade vorodi bar hast zaman baraye mohasebe')
plt.show()

