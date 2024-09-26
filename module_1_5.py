immutable_var = 1, 'string', True
print(immutable_var)
# immutable_var[2] = False  #Выводится ошибка так как tuple не изменяемый.
# print(immutable_var)
mutable_list = ([1, 'string', True], 1, 2)
mutable_list[0][2] = False
print(mutable_list)