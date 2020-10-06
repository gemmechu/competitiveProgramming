def divide(dividend, divisor):
    result = 0
    sign = 1
    if dividend<0 or divisor<0 :
        if dividend<0 and divisor<0:
            sign = 1
        else:
            sign = -1
    dividend, divisor = abs(dividend), abs(divisor)
    while (divisor <= dividend ):
        tmp , cnt = divisor, 1
        while (tmp <= dividend):
            tmp <<= 1
            cnt <<= 1
        dividend -= tmp >> 1
        result += cnt >> 1
    if(sign == -1):
        result = ~(result - 1)

    #check overflow
    if()
    return result
print(divide(0,2))