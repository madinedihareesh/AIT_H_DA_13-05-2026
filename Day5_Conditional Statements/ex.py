'''
Condition statement
smaple if
if else
if elif else
nested condtional
match
'''

# age=20
# if age>=18:
#     print('Essible for Driving License')

# isUpi=True

# if isUpi:
#     print('Amount transfred successfully')

#if else

# num=int(input('Enter a number'))
# if num%2==0:
#     print('Even NUmber')
# else:
#     print('Odd number')    

# marks=int(input('Emter marks: '))
# if marks>0:
#     if marks>=90:
#         print("Grade 'A'")
#     elif marks>=70 and marks<90:
#         print("Grade 'B'") 
#     elif marks>=50 and marks<70:
#         print("Grade 'C'")  
#     else:
#         print("Grade 'F'")  
# else:
#     print('Enter Proper Marks')           

# mot=input('Enter you mot')
# if mot=='Train':
#     print('I am going by train')
# elif mot=='Bus':
#     print('I am going by Bus')
# elif mot=='Flight':
#     print('I am going by Flight')
# elif mot=='Bike':
#     print('I am going By Bike')
# elif mot=='Car':
#     print('I am Going By Car')    
# else:
#     print('Not Planning to Leave')    


day=int(input('Enter Day Number: '))

match day:
    case 1:
        print('Moday')
    case 2:
        print('Tuse')
    case 3:
        print('Wed')
    case 4:
        print('Thurs')
    case 5:
        print('Fri')
    case 6:
        print('Sat')
    case 7:
        print('Sun')
    case _:
        print('Enter valid number')                      

