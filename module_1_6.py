my_dict = {'Aleksandr' : 1988,
           'Anna': 1993,
           'Alla': 1962}
print(my_dict)
print(my_dict['Alla'])
print(my_dict.get('Alex'))
my_dict.update({'Roma': 1983,
                'Sergey': 1959})
del_key = my_dict.pop('Aleksandr')
print(del_key)

my_set = {'Aleksandr', 1, 2, 1, 3, 2, 3, 'Aleksandr'}
print(my_set)
my_set.add(False)
my_set.add(4)
my_set.discard(1)
print(my_set)