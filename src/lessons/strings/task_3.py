# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef"

text = input('Please enter your text: ')
text = text.replace(' ', '')
dublicates = []

for result in text:
    if result not in dublicates:
        dublicates.append(result)
print(''.join(dublicates))