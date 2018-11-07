import json

filename = 'numbername.json'

def shuru(a):
    filename = 'numbername.json'
    with open(filename,'w') as obj_f:
        json.dump(a,obj_f)

def shuchu():
    filename = 'numbername.json'
    with open(filename) as obj_f:
        r = json.load(obj_f)
        print(r) 

shuru(input())
shuchu()