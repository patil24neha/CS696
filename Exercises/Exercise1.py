def hello():
    print("Hello World")
    return

def percent_decimal(i):
    if i==1:
        return 100
    elif i<1:
        return i*100
    else:
        return i/100

def exponent(integer, power):
    ans = 1
    if integer == 0 and power == 0:
        return 1
    elif integer == 0:
        return 0
    elif integer > 0 and power == 0:
        return 1
    elif integer > 0 and power > 0:
        for i in range(power):
            ans = integer * ans
        return ans

def complement(dna):
    ans = ""
    for j in dna:
        if j == 'G':
            j = 'C'
        elif j == 'C':
            j = 'G'
        elif j == 'T':
            j = 'A'
        else:
            j = 'T'
        ans += j

    return ans

hello();
ans = percent_decimal(0.45)
print(ans)
expans = exponent(3,2)
print(expans)
compans = complement("CTAGCGT")
print(compans)