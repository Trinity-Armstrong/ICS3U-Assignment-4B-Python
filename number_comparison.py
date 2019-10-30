#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: October 2019
# This is the number comparison program


def main():
    # This function runs the number comparison program

    # input
    try:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        print("")

    # process
        if first_number > second_number:
            print(first_number, ">", second_number)
        elif first_number < second_number:
            print(first_number, "<", second_number)
        elif first_number == second_number:
            print(first_number, "=", second_number)
    except Exception:
        print("")
        print("This is not an integer.")


if __name__ == "__main__":
    main()
