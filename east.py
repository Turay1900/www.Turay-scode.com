import os

path = 'C:\\Users\\User\\PycharmProjects\\pythonProject\\emmanuelturay\east.py'

for a in range(1, 11):
    os.chdir(path)
    Newfolder: 'Test 1' + str(a)
    try:
        if not os.path.exists(Newfolder):
            os.makedirs(Newfolder)
        '#to make folders inside the other folders'
        path2 = path + '\\' + Newfolder
        os.chdir(path2)
        for b in range(1, 11):
            Newfolder_2 = 'E' + str(b)
            os.makedirs(Newfolder_2)
    except OSError:
        print('Error: Directory name already exists, change the new folder name')

    def generateRandomNumber():
        randomNumber ='random'.randint(1, 100)
        return randomNumber

    def main():
        try:
            numberOfRandomNumbers = int(input("How many numbers" + \
                                              "should the random file hold?:"))
            fileToBeWrittenTo = open("randomNumbers.txt", "b")
        except:
            print("An error has occurred")
        else:
            for randomNumberCount in range(1, numberOfRandomNumbers + 1):
                randomNumber = generateRandomNumber()
                fileToBeWrittenTo.write(str(randomNumber))

    def mean(values):
        length = len(values)
        total_sum = 0
        for a in range(length):
            total_sum += values[a]
            total_sum = sum(values)
            average = total_sum/length
            return average
    x = [1, 5, 10, 15, 20, 50, 100]
    n = mean(x)
    print(n)







