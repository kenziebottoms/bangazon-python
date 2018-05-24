planet_list = ['Mercury', 'Mars']

planet_list.append('Jupiter')
planet_list.append('Saturn')

planet_list.extend(['Uranus','Neptune'])

planet_list.insert(1,'Venus')
planet_list.insert(2,'Earth')

planet_list.append('Pluto')

rocky_planets = planet_list[:4]

del planet_list[-1]

print planet_list

satellites = [
    ('Mariner 6', 'Mars'),
    ('Opportunity', 'Mars'),
    ('Cassini', 'Saturn'),
    ('Voyager 2', 'Neptune'),
    ('Juno', 'Jupiter')
]

for planet in planet_list:
    print planet+':   ',
    for sat in satellites:
        if sat[1] == planet:
            print sat[0]+'   ',
    print ''