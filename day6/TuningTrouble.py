def checkUnique(str):
  for i in range(len(str)):
    for j in range(i + 1,len(str)):
      if(str[i] == str[j]):
        return False
  return True

if __name__ == '__main__':
    input = open('day6/input.txt', 'r').read().rstrip()

    for i in range(0, len(input) - 4):
        if checkUnique(input[i:i+4]):
            print('first package sequence after: ' + str(i + 4))
            break

    for i in range(0, len(input) - 14):
        if checkUnique(input[i:i+14]):
            print('first messege sequence after: ' + str(i + 14))
            break
