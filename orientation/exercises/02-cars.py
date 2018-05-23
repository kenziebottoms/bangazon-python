showroom = {
    'The Batmobile',
    'Wonder Woman\'s Invisible Plane',
    'Lamborghini',
    'Toyota Prius'
}
print len(showroom)

showroom.add('Toyota Prius')
# no dice because it's a duplicate string
# shrug emoji!!!
print len(showroom)

new_cars = {
    'Xterra',
    'Kia Soul'
}
showroom.update(new_cars)
print len(showroom)

showroom.discard('Xterra')
print len(showroom)