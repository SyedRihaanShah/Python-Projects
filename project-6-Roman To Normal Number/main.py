Romanstr = input("Enter Your Roman Number: ")

RomanNum_to_NormalNum = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}
 
num = 0

Romanstr = Romanstr.replace('IV', 'IIII')
Romanstr = Romanstr.replace('IX', 'VIIII')
Romanstr = Romanstr.replace('XL', 'XXXX')
Romanstr = Romanstr.replace('XC', 'LXXXX')
Romanstr = Romanstr.replace('CD', 'CCCC')
Romanstr = Romanstr.replace('CM', 'DCCCC')

RomList = list(Romanstr)

for char in RomList:
    num = num + RomanNum_to_NormalNum[char]

print(num)