# # print numbers from 1 to 100
# #  if no is % 3 print Fizz and if no is %5 print Buzz if Both print FizzBuzz

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
