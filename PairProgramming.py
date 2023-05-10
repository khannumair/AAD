a,b = '512','048'
if len(a) > len(b):
    maxLen = len(a)
    b = b.zfill(maxLen)
else: 
    maxLen = len(b)
    a = a.zfill(maxLen)
def add(a,b):
    result  = ''
    carry = 0
    for i in range (maxLen - 1, -1, -1):
        digitSum = int(a[i]) + int(b[i]) + carry
        if digitSum > 9:
            carry = 1
        else:
            carry = 0
        result = str(digitSum % 10) + result
    return result
sum = add(a,b)
print(a,'+',b,'=',sum)