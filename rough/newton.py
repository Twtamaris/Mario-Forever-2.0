print("This Is Newton Apple")
while True:
    try:
        x = float(input("Enter a number: "))
        break
    except ValueError:
        print("You must enter a number")
        continue
guess = x / 2.0
i = 0
while guess * guess != x and i < 20:
    guess = (guess + x / guess) / 2.0
    i += 1
print("Square root of", x, "is about", guess)
print("Newton's method got it right in", i, "tries")
