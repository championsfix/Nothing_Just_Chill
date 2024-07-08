import math
def Halstead(n1,n2,N1,N2):
    N = N1+N2
    n = n1+n2
    program_volume = N * math.log(n,2)
    program_level=N*n1/n2*N1
    D=(n1/2)*(N2/2)
    program_Effort=D*program_volume
    program_Time=program_Effort/(60*18)
    print(f"--OUTPUT--")
    print(f"Unique operator used: {n1}")
    print(f"Unique operands used: {n2}")
    print(f"Total operands used: {N1}")
    print(f"Total operator used: {N2}")
    print(f"Value of N: {N}")
    print(f"Value of n: {n}")
    print(f"Program volume: {program_volume}")
    print(f"Program Level:{program_level}")
    print(f"Program Effort:{program_Effort}")
    print(f"Program Level:{program_Time}")

   
if __name__ == '__main__':
    n1 = int(input("Enter the num of unique operator: "))
    n2 = int(input("Enter the num of unique operands: "))
    N1 = int(input("Enter the total num of operator: "))
    N2 = int(input("Enter the total num of operand: "))
    Halstead(n1,n2,N1,N2)
