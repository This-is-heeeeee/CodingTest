#쉽게 푸는 문제
def make_array() :
    array = []
    num = 1;
    count = 0;
    for i in range(1000) :
        if num == count :
            num += 1
            count = 0
        array.append(num)
        count+=1

    return array


def main() :
    A, B = map(int, input().split())

    array = make_array()

    result = sum(array[A-1 : B])

    print(result)


if __name__ == "__main__" :
    main()