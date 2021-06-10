#연산자 끼워넣기
def func(nums, operators) :
    num_temp = []
    operators_temp = [[], [], [], []]
    result_max = []
    result_min = []
    if operators[0] :
        operators_temp[0] = operators.copy()
        operators_temp[0][0] -= 1
        num_temp.append(nums[0] + nums[1])

    if operators[1] :
        operators_temp[1] = operators.copy()
        operators_temp[1][1] -= 1
        num_temp.append(nums[0] - nums[1])

    if operators[2] :
        operators_temp[2] = operators.copy()
        operators_temp[2][2] -= 1
        num_temp.append(nums[0] * nums[1])

    if operators[3] :
        operators_temp[3] = operators.copy()
        operators_temp[3][3] -= 1
        num_temp.append(int(nums[0] / nums[1]))

    num_max = max(num_temp)
    num_min = min(num_temp)

    if len(nums) > 2 :
        index = 0
        for i in range(4) :
            if operators_temp[i] :
                temp = nums[2:].copy()
                temp.insert(0,num_temp[index])
                max_temp, min_temp = func(temp, operators_temp[i])
                result_max.append(max_temp)
                result_min.append(min_temp)
                index+=1
        return max(result_max), min(result_min)

    else :
        #print(num_max, num_min)
        return num_max, num_min




def main() :
    N = int(input())
    nums = list(map(int, input().split()))
    operators = list(map(int, input().split())) #+ - x /

    max_num, min_num = func(nums, operators)
    print(max_num, min_num)

if __name__ == "__main__" :
    main()