#Задание 1:
# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы


text = input('Enter your text: ')

bltrs = 0
smltrs = 0

for count in text:
    if count.isupper() and 'A' <= count <= 'Z':
        bltrs += 1
    elif count.islower() and 'a' <= count <= 'z':
        smltrs += 1
print('Amount of big letters', bltrs)
print('Amount of small letters', smltrs)


