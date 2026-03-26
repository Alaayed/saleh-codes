UPPER_BOUND = 1000000007
def inversions():
    line = input()
    qm, qmenc = line.count('?'), 0
    zc, zcenc = line.count('0'), 0
    p_qm= int(pow(2, qm , UPPER_BOUND))
    p_qm1= int(pow(2,qm-1, UPPER_BOUND))
    p_qm2= int(pow(2,qm-2, UPPER_BOUND))
    total_inversions = 0
    for i in range(0, len(line)):
            if line[i] == '1':
                qmpairs = qm-qmenc
                zcpairs = zc-zcenc
                total_inversions = (total_inversions + qmpairs * p_qm1 + zcpairs * p_qm) % UPPER_BOUND
            elif line[i] == '?':
                qmenc += 1
                qmpairs = qm-qmenc
                zcpairs = zc-zcenc
                total_inversions = (total_inversions + qmpairs * p_qm2 + zcpairs * p_qm1) % UPPER_BOUND
            elif line[i] == '0':
                zcenc += 1
    return int(total_inversions)
print(inversions())