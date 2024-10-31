def single_digit():
    while True:
        try:
            number = int(input("Enter a number: "))
            if number < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
