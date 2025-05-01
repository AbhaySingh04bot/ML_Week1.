name = input("Enter your name: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number for age.")

location = input("Enter your location: ")
interest = input("Enter something you're interested in: ")

intro = f"""
Hi! My name is {name}. I'm {age} years old and I live in {location}.
One of my main interests is {interest}. I'm excited to keep learning and exploring new things!
"""

print(intro)

