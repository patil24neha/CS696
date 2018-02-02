
def first_elements(my_list, n):
    return my_list[:n]

def last_element(my_list, n):
    return my_list[-n:]

def n_elements(my_list, start, n):
    end = start + n
    return my_list[start:end]

def count_letters(s):
    count_dict = {}
    for i in s:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

def protein_wight(protein):
    AMINO_ACID_WEIGHTS = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
                          'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
                          'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
                          'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06}

    total = 0
    for i in protein:
        total += AMINO_ACID_WEIGHTS[i]
    return total



firstlist = first_elements([0, 1, 2, 3], 2)
print(firstlist)

lastlist = last_element([0, 1, 2, 3], 2)
print(lastlist)

nlist = n_elements([0, 1, 2, 3, 4, 5],2, 3)
print(nlist)

count = count_letters("ABCDABSCDEFF")
print(count)

total = protein_wight("AC")
print(total)