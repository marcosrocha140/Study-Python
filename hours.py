name = str(input("Enter your name.\n"))
hours = int(input("Whats is hours now?\n"))

if hours < 24 and hours >= 18:
    print('Good Night!', name)
elif hours >= 0 and hours < 12:
    print('Good Morning', name)
elif hours >= 12 and hours < 18:
    print('Good Afternoom', name)
else:
    print("Value Invaid!")
