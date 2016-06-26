def minscalarprod(vector1, vector2):
    n_integers = len(vector1)
    candidate = 0
    for j in range(n_integers):
        min1 = min(vector1)
        max2 = max(vector2)
        candidate += min1 * max2
        vector1.remove(min1)
        vector2.remove(max2)
    return candidate

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
        print("Case #"+str(i)+": ")

        # Gather data to be used
        n_flavors = int(dataList[count])
        count += 1

        m_customers = int(dataList[count])
        count += 1

        #Initialize dictionaries to track customer preferences
        customerdictionary = {}
        flavordictionary = {}
        customerprefs = {}

        # Create a vector for each customer
        for customer in range(1, m_customers+1):
            customerdictionary[customer] = [int(x) for x in dataList[count].split()]
            count += 1

        # Initialize flavor vectors
        for flavor in range(1, n_flavors+1):
            flavordictionary[flavor] = [-1 for x in range(m_customers)]

        # Initialize customer preference vectors
        for customer in range(1, m_customers+1):
            customerprefs[customer] = [-1 for x in range(n_flavors)]

        # Assign appropriate values to flavor vectors
        for customer in customerdictionary:
            #print("Customer #"+str(customer))
            for j in range(1, len(customerdictionary[customer]),2):
                for k in flavordictionary.keys():
                    if customerdictionary[customer][j] == k:
                        flavordictionary[k][customer-1] = customerdictionary[customer][j+1]

        # Create customer preference vectors
        for flavor in flavordictionary:
            for customer in range(1, m_customers+1):
                customerprefs[customer][flavor-1] = flavordictionary[flavor][customer-1]

        # Number of preferences per customer
        numberofprefs = [0 for customer in range(m_customers)]

        for customer in range(1, m_customers+1):
            numberofprefs[customer-1] = customerprefs[customer].count(1) + customerprefs[customer].count(0)

        candidate = [0 for flavor in range(n_flavors)]
        satisfaction = [0 for customer in range(m_customers)]

        # NOT YET DONE: Need to find a way to change the candidate vector correctly
        for flavor in range(1, n_flavors + 1):
            # Check preferences and change candidate vector if needed
            for customer in range(sum(satisfaction) + 1, m_customers + 1):
                if customerprefs[customer][flavor-1] == 1 and numberofprefs[customer-1] == 1:
                    candidate[flavor-1] = 1
                    satisfaction[customer-1] = 1
                    break
                elif customerprefs[customer][flavor-1] == 0 and numberofprefs[customer-1] > 1:
                    candidate[flavor-1] = 0
                    satisfaction[customer-1] = 1
                elif customerprefs[customer][flavor-1] == 0:
                    candidate[flavor-1] = 0
                    satisfaction[customer-1] = 1
                    break
                elif customerprefs[customer][flavor-1] == 1 and numberofprefs[customer-1] > 1:
                    candidate[flavor-1] = 1
                    satisfaction[customer-1] = 1
                elif customerprefs[customer][flavor-1] == -1:
                    candidate[flavor-1] = 0
            print(candidate)

        for customer in customerprefs.keys():
            for flavor in range(n_flavors):
                if customerprefs[customer][flavor] == candidate[flavor]:
                    satisfaction[customer-1] = 1

        # Check if customers are satisfied
        if sum(satisfaction) == m_customers:
            outputFile.write(" ".join(str(x) for x in candidate))
            outputFile.write("\n")
        else:
            outputFile.write("IMPOSSIBLE\n")






        # print("Customers:", customerdictionary)
        # print("Flavors:", flavordictionary)
        print("Customer Preferences:", customerprefs)
        print("Number of Preferences:", numberofprefs)