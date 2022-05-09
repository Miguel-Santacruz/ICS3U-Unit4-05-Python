#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Apr 2022
# This program adds positive numbers


def main():
    # This function adds positive numbers
    answer = 0

    # input
    string1 = input("How many numbers are you going to add: ")

    # process & output
    try:
        amount_of_numbers = int(string1)
        if amount_of_numbers < 0:
            print("Invalid amount of numbers.")
        else:
            while amount_of_numbers > 0:
                amount_of_numbers = amount_of_numbers - 1
                string2 = input("Enter number to add: ")
                try:
                    number = int(string2)
                    if number < 0:
                        continue
                    answer = answer + number
                except Exception:
                    continue
            print("Sum of just positive numbers is: {}".format(answer))
    except Exception:
        print("Invalid amount of numbers.")

    print("\nDone.")


if __name__ == "__main__":
    main()
