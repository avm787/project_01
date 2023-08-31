import random
l = []
variable = 0
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
for i in range(3):
    n = random.choice(my_favorite_songs)
    l.append(n)
for i in l:     
    variable += i[1] 
variable = float('{:.2f}'.format(variable))     
print(f"Три песни звучат {variable} минут") 


    

from random import *
m = []
variable1 = 0
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
for i in range(3):
    data = list(my_favorite_songs_dict.items())
    r = sample(data, 1)
    m += r
for i in m:   
    variable1 += i[1]
variable1 = float('{:.2f}'.format(variable1))    
print(f"Три песни звучат {variable1} минут") 

  
       












