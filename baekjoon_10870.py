#피보나치 수 5
def fibo(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1

    return fibo(n-1) + fibo(n-2)
def main() :
    n = int(input())

    print(fibo(n))


if __name__ == "__main__" :
    main()