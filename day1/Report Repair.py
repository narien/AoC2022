def sumCals(lines):
    cals = set()
    currCount = 0
    for val in lines:
        if val == '':
            cals.add(currCount)
            currCount = 0
            continue
        
        currCount += int(val)
    return cals

if __name__ == '__main__':
    input = r'C:\Users\Jakob\workspaces\AoC2022\day1\input.txt'
    with open(input) as f:
        lines = [val.strip() for val in f]
    cals = sumCals(lines)
    print('most calories is: ' + str(max(cals)))
    print('three most cals is: ' + str(sum(sorted(cals)[-3:])))