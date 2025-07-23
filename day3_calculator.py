import day3_math_operations as m

functions = [m.add, m.minus, m.multiply, m.divide, m.exponent]


if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Exponent")
        print("6: Exit")
        
        choice = int(input("\nEnter your choice: "))

        if choice == 6:
            break
        else:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))

            result = functions[choice - 1] (a, b)
            print(result)


