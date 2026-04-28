"""
I have list of numbers [1,2,3,4,5,6]
Without using inbuilt functions find mean of the list of numbers
"""
numbers = [1,2,3,4,5,6]
sum = 0
count = 0
for number in numbers:
    sum = sum+number
    count = count+1
mean = sum/count
print(f"The mean is {mean}")

"""
Fizz Buzz 
Loop over Number from 1 to 100
If number is divisible by 3 print Fizz
If number is divisible by 5 print Buzz
If number is divisible by both 3 and 5 print FizzBuzz
Else print the number
5%2=1
i%3==0:
    print("Fizz)
"""

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)