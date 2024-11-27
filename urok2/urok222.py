list_append = [1, 2, 3]
print(list_append)           #Пише list_append

list_append.append(4)
print(list_append)            #list_append поширюється цифрою 4

list_append.append(5)          #list_append поширюється цифрою 5
print(list_append)

list_extend = [4, 5, 6]
print(list_extend)              #Створюється list_extend 
list_extend.extend([7, 8, 9])    #list_extend поширюється цифрами 7, 8, 9
print(list_extend)


print(list_extend.index(6))        #Видає індекс 6 у list_extend

print(len(list_append))            #Видає довжину list_extend
