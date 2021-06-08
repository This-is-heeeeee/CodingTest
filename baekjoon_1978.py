#소수 찾기
def main() :
    N = int(input())
    array = list(map(int, input().split()))
    count = N

    for num in array:
        if num == 1 :
            count -= 1
            continue
        for i in range(2, num) :
            if num%i == 0:
                count -= 1
                break



    print(count)



if __name__ == "__main__" :
    main()