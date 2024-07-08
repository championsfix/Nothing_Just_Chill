'''WAP in python to find the program volume, program level,Effort and time using Halstead technique in the dynamic way'''
import sys
import math

n1=0 #unique no.of operators
n2=0 #unique no.of operands
N1=0 #total no.of operators
N2=0 #total no.of operands
s = "([ . -> * + - ~ ! ++ -- / % - << >> < > <= >= != == & ^ | && || = *= /= %= += -= <<= >>= &= ^= |= : ? { ; auto break case char const continue default do double else enum extern float for goto if int long main printf register return scanf short signed sizeof static struct  string switch typedef union unsigned void volatile while"

operators = ['<', '>', '=','!','&','|','^','+','-','*','/','\0']
halstead_operators = s.split()
separators = [',', ';', ':',')','(','{','}','[',']','"','\0']
keywords = ["auto", "break" ,"case","char","const","continue","default","do","double","else","enum","extern","float","for", "goto","if","int", "long","main","printf","scanf","register","return","short","signed","sizeof","static","struct","switch","typedef", "union","unsigned","void","volatile","while","string"]
f = open(sys.argv[1],'r')
code = f.read()
st = 0
tokens = []
temp = []
unique_operands = []
i=0
# split the input code into tokens
while i<len(code):
  
    if i+1==len(code) or code[i]==' ' or code[i]=='\n' or code[i]=='\t' or (code[i] in operators) or (code[i] in separators):
        temp.clear()
        if code[i]=='"':
            st = i+1
            # k = i
            while code[st]!='"':
                temp.append(code[st])
                st += 1
                # k += 1
            st +=1
            i=st
        while st<i:
            temp.append(code[st])
            st+=1
        print(temp)
        st =i+1
        if len(temp)>0:tokens.append("".join(temp))
    if (code[i] in halstead_operators):
        # print(code[i])
        tokens.append("".join(code[i]))
        
    i+=1

# count the total no.of operators and operands
for i in range(len(tokens)):
    if (tokens[i] in halstead_operators): 
        # print(tokens[i])
        N1 +=1
    else:
        unique_operands.append(tokens[i])
        N2 +=1

for i in range(len(halstead_operators)):
    if halstead_operators[i] in tokens:
        n1+=1

unique_operands = list(set(unique_operands))
n2 = len(unique_operands)
print()
print("Unique No.Of Operators(n1): ",n1)
print("Total no.of operators(N1): ",N1)
print("Unique No.Of Operators(n2): ",n2)
print("Total no.of Operands(N2): ",N2)

N = N1 + N2 #Program Length
n = n1 + n2 #Program Vocabulary
V = N * math.log2(n) #Program Volume
V1 = (2 + n2)*math.log2(2+n2) #Potential Minimum Volume
L = V1/V #Program Level
E = V/L #Effort
T = E/18 

print()
print("Length(N): ",N)
print("Vocabulary(n): ",n)
print("Volume: ",V)
print("Program Level: ",L)
print("Effort: ",E)
print("Time: ",T)
