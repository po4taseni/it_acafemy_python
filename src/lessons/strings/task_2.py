# Задание 2
# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания

sentence = input('Please enter your text: ')  # "This is a sentence"
sentence = sentence.replace(',' '')

max_len = 0
max_word = ""

words = sentence.split(" ")  # ["This", "is", "a", "sentence"]
for word in words:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word

print(max_word)
