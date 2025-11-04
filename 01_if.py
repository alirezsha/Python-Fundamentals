import math

#x = int(input('Write a number: '))
x = -81

if x < 0:
    x = abs(x)
    
print(math.sqrt(x))
print('---------------------------------')

x = 9

if True:
    x = 13

print(x)
print('---------------------------------')

#x = int(input('Write a number: '))
x = 6

if x % 2 == 0:
    print("It's an even!")
else:
    print("It's an odd!")

print('---------------------------------')

# a = int(input("Write a number for a:"))
# b = int(input("Write a number for b:"))
a = 9
b = 13

if a == 3 or b == 6:
    print("That's right!")
else:
    print("That's wrong!")

print('---------------------------------')

names = ['Amir', 'Alireza', 'Yas']

if 'Parsa' in names:
    print("Yes")
else:
    print("No")

print('---------------------------------')

# x = int(input("Write a number for x:"))
# y = int(input("Write a number for y:"))
x = 3
y = 6

# if x < y:
#     n = x
# else:
#     n = y

n = x if x < y else y

print(n)
print('---------------------------------')

vowels = 'aeiou'

# if 'o' in vowels:
#     r = "Yes"
# else:
#     r = "No"

r = "Yes" if ('o' in vowels) else "No"

print(r)
print('---------------------------------')

# a = int(input("Write a number for a:"))
# b = int(input("Write a number for b:"))
a = 3
b = 9

c = a if a > b else (b + 6)

print(c)
print('---------------------------------')

# score = int(input("Enter the score: "))
score = 19

r = 'Failed' if score < 10 else 'Passed'

print(r)
print('---------------------------------')

# today = input("Is it Holiday or Working Day?: ")
today = 'Holiday'
# m = int(input("How much money do you have in your account?: "))
m = 30000

if today == 'Holiday':
    if m > 16000:
        print("Let's go shopping!")
    else:
        print("Let's play PlayStation!")
else:
    print("So let's go work!")
    
print('---------------------------------')

# score = int(input("Enter the score: "))
score = 93

if score >= 90:
    r = 'A'
elif score >= 80:
    r = 'B'
elif score >= 70:
    r = 'C'
else:
    r = 'D'

print(r)
print('---------------------------------')

# a = int(input("Write a number for a:"))
# b = int(input("Write a number for b:"))
a = 6
b = -9

if a > 0 and y > 0:
    print("+ * + = Positive")
elif a > 0 and y < 0:
    print("+ * - = Negative")
elif a < 0 and y > 0:
    print("- * + = Negative")
else:
    print("- * - = Positive")

print('---------------------------------')

# age = int(input("Enter the age: "))
age = 33
# gender = input("What is his/her gender?: ")
gender = "Female"

if age < 18:
    if gender == "Female":
        print('Daughter')
    else:
        print("Son")
elif age >= 18 and age < 63:
    if gender == "Female":
        print("Mother")
    else:
        print("Father")
else:
    if gender == "Female":
        print("Grandmother")
    else:
        print("Grandfather")
        
print('---------------------------------')

# h = int(input("Enter the height: "))
h = 1.93
# w = int(input("Enter the weight: "))
w = 83

bmi = w / (h**2)

if bmi < 15:
    r = 'Very severely underweight'
elif 15 <= bmi <= 16:
    r = 'Severely underweight'
elif 16 < bmi <= 18.5:
    r = 'Underweight'
elif 18.5 < bmi <= 25:
    r = 'Normal'
elif 25 < bmi <= 30:
    r = 'Overweight'
elif 30 < bmi <= 35:
    r = 'Moderately obese'
elif 35 < bmi <= 40:
    r = 'Severely obese'
else:
    r = 'Very severely obese'

print("BMI = " + str(bmi) + " He/She is " + r + ".")
