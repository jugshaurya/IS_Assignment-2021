## GOAL :
# Write a program that can encrypt and Decrypt using a 2 X 2 Hill Cipher 

# =======================================
## By Shaurya Singhal - MCA-2ndYr-3rdSem
## Date: 20-10-2021
# =======================================

# Helper Function
def getChar(ascii):
    return chr(ascii + 65)

def HillCipher(text, key='SHAU'):

    # 1. Filling ascii values of text in 2 X 1 Matrix as text matrix

    textMatrix = []
    textMatrix.append([ord(text[0]) % 65])
    textMatrix.append([ord(text[1]) % 65])

    # 2. Filling ascii values of key in 2 X 2 Matrix as key matrix

    keyMatrix = []
    count = 0
    for i in range(2):
        subMat = []
        for j in range(2):
            subMat.append(ord(key[count]) % 65)
            count += 1
        keyMatrix.append(subMat)

    # 3. Generating Cipher Matrix
    #
    #   | a , b |     | e |
    #   |       |  X  |   |
    #   | c , d |     | f |
    #
    # # Result
    #   | a*b , e*f |
    #   |           |
    #   | c*e , d*f |
    #

    return ''.join([getChar((keyMatrix[0][0] * textMatrix[0][0]
                   + keyMatrix[0][1] * textMatrix[1][0]) % 26),
                   getChar((keyMatrix[1][0] * textMatrix[0][0]
                   + keyMatrix[1][1] * textMatrix[1][0]) % 26)])

def main():
    text = 'SI'
    output = HillCipher(text)
    print(output)


if __name__ == '__main__':
    main()
