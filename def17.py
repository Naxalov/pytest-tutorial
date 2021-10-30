def func_sum_even(n):
    e_digit1=n%10
    n//=10
    e_digit2=n%10
    e_digit3=n//10
    sum_even=e_digit1*(1-e_digit1%2)+e_digit2*(1-e_digit2%2)+e_digit3*(1-e_digit3%2)
    return sum_even
# n=int(input())
# print(func_sum_even(n))    