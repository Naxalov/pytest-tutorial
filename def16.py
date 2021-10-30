def func_count_odd(n):
    digit1=n%10
    n//=10
    digit2=n%10
    n//=10
    digit3=n%10
    n//=10
    digit4=n%10
    digit5=n//10
    count_odd=count_even = digit1%2+digit2%2+digit3%2+digit4%2+digit5%2

    return count_odd
# n=int(input())
# print(func_count_odd(n))   