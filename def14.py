def func_multiply_digits(a):
    digit1=a%10
    a//=10
    digit2=a%10
    a//=10
    digit3=a%10
    a//=10
    digit4=a%10
    digit5=a//10
    multiply_digits=digit1*digit2*digit3*digit4*digit5
    return multiply_digits
# a=int(input())
# print(func_multiply_digits(a))    