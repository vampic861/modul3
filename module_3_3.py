def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(123, False, 'str')
print_params(c = 'сон')
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [4532, 'дом', False]
values_dict = {'a': 34541, 'b': 'цифра', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [25.25, True]
print_params(*values_list_2, 66)