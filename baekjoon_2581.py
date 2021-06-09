#소수
def find_prime(M, N) :
    array = []
    for i in range(M,N+1) :
        if i == 2 :
            array.append(i)
        for j in range(2,i) :
            if i%j == 0 :
                break
            if j == i-1 :
                array.append(i)

    return array

def main() :
    M = int(input())
    N = int(input())
    primes = find_prime(M, N)

    if not primes :
        print("-1")
        return

    result = [0, 0]
    result[0] = sum(primes)
    result[1] = primes[0]

    print(result[0])
    print(result[1])

    return


if __name__ == "__main__" :
    main()