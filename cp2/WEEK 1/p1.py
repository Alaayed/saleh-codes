def virus_replication():
    s1,s2= input(),input()
    prefix = prefix_check(s1,s2)
    suffix = suffix_check(s1,s2)
    if prefix > suffix:
        return abs(len(s1)-len(s2))
    return max(0,suffix-prefix -1 - (len(s1) - len(s2)))

def prefix_check(s1,s2):
    for i in range(len(s1)):
        if i == len(s2) or s1[i] != s2[i]:
            return i -1
    return len(s1)-1
def suffix_check(s1,s2):
    for i in range(1, len(s1)+1):
        if (i == len(s2)+1) or s1[-i] != s2[-i] :
            return len(s1) - i + 1
    return 0
print(virus_replication())
