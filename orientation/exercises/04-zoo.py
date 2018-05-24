zoo = ('elephant', 'snow leopard', 'komodo dragon', 'eyelash viper')

print zoo.index('snow leopard')

print 'eyelash viper' in zoo

(noodle_nose, fluff_tail, acid_spit, cute_n_deadly) = zoo

print 'Cute \'n\' deadly:',cute_n_deadly
print 'Noodle nose:', noodle_nose

zoo = list(zoo)

print zoo

zoo.extend(['maned wolf', 'leachianus gecko', 'otter'])

print zoo

zoo = tuple(zoo)

print zoo