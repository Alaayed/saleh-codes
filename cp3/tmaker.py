def solve():
    file_name = input()
    lines  =[]
    with open(file_name) as fd:
        for line in fd:
            line =repr(line.rstrip())[1:-1]
            line = '\"' + line +  '\"'
            lines.append(line)
            print(line)
    file_name +='body'
    with open(file_name, 'w') as fd:
        for line in lines:
            fd.write(line)
            fd.write(',\n')
    
solve()