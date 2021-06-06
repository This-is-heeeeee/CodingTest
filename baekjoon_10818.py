#최소, 최대
def main() :
    N = int(input())

    array = list(map(int, input().split()))

    array.sort()

    print("{} {}".format(array[0], array[-1]))

if __name__ == "__main__" :
    main()