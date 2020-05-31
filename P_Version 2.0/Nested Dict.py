section = {'A':{'Strength':30,
                 'girls':12,
                 'boys':18
               },
           'B':{'Strength':45,
                 'girls':25,
                 'boys':20
                }
          }

key1 = input('Enter the 1key: ')
key2 = input('Enter the 2key: ')

if key1 in dict:
  #print(section[key1])
  print(section[key1][key2])

else:
  print('Invalid Key, try again')

