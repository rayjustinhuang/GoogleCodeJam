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
        casecredit = int(dataList[count])
        count += 1

        numberofitems = int(dataList[count])
        count += 1

        costofitems = [int(x) for x in dataList[count].split()]
        count += 1
        print(costofitems)

        # Condition to finding the correct case
        testCheck = False

        # Test by adding each item to other items until total cost is exactly equal to credit
        for j in range(len(costofitems)-1):
            if testCheck:
                break
            else:
                for k in range(j+1,len(costofitems)):
                    if((costofitems[j] + costofitems[k]) == casecredit):
                        outputFile.write(str(j+1) + " " + str(k+1) + "\n")
                        testCheck = True
                        break

    print("Process complete.")
    outputFile.close()

