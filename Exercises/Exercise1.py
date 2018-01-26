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
    if integer == 0 and power == 0:
        return 1
    elif integer == 0:
        return 0
    elif integer > 0 and power == 0:
        return 1
    elif integer > 0 and power > 0:
        for power in range(power + 1):
            ans = integer ** power
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
expans = exponent(4,3)
print(expans)
compans = complement("CTAGCGT")
print(compans)