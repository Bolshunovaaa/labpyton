# Multiparadigmatic  programming languages:Task_1
# Bolshunova Kateryna:IKM-221a
print('Multiparadigmatic  programming languages:Task_2\nBolshunova Kateryna:IKM-221a')

TEMPLATE = 'Please Enter {} : '
try:
    a = float(input(TEMPLATE.format('a')))
    b = float(input(TEMPLATE.format('b')))
    c = float(input(TEMPLATE.format('c')))
    res = ((11 + 2 * a + 4.1) / (12.4 - b)) + c
    print(res)
except ValueError:
    print('You wrote a letter,try to enter number')