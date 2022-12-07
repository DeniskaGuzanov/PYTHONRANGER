#1 Напишите программу, удаляющую из файла все слова, содержащие "абв".

file = ('abv wer tre abv qwe sre abv abv')


slovo = ('abv')
for string in file.split('\n'):
    for i in slovo:
        string = string.replace(i, '')
    if string:
        print(string)