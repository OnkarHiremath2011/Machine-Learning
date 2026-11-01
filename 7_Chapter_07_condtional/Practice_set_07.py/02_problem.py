# 2. Write a program to find out whether a student has passed or failed if it requires a 
#    total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
#    take marks as an input from the user.

sub1=float(input("Enter the marks: "))
sub2=float(input("Enter the marks: "))
sub3=float(input("Enter the marks: "))

total_marks=sub1+sub2+sub3
percentage=(total_marks)/100

if (sub1>=33 and sub2>=33 and sub3>=33):
    print("Congratulations ! you are pass")
else:
    print(" failed , Better luck next time !")