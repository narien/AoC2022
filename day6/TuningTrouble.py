def checkUnique(str):
  for i in range(len(str)):
    for j in range(i + 1,len(str)):
      if(str[i] == str[j]):
        return False
  return True

def findSequence(type, input, length):
    for i in range(0, len(input) - length):
        if checkUnique(input[i:i + length]):
            print('first ' + type + ' sequence after: ' + str(i + length))
            return

if __name__ == '__main__':
    input = open('day6/input.txt', 'r').read().rstrip()

    findSequence('package', input, 4)
    findSequence('message', input, 14)
