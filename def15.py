def func_count_even(n):
    digit1=n%10
    n//=10
    digit2=n%10
    n//=10
    digit3=n%10
    n//=10
    digit4=n%10
    digit5=n//10

    count_even = (1-digit1%2)+(1-digit2%2)+(1-digit3%2)+(1-digit4%2)+(1-digit5%2)

    return count_even
# n=int(input())
# print(func_count_even(n))     