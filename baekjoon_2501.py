#약수 구하기
divisors = []

def main() :
    N, K = map(int, input().split())

    for i in range(1,N+1) :
        if N % i == 0 :
            divisors.append(i)

    if K > len(divisors) :
        result = 0
    else :
        result = divisors[K-1]

    print(result)


if __name__ == "__main__" :
    main()