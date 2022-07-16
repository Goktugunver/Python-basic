number1 = 25
number2 = 30
number3 = 40
max = "Maximum number: "
min = "Minimum number: "

if number1>number2 and number1>number3:
    print(max,number1)

if number2>number1 and number2>number3:
    print(max,number2)

if number3>number1 and number3>number2:
    print(max,number3)

    
if number1<number2 and number1<number3:
    print(min,number1)

if number2<number1 and number2<number3:
    print(min,number2)

if number3<number1 and number3<number2:
    print(min,number3)
