import string
import requests

print ("1. Wybierz plik wejsciowy")
decision=raw_input('Czy program ma pobrac plik z Internetu? T/N')
if decision==('T'):
print("Podaj URL pliku: ")
url=raw_input()
myfile = requests.get(url)
with open('C:\Users\studentwsb\Desktop\nowy.txt', 'w') as f:
f.write(myfile.content)
if decision==('N'):
print("Podaj sciezke pliku: ")
url=raw_input()


try:
    char_count=0
    text = open(r'C:\Users\analyse_text.txt', 'r')
    data = text.read()
    for char in data:
        if char in string.ascii_letters:
            char_count=char_count+1
    print('Number of characters in text file: ', char_count)
    stats.write('Number of characters in text file: ' + repr(char_count)+'\n')
except OSError as e:
    print('File not found. Please download the file once again')
stats.close()
stats=open(r'C:\Users\analyse_text.txt', "a+")
try:
    file = open(r'C:\Users\analyse_text.txt', 'r')
    data = file.read().split()
    print(data)
    count_words=len(data)
    print('Number of words in text file: ', count_words)
    stats.write('Number of words in text file: ' + repr(count_words)+'\n')
except OSError as e:
    print('File not found. Please download the file once again')

try:
    punct=0
    plik = open(r'C:\Users\analyse_text.txt', 'r')
    plik_open = plik.read()
    for char in plik_open:
        if char in string.punctuation:
            punct=punct+1
    print("Number of punctuactions in text file: ", punct)
    stats.write('Number of punctuations in text file: ' + repr(punct)+'\n')
except OSError as e:
    print('File not found. Please download the file once again')

try:
    import re
    file = open(r'C:\Users\analyse_text.txt', 'r')
    data=file.read()
    sentence=re.split(r'[.?!]\s*', data)
    print(sentence)
    count_sent=len(sentence)-1
    print('Number of sentences in text file: ', count_sent)
    stats.write('Number of sentences in text file: ' + repr(count_sent)+'\n')
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
