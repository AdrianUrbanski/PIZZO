import json
import sys

path = input()
with open(path, 'r') as f:
     tutorzy = json.load(f)

studenci = tutorzy["studenci"]
konflikty = tutorzy["konflikty"]

print(f'p cnf {2*studenci} {4*len(konflikty)}')

for k in konflikty:
    i = k["zrzeda"]
    j = k["nielubiany"]
    print(f'{2*i-1} {2*i} {2*j-1} {2*j} 0')
    print(f'{2*i-1} {2*i} -{2*j-1} -{2*j} 0')
    print(f'-{2*i-1} -{2*i} {2*j-1} {2*j} 0')
    print(f'-{2*i-1} -{2*i} -{2*j-1} -{2*j} 0')
