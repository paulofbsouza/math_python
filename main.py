# THIS IS THE HEADER
# Owner: Mr. de Souza
# Description: Math Menu code with options
# Date: 08-2-2022

#Displays a welcome message
print ('This is Mr. de Souza Math Python CODE')

#Define a != value for opt different from 0, to begin the loop
opt=1

#Keep the menu inside a loop
while opt!=0:
  print('MENU- CHOSE AN OPTION BELOW:')
  print('1- # divisible by 2 - even numbers') #Print the option
  print('2- # not divisible by 2 - odd numbers')
  print('3- sum of numbers')
  print('4- Fibonacci sequence')
  print('5- Prime numbers')
  print('6- # Factorial')
  print('0- To exit')
  opt=int(input('Choose your option: '))

#Option 1 - Even #
  if opt==1:
    i=1
    a=int(input('Type a number, this option will show you the even #: '))
    while i<=a:
      if i%2==0:
        print(i)
      i=i+1
    print('\n\n')

 
#Option 2 - Odd # or Not even #   
  if opt==2:
    i=1
    a=int(input('Type a number, this option will show you the odds #: '))
    while i<=a:
      if i%2!=0:
        print(i)
      i=i+1
    print('\n\n')

  
#Option 3 - Summ the sequence
  if opt==3:
    i=1
    sum=0
    a=int(input('Type a number, this option will show you the sum: '))
    while i<=a:
      print(i)
      sum=sum+i
      print('The sum is: ', sum)
      i=i+1
    print('\n\n')


#Option 4 - Fibbnacci sequence
  if opt==4:
    N = int(input("Number of elements in Fibonacci Series, N, (N>=2) : "))
    #initialize the list with starting elements: 0, 1
    fibonacciSeries = [0,1]
    if N>2: 
      for i in range(2, N):
        #next elment in series = sum of its previous two numbers
        nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
        #append the element to the series
        fibonacciSeries.append(nextElement)
    print(fibonacciSeries)
    print('\n\n')
    

#Option 5 - Prime numbers
  if opt==5:
    lower = int(input("Enter the lower value:"))
    upper = int(input("Enter the upper value:"))
    for number in range(lower,upper+1):
      if number>1:
        for i in range(2,number):
          if (number%i)==0:
            break
        else:
              print(number)
    print('\n\n')

#Option 6 - Multiplication of the sequence (factorial)
  if opt==6:
    i=1
    f=1
    a=int(input('Type a number, this option will show you the factorial: '))
    while i<=a:
      f=f*i
      print(i,'! =',f)
      i=i+1
    print('\n\n')

#Break while option and displays a message      
  if opt==0:
    print('You choose "0" the program finished')
    break
