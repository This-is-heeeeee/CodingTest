#일곱 난쟁이
def main() :
    array = []
    sum = 0
    for i in range(9) :
        n = int(input())
        array.append(n)
        sum += n

    diff = sum - 100

    array.sort()

    for i in range(9) :
        if len(array) < 9 :
            break
        for j in range(i+1, 9) :
            if array[i] + array[j] == diff :
                del array[j]
                del array[i]
                break

    for i in range(len(array)) :
        print(array[i])


if __name__ == "__main__" :
    main()