n1 = float(input('Enter your first note\n'))
n2 = float(input('Enter your second note\n'))
average = (n1 + n2) / 2

print(f'the average of student is: {average:,.1f}')

if average < 7:
    print('Student disapproved!')
else:
    print('Student approved! Compliment :)')