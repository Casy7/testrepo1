'''Напишите программу, которая вводит с клавиатуры непустой массив целых чисел, и выводит
число локальных максимумов (элемент является локальным максимумом, если он не имеет
соседей, больших, чем он сам).'''
#a=[1,3,4,3,4,3,24,3,11,1,1,1,234,387]
a=input("Введите массив чисел(через запятую):  ")
a=a.replace(" ","")
a=a.split(",")
a.append(-999999999)
maxes=[]
for i in range(len(a)):
    a[i]=float(a[i])
for i in range(len(a)-1):
	if a[i-1]<=a[i]>=a[i+1]:
		maxes+=[a[i]]
print(maxes)
