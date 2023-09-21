import random
import string
def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choices(characters, k=length))
    return password
def main():
    print("Welcome to the Strong Password Generator")

    try:
        length = int(input("Enter the password length you want: "))
        if length <= 0:
            print(" NOTE : Password length should be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
        return

    password = generate_password(length)

    print("Password is Generated :", password)


if __name__ == "__main__":
    main()
