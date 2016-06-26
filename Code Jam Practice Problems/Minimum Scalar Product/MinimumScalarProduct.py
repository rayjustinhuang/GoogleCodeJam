if __name__ == "__main__":

    # Collect input data
    inputfilename = input("Enter the name of the input file (include extension): ")
    inputFile = open(inputfilename)
    inputContent = inputFile.read()
    inputFile.close()

    # Create a list from the input data delimited by new lines
    dataList = inputContent.split("\n")
    count = 1  # To aid in reading data from the dataList

    # The first line in the data is the number of cases
    numberofcases = int(dataList[0])

    # Begin writing to output file
    outputfilename = input("Enter the name of the output file (include extension): ")
    outputFile = open(outputfilename, "w")

    # Begin iteration per case
    for i in range(1, numberofcases+1):
        casenum = "Case #"+str(i)+": "
        outputFile.write(casenum)

        # Extract necessary information for this particular case
        n_integers = int(dataList[count])
        count += 1

        vector1 = [int(x) for x in dataList[count].split()]
        count += 1

        vector2 = [int(x) for x in dataList[count].split()]
        count += 1

        print(n_integers,"\n",vector1,"\n",vector2)

        candidate = 0
        for j in range(n_integers):
            min1 = min(vector1)
            max2 = max(vector2)
            candidate += min1*max2
            vector1.remove(min1)
            vector2.remove(max2)

        outputFile.write(str(candidate)+"\n")
        print(candidate)

    print("Process complete.")
    outputFile.close()