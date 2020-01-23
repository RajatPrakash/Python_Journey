# WRITE A CODE THAT TAKES A LIST OF TEMPERATURES FROM A USER AND CONVERT THEM FROM CELSIUS TO FAHRENHEIT
# formula == 9/5 * C + 32
len = int(input('enter the length of list'))
Temp_C = []
for i in range(0, len):
    element = int(input('element:'))
    Temp_C.append(element)

Temp_F = [(9/5 * i + 32) for i in Temp_C]
print('Temp in CELSIUS -- {}, \nTemp in FAHRENHEIT {}'.format(Temp_C, Temp_F))
