'''
3. Является ли строка именем переменной в Python
'''
var1 = input("Введите строку:   ")
#Нечёткоое условие.
i = [k for k,v in locals().items() if v is var1][0]
if(i==var1):
	print("Значение переменной совпадает с её названием.")
else:
	print("Значение переменной не совпадает с её названием.")