#지능형 기차 2
def main() :
    num = 0
    array = []

    for i in range(10) :
        n, k = map(int, input().split())
        num = num - n + k
        array.append(num)

    array.sort()

    result = array[-1]

    print(result)

if __name__ == "__main__" :
    main()