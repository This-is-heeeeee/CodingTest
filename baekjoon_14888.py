#연산자 끼워넣기
max = 0
min = 0

def func(nums, operators) :
    num_temp = [[], [], [], []]
    operators_temp = [[], [], [], []]
    result = []
    if operators[0] :
        operators_temp[0] = operators
        operators_temp[0][0] -= 1
        num_temp[0][0] = nums[0] + nums[1]

    if operators[1] :
        operators_temp[1] = operators
        operators_temp[1][1] -= 1
        num_temp[1][0] = nums[0] - nums[1]

    if operators[2] :
        operators_temp[2] = operators
        operators_temp[2][2] -= 1
        num_temp[2][0] = nums[0] * nums[1]

    if operators[3] :
        operators_temp[3] = operators
        operators_temp[3][3] -= 1
        num_temp[3][0] = int(nums[0] / nums[1])

    if len(nums) > 3 :
        for i in range(4) :
            if num_temp[i] :
                num_temp[i].extend(nums[2:])
                result.append(func(num_temp[i], operators_temp[i]))

    if len(nums) <= 2 :





def main() :
    N = int(input())
    nums = list(map(int, input().split()))
    operators = list(map(int, input().split())) #+ - x /

    max = 0

    min = 0

if __name__ == "__main__" :
    main()