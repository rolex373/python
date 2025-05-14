def get_month_name(n):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[n - 1] if 1 <= n <= 12 else None

count = 0

while True:
    user_input = input("Enter a number (1-12) or type 'stop' to exit: ")
    if user_input.lower() == 'stop':
        print(f"Exiting the program. You entered values {count} time(s).")
        break
    try:
        n = int(user_input)
        count += 1
        month = get_month_name(n)
        print(f"The month is: {month}" if month else "Invalid number. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'stop' to exit.")
