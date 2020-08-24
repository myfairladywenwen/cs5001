def gdc(m, n):
    if n == 0:
        return m
    else:
        return gdc(n, n%m)
# 求小和大的最大公约数
# 就去求小的和大的整除小的的余数的最大公约数

def gdc_naive(m, n):
    small = m if m < n else n
    for i in range(1, small + 1):
        if m%i == 0 and n%i == 0:
            gdc = i
    return gdc

def main():
    print(gdc(12, 100))
    print(gdc_naive(12, 100))

main()


