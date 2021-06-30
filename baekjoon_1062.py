#가르침
def main() :
    N, K = map(int, input().split())

    if K < 5:
        print(0)
        return
    elif K == 26:
        print(N)
        return

    words = []
    result = 0

    K -= 5

    for i in range(N):
        string = input()
        string = string.replace('a', '')
        string = string.replace('n', '')
        string = string.replace('t', '')
        string = string.replace('i', '')
        string = string.replace('c', '')

        #string = list(set(string))
        string = ''.join(set(string))


        if len(string) <= K :
            words.append(string)

    words.sort(key=len, reverse=True)

    checked_list = []

    while K and words:
        letters = {}
        for word in words:
            if word in checked_list :
                continue
            check = True

            for k, v in letters.items():
                if word in k:
                    letters[k] += 1
                    check = False
                    break

            if not letters or check:
                letters[word] = 1
        for k, v in letters.items():
            if len(k) <= K:
                K -= len(k)
                result += v
                for word in words:
                    if word in k:
                        checked_list.append(word)

    print(result)


if __name__ == "__main__" :
    main()

"""
3 8
antargbtica
antartica
antavtica
"""