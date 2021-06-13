#빗물
def main() :
    H, W = map(int, input().split())
    blocks = list(map(int, input().split()))
    check_walls = False
    result = 0

    while True :
        check_walls = False
        count = 0
        for i in range(len(blocks)) :
            blocks[i] -= 1
            if blocks[i] >= 0 :
                if check_walls :
                    result += count
                    count = 0
                if not check_walls :
                    check_walls = True

            if blocks[i] < 0 and check_walls :
                count+=1

        if check_walls == False :
            break

    print(result)

if __name__ == "__main__" :
    main()