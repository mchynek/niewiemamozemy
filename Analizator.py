import string
import requests

print("""            1. Pobierz plik z internetu 
            2. Zlicz liczbe liter w pobranym pliku
            3. Zlicz liczbe wyrazów w pliku
            4. Zlicz liczbe znaków interpunkcyjnych w pliku.
            5. Zlicz liczbe zdan w pliku
            6. Wygeneruj raport o uzyciu liter (A-Z)
            7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt
            8. Wyjscie z programu""")

url = r'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwjT9_C2z5fmAhXisosKHY9AB_UQFjAAegQIBRAJ&url=http%3A%2F%2F25.io%2Ftoau%2Faudio%2Fsample.txt&usg=AOvVaw2ICc9VRyFRjKYeSurH31CF' #tu wpisac poprawny link do tekstu
myfile=requests.get(url)
open(r'plik.txt', 'wb').write(myfile.content) #a tutaj wpisac lokalizacje gdzie ma byc plik pobrany


stats=open(r'statystyki.txt', "w+")
try:
    char_count=0
    text = open(r'plik.txt', 'r')
    data = text.read()
    for char in data:
        if char in string.ascii_letters:
            char_count=char_count+1
    print('Number of characters in text file: ', char_count)
    stats.write('Number of characters in text file: ' + repr(char_count)+'\n')
    text.close()
except OSError as e:
    print('File not found. Please download the file once again')
stats.close()
stats=open(r'statystyki.txt', "a+")

try:
    file = open(r'plik.txt', 'r')
    data = file.read().split()
    count_words=len(data)
    #poprawic, liczy kazda sekwencje charow, oddzielonych spacjami. nawet jezeli to znaki punct.
    print('Number of words in text file: ', count_words)
    stats.write('Number of words in text file: ' + repr(count_words)+'\n')
    file.close()
except OSError as e:
    print('File not found. Please download the file once again')

try:
    punct=0
    plik = open(r'plik.txt', 'r')
    plik_open = plik.read()
    for char in plik_open:
        if char in string.punctuation:
            punct=punct+1
    print("Number of punctuactions in text file: ", punct)
    stats.write('Number of punctuations in text file: ' + repr(punct)+'\n')
    plik.close()
except OSError as e:
    print('File not found. Please download the file once again')

try:
    import re
    file = open(r'plik.txt', 'r')
    data=file.read()
    sentence=re.split(r'[.?!]\s*', data)
    count_sent=len(sentence)-1
    print('Number of sentences in text file: ', count_sent)
    stats.write('Number of sentences in text file: ' + repr(count_sent)+'\n')
    file.close()
except OSError as e:
    print('File not found. Please download the file once again')

low_letters_list=[]
low_letters_list=string.ascii_lowercase
letters_list=string.ascii_uppercase
count_low=[]
for letter in low_letters_list:
    count_low.append(data.count(letter))

upp_letters_list=[]
letter_occur={}
upp_letters_list=string.ascii_uppercase
letters_list=string.ascii_uppercase
count_upp=[]
for letter in upp_letters_list:
    count_upp.append(data.count(letter))

let=[]
for i in range (0, 26 ):
    let.append(count_low[i]+count_upp[i])

for i in range (0,26):
    print(upp_letters_list[i], ": ", let[i])
    stats.write(repr(upp_letters_list[i])+ ": "+ repr(let[i])+'\n')
stats.close()

import os
print ("8. Wyjście z progtamu T/N?")
action = input()
if(action=='T'):
    os.remove("statystyki.txt")
    os.remove("plik.txt")
