def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    print("\nMATHEMATICS LEARNING TOOL")
    print("Select an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        value = int(input("Enter a non-negative integer: "))
        if value >= 0:
            result = factorial(value)
            print(f"[RESULT] Factorial of {value} ({value}!) = {result}")

    elif choice == "2":
        num_terms = int(input("Enter number of terms to generate: "))
        if num_terms >= 0:
            fib_list = []
            for i in range(num_terms):
                fib_list.append(fibonacci(i))
            print(f"[RESULT] Fibonacci series ({num_terms} terms): {fib_list}")

    elif choice == "3":
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")


