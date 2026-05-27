# print '*' insted of owels in a string

vowels='aeiouAEIOU'


'''
s=input('Enter a String')
i=0
while i<len(s):
    if s[i] in vowels:
        print('*')
    else:    
        print(s[i])
    i+=1
'''

'''st=input('Enter a string: ')
rev=''
i=len(st)-1
while i>=0:
    rev+=st[i]
    i-=1
if st==rev:
    print(st,'is a palendrome')
else:
    print(st,'is not a palendrome')  '''      


# num=int(input('Enter a  number for fact: '))
# res=1
# while num>0:
#     res*=num
#     num-=1
# print(res)    

'''
num=int(input('Enter a number: '))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
        print(i,'is a factor of num',num)
    i+=1
print(count,'is no of factors for num',num)  '''      

'''
num=int(input('Enter a number: '))
count=0
i=1
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print(num,'is a prime number')
else:
    print(num,'is not a prime number')   '''   


# year=int(input('Enter a year: '))
# if year%100==0:
#     if year%400==0:
#         print(year,'Year is a leapyear')
#     else:
#         print(year,'is not a leap year')
# elif year%4==0:
#     print(year,'is a leap year')
# else:
#     print(year,'is not a leap year')            