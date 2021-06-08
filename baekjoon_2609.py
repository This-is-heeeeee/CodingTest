#최대공야수와 최소공배수
def get_gcd(n, m) :
    if m == 0 :
        return n

    r = n % m
    return get_gcd(m, r)

def main() :
    array = list(map(int, input().split()))
    array.sort()

    n = array[1]
    m = array[0]

    gcd = get_gcd(n, m)
    lcm = int(n * m / gcd)

    print(gcd)
    print(lcm)

if __name__ == "__main__" :
    main()