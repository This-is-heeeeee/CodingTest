#괄호의 값
def main() :
    parentheses = input()
    temp = []
    nums = []
    check = []
    result = 0
    pre = ''

    for parenthes in parentheses:
        if parenthes == '(' or parenthes == '[':
            if not temp and nums:
                result += nums[0]
                nums = []
            if pre == '(' or pre == '[':
                check.append(len(nums))
            temp.append(parenthes)

        elif parenthes == ')':
            if not temp or temp[-1] == '[':
                print(0)
                return
            nums.append(2)
            temp.pop()
            if pre == ')' or pre == ']' :
                num = sum(nums[check[-1]:-1]) * nums[-1]
                nums = nums[:check[-1]]
                nums.append(num)
                check.pop()

        elif parenthes == ']':
            if not temp or temp[-1] == '(':
                print(0)
                return
            nums.append(3)
            temp.pop()
            if pre == ')' or pre == ']' :
                num = sum(nums[check[-1]:-1])*nums[-1]
                nums = nums[:check[-1]]
                nums.append(num)
                check.pop()

        else :
            print(0)
            return
        pre = parenthes
        """
        print("parenthes : {}".format(parenthes))
        print("temp : {}".format(temp))
        print("nums : {}".format(nums))
        print("check : {}".format(check))
        """

    if temp or not nums:
        result = 0

    else: result += nums[0]

    print(result)

if __name__ == "__main__" :
    main()