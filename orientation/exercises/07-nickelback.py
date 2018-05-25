songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Marianas Trench', 'Beside You'),
    ('Nickelback', 'Look at this Graph'),
    ('OK Go', 'This Too Shall Pass')
}

not_nickelback = [s for s in songs if s[0] != 'Nickelback']

print not_nickelback