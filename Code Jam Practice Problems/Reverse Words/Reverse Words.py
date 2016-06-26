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
        words = [str(x) for x in dataList[count].split()]
        count += 1
        print(words)

        # Print words from list indexed backwards
        for j in range(len(words)-1,-1,-1):
            outputFile.write(words[j]+" ")

        # Write a new line for the entry of the next case
        outputFile.write("\n")

    print("Process complete.")
    outputFile.close()