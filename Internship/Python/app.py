digit = 153
sum = 0
temp = digit
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == 153:
    print("The number is an Armstrong number")      
else:
    print("The number is not an Armstrong number")

