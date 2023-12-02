DICT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

def find(line):
    index = []
    for num in DICT:
        count = 0
        number = ""
        while count < len(line):
            if line.find(num, count) == number:
                count += 1
                continue
            if line.find(num, count) != -1:
                index.append(line.find(num, count))
                number = line.find(num, count)
            count += 1
    index.sort()
    return index

def translate(index):
    for count, num in enumerate(index):
        for num2 in DICT:
            count2 = 0
            while count2 < len(line):
                if line.find(num2, count2) == num:
                    index[count] = DICT[num2]
                count2 += 1
    return index

def formatting(target):
    numbers = str(target[0]) + str(target[len(target)-1])
    return int(numbers)
    
def final(target):
    result = 0
    for i in target:
        result += i
    return result

result = []
with open('teste.txt', 'r') as file:
    for line in file:
        index = find(line)
        index = translate(index)
        result.append(formatting(index))

    print(final(result))

#resposta é 54634
#resposta 2 é 53855
