def main():
    numbers = list(map(int, input().split()))
    n,m,a = numbers[0], numbers[1],numbers[2]
    if n%a > 0:
        side_one = n // a + 1
    else:
        side_one = n/a
    if m%a >0:
        side_two = m//a +1
    else:
        side_two = m/a
    output=int(side_one)* int(side_two)
    print(output)
main()