# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

def get_prime_list(n):
    prime_list = []
    num = 2

    while num <= n:
        prime_bool = True
        for i in prime_list:
            if num % i == 0:
                prime_bool = False
                break
        if prime_bool:
            prime_list.append(num)
        num += 1

    return prime_list


def main():
    [m, n] = [int(item) for item in input("input M, N : ").split()]
    # m, n = 3, 16

    prime_list = get_prime_list(n)

    for prime in prime_list:
        if prime >= m:
            print(prime)


main()