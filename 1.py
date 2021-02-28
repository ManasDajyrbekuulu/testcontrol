#1 zadacha
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

dict_1={}
for index,value in enumerate(lst):
    dict_1[index+0]=value
print(dict_1)

#2 задание
print("Игра: Угадай число")


import random
guesses_made = 0

number = random.randint(1, 20)
print ("Угадай число от 1 до 20")

while guesses_made < 5:
    guess = int(input('Введи число: '))
    guesses_made += 1

    if guess < number:
        print ('Слишком мало')

    if guess > number:
        print ('Слишком много')

    if guess == number:
        break

if guess == number:
    print ("Класс! Вы угадали.")
else:
    print ("Все, вы не выиграли. Игра завершилась")


# 3 задание

def i (text):
  simvol = int(len(text) /2)
  
  some_string = text[simvol-1:simvol+2]
  print( some_string)
  
i("Adverts")
 

# 4 задание 

def merge(s1, s2): 
    result = "" 
    i = 0
    while (i < len(s1)) or (i < len(s2)):
        if (i < len(s1)):
            result += s1[i] 
 
        if (i < len(s2)):
            result += s2[i] 
             
        i += 1
         
    return result
 
s1 = "Aidana"
s2 = "Adilet"
 
print(merge(s1, s2))