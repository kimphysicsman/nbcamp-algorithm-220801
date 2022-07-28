# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
#
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

def get_greatest_common_factor(a, b):
    if a > b:
        a, b = b, a

    gcf = None

    n = 1
    while n <= a:
        if a % n == 0 and b % n == 0:
            gcf = n
        n += 1

    return gcf


def get_least_common_multiple(a, b):
    if a > b:
        a, b = b, a

    lcm = None

    n = b
    while n <= a * b:
        if n % a == 0 and n % b == 0:
            lcm = n
            break
        n += 1

    return lcm


def main():
    [a, b] = [int(item) for item in input("input A, B : ").split()]
    # a, b = 24, 18

    if a > b:
        a, b = b, a

    gcf = get_greatest_common_factor(a, b)
    lcm = get_least_common_multiple(a, b)

    print(gcf)
    print(lcm)



main()