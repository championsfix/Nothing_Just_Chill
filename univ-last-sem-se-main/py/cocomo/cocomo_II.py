x = int(input("Enter the number of Line of Codes:"))
kloc = (x/1000)
print("1. Product Attributes 2. Computer Attributes 3. Personnel Attributes 4. Project Attributes")
i = int(input("Select the Attribute:"))
if(i == 1):
    print("1. Required Software reliability 2. Database Size 3. Product Complexity ")
    j = int(input("Enter the value:"))
    if(j == 1):
        print("1. Very Low 2. Low 3. Nominal 4. High 5. Very High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 0.75
        elif(k == 2):
            EAF = 0.88
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 1.15
        elif(k == 5):
            EAF = 1.40
        else:
            print("Invalid Input")
    elif(j == 2):
        print("1. Low 2. Nominal 3. High 4. Very High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 0.94
        elif(k == 2):
            EAF = 1.00
        elif(k == 3):
            EAF = 1.08
        elif(k == 4):
            EAF = 1.16
        else:
            print("Invalid Input")
    elif(j == 3):
        print("1. Very Low 2. Low 3. Nominal 4. High 5. Very High 6. Extreme High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 0.70
        elif(k == 2):
            EAF = 0.85
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 1.15
        elif(k == 5):
            EAF = 1.30
        elif(k == 6):
            EAF = 1.65
        else:
            print("Invalid Input")
elif(i == 2):
    print("1. Execution time constraints 2. Main storage constraints 3. Virtual machine volitility 4. Computer turnaround time ")
    j = int(input("Enter the value:"))
    if(j == 1):
        print("1. Nominal 2. High 3. Very High 4. Extreme High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.00
        elif(k == 2):
            EAF = 1.11
        elif(k == 3):
            EAF = 1.30
        elif(k == 4):
            EAF = 1.66
        else:
            print("Invalid Input")
    elif(j == 2):
        print("1. Nominal 2. High 3. Very High 4. Extreme High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.00
        elif(k == 2):
            EAF = 1.06
        elif(k == 3):
            EAF = 1.21
        elif(k == 4):
            EAF = 1.56
        else:
            print("Invalid Input")
    elif(j == 3):
        print("1. Very Low 2. Low 3. Nominal 4. High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 0.87
        elif(k == 2):
            EAF = 1.00
        elif(k == 3):
            EAF = 1.15
        elif(k == 4):
            EAF = 1.30
        else:
            print("Invalid Input")
    elif(j == 4):
        print("1. Low 2. Nominal 3. High 4. Very High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 0.87
        elif(k == 2):
            EAF = 1.00
        elif(k == 3):
            Effort = 2.94 * EAF * (KSLOC)
            EAF = 1.07
        elif(k == 4):
            EAF = 1.15
        else:
            print("Invalid Input")
    elif(j == 5):
        print("Invalid Input")
elif(i == 3):
    print("1. Analyst capability 2. Applications experience 3. Programmer capability 4. Virtual macine experience 5. Programming language experience ")
    j = int(input("Enter the value:"))
    if(j == 1):
        print("1. Very Low 2. Low 3. Nominal 4. High 5. Very High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.46
        elif(k == 2):
            EAF = 1.19
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 0.86
        elif(k == 5):
            EAF = 0.71
        else:
            print("Invalid Input")
    elif(j == 2):
        print("1. Very Low 2. Low 3. Nominal 4. High 5. Very High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.29
        elif(k == 2):
            EAF = 1.13
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 0.91
        elif(k == 5):
            EAF = 0.82
        else:
            print("Invalid Input")
    elif(j == 3):
        print("1. Very Low 2. Low 3. Nominal 4. High 5. Very High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.42
        elif(k == 2):
            EAF = 1.17
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 0.86
        elif(k == 5):
            EAF = 0.70
        else:
            print("Invalid Input")
    elif(j == 4):
        print("1. Very Low 2. Low 3. Nominal 4. High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.21
        elif(k == 2):
            EAF = 1.10
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 0.90
        else:
            print("Invalid Input")
    elif(j == 5):
        print("1. Very Low 2. Low 3. Nominal 4. High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.14
        elif(k == 2):
            EAF = 1.07
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 0.95
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
elif(i == 4):
    print("1. Use of modern programming practices 2. Use of software tools 3. Required development schedule ")
    j = int(input("Enter the value:"))
    if(j == 1):
        print("1. Very Low 2. Low 3. Nominal 4. High 5. Very High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.24
        elif(k == 2):
            EAF = 1.10
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 0.91
        elif(k == 5):
            EAF = 0.82
        else:
            print("Invalid Input")
    elif(j == 2):
        print("1. Very Low 2. Low 3. Nominal 4. High 5. Very High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.24
        elif(k == 2):
            EAF = 1.10
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 0.91
        elif(k == 5):
            EAF = 0.83
        else:
            print("Invalid Input")
    elif(j == 3):
        print("1. Very Low 2. Low 3. Nominal 4. High 5. Very High ")
        k = int(input("Enter the value:"))
        if(k == 1):
            EAF = 1.23
        elif(k == 2):
            EAF = 1.08
        elif(k == 3):
            EAF = 1.00
        elif(k == 4):
            EAF = 1.04
        elif(k == 5):
            EAF = 1.10
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")

print("\n\nOrganic Mode:")
E = 3.2*(pow(kloc, 1.05))*EAF
tdev = 2.5*(pow(E, 0.38))
print("Organic Effort:", E, "Person Month")
print("Organic tdev:", tdev, "Months")
print("\n\nSemidetached Mode:")
E = 3.0*(pow(kloc, 1.12))*EAF
tdev = 2.5*(pow(E, 0.35))
print("Semidetached Effort:", E, "Person Month")
print("Semidetached tdev:", tdev, "Months")
print("\n\nEmbedded Mode:")
E = 2.8*(pow(kloc, 1.20))*EAF
tdev = 2.5*(pow(E, 0.32))
print("Embedded Effort:", E, "Person Month")
print("Embedded tdev:", tdev, "Months")
