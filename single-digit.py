def single_digit():
    while True:
        try:
            number = int(input("Enter a number: "))
            if number < 0:
                print("Please enter a positive number.")
                continue
            if number < 10:
                print(f"The number is already a single digit: {number}. Exiting the program.")
                return

            break
        except ValueError:
            print("Please enter a valid number.")

    while number >= 10:
        number = sum(int(digit) for digit in str(number))

    print(f"The single digit is: {number}")

single_digit()
