my_family = {
    'mother': {
        'name': 'Heather',
        'age': 49
    },
    'father': {
        'name': 'Calvin',
        'age': 49
    },
    'younger sister': {
        'name': 'Peyton',
        'age': 21
    },
    'youngest sister': {
        'name': 'Zoe',
        'age': 19
    }
}

for key, val in my_family.items():
    print val['name'],'is my',key,'and is',str(val['age']),'years old.'
