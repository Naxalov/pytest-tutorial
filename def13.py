def func_sumdigits(a):  #five-digit number
    digit1=a%10 #5
    a//=10
    digit2=a%10 #4
    a//=10
    digit3=a%10 #3
    a//=10
    digit4=a%10 #2
    digit5=a//10 #1
    sum_digits=digit1+digit2+digit3+digit4+digit5
    return sum_digits
# a=int(input())
# print(func_sumdigits(a))    