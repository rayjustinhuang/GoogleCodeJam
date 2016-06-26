if __name__ == "__main__":

    # Collect input data
    inputfilename = input("Enter input filename (include extensions): ")
    inputFile = open(inputfilename)
    inputContent = inputFile.read()
    inputFile.close()
    #print(inputContent)

    # Put data into a list
    dataList = inputContent.split("\n")
    #print(dataList)

    #Define T9 dictionary
    T9Code = {"a": 2, "b": 22, "c": 222, "d": 3, "e": 33, "f": 333,
         "g": 4, "h": 44, "i": 444, "j": 5, "k": 55, "l": 555,
         "m": 6, "n": 66, "o": 666, "p": 7, "q": 77, "r": 777,
         "s": 7777, "t": 8, "u": 88, "v": 888, "w": 9, "x": 99,
         "y": 999, "z": 9999, " ": 0}

    # Determine the number of test cases
    numberoftestcases = int(dataList[0]) # The first line of the file is the number of test cases

    # Start writing to output file
    outputfilename = input("Enter output filename (include extensions): ")
    outputFile = open(outputfilename, 'w')

    # Counter to help with reading the list of data
    count = 1

    # Iterate with algorithm per case
    for i in range(1, numberoftestcases + 1):
        # Print case number in prescribed output format
        casenum = "Case #" + str(i) + ": "
        print(str(casenum))
        outputFile.write(casenum)

        # Determine relevant case data for current iteration
        lines = list(dataList[count])
        count += 1
        print(lines)

        for word in range(len(lines)):
            if word == 0:
                outputFile.write(str(T9Code[lines[word]]))
            elif T9Code[lines[word-1]]%10 == T9Code[lines[word]]%10:
                outputFile.write(" "+str(T9Code[lines[word]]))
            else:
                outputFile.write(str(T9Code[lines[word]]))

        outputFile.write("\n")

    print("Process complete.")
    outputFile.close()
