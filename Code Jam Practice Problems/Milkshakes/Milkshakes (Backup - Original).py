if __name__ == "__main__":

    # Open the input file
    inputfilename = input("Enter the name of the input file (include extensions): ")
    inputFile = open(inputfilename)
    inputContent = inputFile.read()
    inputFile.close()

    # Save the file contents to a list of data delimited by new lines
    dataList = inputContent.split("\n")
    count = 1  # Create a counter to help with list indexing

    # Determine the number of cases using the first line of the created list
    numberofcases = int(dataList[0])

    # Start writing to output file
    outputfilename = input("Enter the name of the output file (include extensions): ")
    outputFile = open(outputfilename, "w")

    # Apply algorithm per case
    for i in range(1, numberofcases+1):
        # Write case number in appropriate format
        outputFile.write("Case #"+str(i)+": ")

        # Gather data to be used
        n_flavors = int(dataList[count])
        count += 1

        m_customers = int(dataList[count])
        count += 1

        # import collections
        customerdictionary = {}  #collections.OrderedDict()
        flavordictionary = {}  #collections.OrderedDict()

        # Create a vector for each customer
        for customer in range(1, m_customers+1):
            #customerdictionaryindex = "Customer #" + str(customer)
            customerdictionary[customer] = [int(x) for x in dataList[count].split()]
            count += 1

        # Initiate flavor vectors
        for flavor in range(1, n_flavors+1):
            flavordictionary[flavor] = [0 for x in range(m_customers)]

        # Assign appropriate values to flavor vectors
        for customer in customerdictionary:
            print("Customer #"+str(customer))
            for j in range(1, len(customerdictionary[customer]),2):
                #print(customerdictionary[customer][j])
                #print(customerdictionary[customer][j+1])
                for k in flavordictionary.keys():
                    #print(flavordictionary[j])
                    if customerdictionary[customer][j] == k:
                        flavordictionary[k][customer-1] = customerdictionary[customer][j+1]
                    #print(flavordictionary[j][customer-1])

                    #print(flavordictionary[k])

        # Process flavor vectors









            # print(len(customerdictionary[customer]))
            # for j in range(1,len(customerdictionary[customer]),2):
            #     for k in range(1, n_flavors+1):
            #         #print(k)
            #         if customerdictionary[customer][j] == k:
            #             print(customerdictionary[customer][j])
            #             flavordictionary[k][j-1] = customerdictionary[customer][j+1]
            #             print(flavordictionary[k][j-1])
            #         else:
            #             flavordictionary[k][j-1] = flavordictionary[k][j-1]
            #             print(flavordictionary[k][j-1])
            #         #print(flavordictionary[k])

        print("Customers :", customerdictionary)
        print("Flavors :", flavordictionary,"\n")


        # for flavor in range(1, n_flavors+1):
        #     flavordictionaryindex = "Flavor #" + str(flavor)
        #     flavordictionary[flavordictionaryindex] = [
        #
        #         for j in range(1,n_flavors+1):
        #
        #             if
        #     ]

        #     for check in range(1, m_customers+1):
        #         if customerdictionary[check[flavor]] == flavor:
        #             flavorcounter += 1
        #         else:
