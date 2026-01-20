name = "Abdallah"
age = 21
height = 175.5
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


x = float(input())
y = float(input())

print(x + y)
print(x - y)
print(x * y)
try:
    print(x / y)
except ZeroDivisionError:
    print("Division by zero is not allowed")


n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


for i in range(2, 21, 2):
    print(i)


secret = 7
guess = None
while guess != secret:
    guess = int(input())


file = open("data.txt", "w")
file.write("Line 1\nLine 2\nLine 3")
file.close()

file = open("data.txt", "r")
print(file.read())
file.close()


numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
print(max(numbers))
print(numbers[::-1])


cities = ("Cairo", "Alex", "Giza", "Aswan")
print(cities[0])
print(cities[-1])


group1 = {"Ahmed", "Ali", "Mona", "Sara"}
group2 = {"Sara", "Omar", "Ali", "Laila"}
print(group1 & group2)


try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed")


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def average_temperature(temp_list, scale):
    avg = sum(temp_list) / len(temp_list)
    if scale == "F":
        return celsius_to_fahrenheit(avg)
    return avg

def highest_temperature(temp_list, scale):
    high = max(temp_list)
    if scale == "F":
        return celsius_to_fahrenheit(high)
    return high


try:
    temps = input().split(",")
    temps = [float(t) for t in temps]

    avg_c = average_temperature(temps, "C")
    high_c = highest_temperature(temps, "C")

    avg_f = average_temperature(temps, "F")
    high_f = highest_temperature(temps, "F")

    print(avg_c, high_c)
    print(avg_f, high_f)
except:
    print("Invalid input")
