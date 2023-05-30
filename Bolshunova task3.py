# Multiparadigmatic  programming languages:Task_3
# Bolshunova Kateryna:IKM-221a
import math

print('Multiparadigmatic  programming languages:Task_3\nBolshunova Kateryna:IKM-221a')

TEMPLATE = 'Please Enter {} : '
try:
    x = int(input(TEMPLATE.format('x')))
    z = int(input(TEMPLATE.format('z')))
    if z != 2:
        res = (x * math.atan(z)) + math.exp((x + 3) / (z - 2))
        print(f'Result is: {res}')
    else:
        print('Error,your function will not work,type something else')
except ValueError:
    print('You wrote a letter,try to enter number')