def findSequence(type, input, length):
    for i in range(0, len(input) - length):
        if len(set(input[i:i + length])) == length:
            print('first ' + type + ' sequence after: ' + str(i + length))
            return

if __name__ == '__main__':
    input = open('day6/input.txt', 'r').read().rstrip()

    findSequence('package', input, 4)
    findSequence('message', input, 14)
