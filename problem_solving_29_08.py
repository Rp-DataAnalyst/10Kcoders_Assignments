Find even digits in a number &count the no of even digits:
 num1= input('enter a number:')
 count=0
 even_digits=[]
 for i in num1:
       if int(i)%2==0:
             count+=1
             even_digits.append(int(i))
 print(even_digits)
 print(count)
 num1=int(input('enter a number:'))
 even_numbers=[]

 while num1>0:
       digits=num1%10
       if digits%2==0:
             even_numbers.append(digits)
       num1=num1//10
 print(even_numbers)
# Find prime digits in a number using while loop:
 num1= int(input('enter a number:'))
 prime_digits=[]
 while num1>0:
       digit=num1%10
       if digit in (2,3,5,7):
             prime_digits.append(digit)
       num1=num1//10
 print(prime_digits)
 Find a perfect number:
num1= int(input('enter a number:'))
original_num=num1
perfect_number= 0
for i in range(1,(num1//2)+1):
      if num1%i==0:
            perfect_number+=i
print(perfect_number)
if original_num== perfect_number:
      print('the given number is a perfect number')
else:
      print('The given number is not a perfect number')





