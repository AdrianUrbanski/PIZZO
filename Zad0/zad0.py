import json
import sys

path = input()
with open(path, 'r') as f:
    automaton = json.load(f)

accepting = automaton["accepting"]

dict = {}
for t in automaton["transitions"]:
   dict[(t["letter"], t["from"])] = t["to"]

state = automaton["initial"]

c = sys.stdin.read(1)

while c:
    if c != '\n':
        state = dict[(c, state)]
    else:
        if state in accepting:
            print("yes")
        else:
            print("no")
        state = automaton["initial"]
    c = sys.stdin.read(1)
