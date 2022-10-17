#Написать программу-парсер, которая принимает группу различных скобок и проверяет, верно ли они расставлены:
#Количество открывающих и закрывающих скобок должно совпадать
#Закрывающая скобка не должна быть раньше открывающей
#Последняя открывающая скобка должна быть тождественна следующей закрывающей
#Например, "((((){}[]{}[])))", "(  dv { ddd { qwerty }} ___) exit", "([{ correct }])" — верно,
#"abc [ io (private] close ) ", "([{ wrong })]" — неверно.

input = input('Введитке скобки: ', )
spisok = []

for i in input:
    if i == '(' or i == '{' or i == '[':
        spisok.append(i)
    elif i == ')':
        if len(spisok) > 0:
            if spisok[-1] == '(':
                del spisok[-1]
            else:
                print('Не верно')
                raise SystemExit
        else:
            print('Не верно')
            raise SystemExit
    elif i == '}':
        if len(spisok) > 0:
            if spisok[-1] == '{':
                del spisok[-1]
            else:
                print('Не верно')
                raise SystemExit
        else:
            print('Не верно')
            raise SystemExit
    elif i == ']':
        if len(spisok) > 0:
            if spisok[-1] == '[':
                del spisok[-1]
            else:
                print('Не верно')
                raise SystemExit
        else:
            print('Не верно')
            raise SystemExit
if len(spisok) > 0:
    print('Не верно')
else:
    print('верно')