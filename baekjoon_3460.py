#이진수
def main() :
    T = int(input())

    for i in range(T) :
        array = []
        num = int(input())

        while num != 0 :
            array.append(num%2)
            num = int(num/2)

        _len = len(array)

        for j in range(_len) :
            if array[j] == 1 :
                print(j, end=' ')

if __name__ == "__main__" :
    main()