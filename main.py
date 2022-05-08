list_a = [0,1,2]
list_b = ['zero', 'one', 'two']
list_c = ['cero', 'uno', 'dos']
list_all = list(zip(list_a, list_b, list_c))
print(list_all)
for a,b,c in list_all:
    print(f'{a} is {b} in English and {c} in Spanish.')
