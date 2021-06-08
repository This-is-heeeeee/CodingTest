#N번째 큰 수
def main() :
    T = int(input())
    result = []

    for i in range(T):
        array = list(map(int, input().split()))
        array.sort()

        result.append(array[-3])

    for i in range(T):
        print(result[i])

if __name__ == "__main__" :
    main()