#멀티탭 스케줄링
def main():
    N, K = map(int, input().split())
    order = list(map(int, input().split()))
    appliances = {}
    powerstrip = []
    result = 0

    for i in range(len(order)):
        if order[i] in appliances.keys():
            appliances[order[i]].append(i+1)
        else :
            appliances[order[i]] = [i+1]

    #print(appliances)

    for o in order:
        if len(powerstrip) >= N and o not in powerstrip:
            max = -1
            key = None
            for k in powerstrip:
                if not appliances[k]:
                    key = k
                    break
                if appliances[k][0] > max:
                    max = appliances[k][0]
                    key = k

            result += 1
            powerstrip.remove(key)

        elif o in powerstrip:
            appliances[o].pop(0)
            continue

        powerstrip.append(o)
        #print(powerstrip)
        #print("{} :{}".format(o, appliances[o]))
        appliances[o].pop(0)

    print(result)

if __name__ == "__main__":
    main()

