"""
Doggy age

Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent.
"""

from dog import Dog

if __name__ == "__main__":
    try:
        dog = Dog(int(input("Enter dog age: ")))
    except ValueError:
        print("You entered not number!")
    else:
        print(f"Dog's age is {dog.human_age()} in human ages!")
