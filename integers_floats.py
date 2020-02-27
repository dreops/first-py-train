number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

#Q: What will be the output of this code?
# I think the output will be the first string from the user
# converted into an integer printed along with the decimal 
# which is a float converted into an integer with the second
# input rounded down according to how Python works with the
# 'round' command and it will print each one on a new line e.g.
# If I enter '7' and then '2.5' it will print the following:
# 7
# 2.5
# 2
# A. Correct!