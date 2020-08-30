a = 55
b = 8
c = 9
text = 'Text'
print(a,"",b,"",c,"",text)
a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
text = (input('Текстовая переменная: '))
print(a,b,c,text)


sec = int( input('Enter seconds: ') )
h = ((sec//3600))%24
m = (sec//60)%60
s = sec%60
print(h,'hours',m,'min',s,'sec')

 
n = int(input('Enter n: '))
print('n + nn + nnn = ',n + n*10 + n + n*100 + n*10 + n)


n = int(input('Введите целое положительное число: '))
m = n%10
n = n//10
while n > 0:
    if n%10 > m:
        m = n%10
    n = n//10
print('Самая большая цифра:',m)


a = float(input('Выручка: '))
b = float(input('Издержки: '))
if a > b :
    print('Прибыль составила: ',int(a-b))
    p = int(input('Кол-во сотрудников: '))
    print('Прибыль на одного сотрудника: ',(a-b)/p)
elif a == b :
    print('Фирма сработала в 0')
else:
    print('Убыток составил: ', int(b-a))


a = float(input('Км в первый день: '))
b = float(input('Цель: '))
day = 1
while a < b :
    a = a * 1.1
    day = day + 1
print('Кол-во дней понадобилось ', day,' дней для преодоления ', a, ' км')


