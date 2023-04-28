import random
a=input('input: ')
computer = random.choice([1,2,3]);
cal=(3+a-computer)%3

if cal==0:
    print('비김');
elif cal==1:
    print('이김');
elif cal==2:
    print('짐');
else:
    print('다시');

       