list_append = [1, 2, 3]
print(list_append)           #Пише list_append

list_append.append(4)
print(list_append)            #list_append поширюєтся до 4 цифр

list_append.append(5)          #list_append поширюєтся до 5 цифр
print(list_append)

list_extend = [4, 5, 6]
print(list_extend)              #Створюється list_extend 
list_extend.extend([7, 8, 9])    #list_extend поширюєтся символами 7, 8, 9
print(list_extend)


print(list_extend.index(6))        #Видає індекс 6 у list_extend

print(len(list_append))            #Видає довжину list_extend
