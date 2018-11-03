people={'first_name':'cheng',
        'last_name':'peng',
        'age':20,
        'city':'ningbo',}
lists={'s':0,
    'k':9,
    'l':8,}
favorite_language={'jen':['python','c','f'],
    'sarah':['d','f','f'],
    'edward':['ruby'],
    'phil':['python','d',],
    }
favorite_language['cheng']='r'

for xf in favorite_language.keys():
    for h in favorite_language[xf]:
        print(xf.title()+" favorite "+h)
    


