## GOAL :
# Write a program that can encrypt and Decrypt using a 2 X 2 Hill Cipher 

# =======================================
## By Shaurya Singhal - MCA-2ndYr-3rdSem
## Date: 20-10-2021
# =======================================

class HillCipher:
    
    def __init__(self, key='SHAU'):
        self.key = key
        self.keyMatrix, self.determinant = getKeyMatrix()
        self.inverseKeyMatrix = getInverseKeyMatrix()
    
    # Task1. Filling ascii values of key in 2 X 2 Matrix as key matrix
    # Task2: calculating keymatrix determinant
    def getKeyMatrix(self):
        keyMatrix = []
        count = 0
        for i in range(2):
            subMat = []
            for j in range(2):
                subMat.append(ord(self.key[count]) % 65)
                count += 1
            keyMatrix.append(subMat)
        
        determinant = (keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0]) % 26
        return (keyMatrix, determinant)      

    # Helper function to convert ascii to character
    def getChar(self, ascii):
        return chr(ascii + 65)

    def getInverseKeyMatrix(self):
        # get Inverse of Key matrix , will be used in decryption
        # inverse of a 2X2 matrix
        #   | a , b |         | d  , -b|   
        #   | c , d |  is     | -c , a|  whole divided by determinant
        
        inverse_key_matrix=[[0,0],[0,0]]

        for i in range(26):
            if (self.determinant * i) % 26 == 1:
                self.determinant = i
                break

        inverseKeyMatrix = [[self.keyMatrix[1][1] // self.determinant % 26, -1 * self.keyMatrix[0][1] // self.determinant % 26],
                            [-1 * self.keyMatrix[1][0] // self.determinant % 26, self.keyMatrix[0][0] // self.determinant % 26]]
        
        return inverseKeyMatrix

    def encrypt(self, text):
        if(len(text) & 1 ):
            raise Exception("")
      
        encryptedtext  = ""
        count = 0
        while count < len(self.text):
            vector = [ord(self.text[count]) - ord('A') + 1, ord(self.text[count + 1]) - ord('A') + 1]
            vector = [(self.keyMatrix[0][0] * vector[0] + self.keyMatrix[0][1] * vector[1]) % 26,
                    (self.keyMatrix[1][0] * vector[0] + self.keyMatrix[1][1] * vector[1]) % 26]
            cipher_text = [chr(vector[i] + ord('A') - 1) for i in range(2)]
            encryptedtext  += ''.join(cipher_text)
            count += 2
        return encryptedtext 

    def decrypt(self,cipher):
        output = ""
        if len(cipher) % 2 != 0:
            cipher += "0"
        count = 0
        # decryption
        while count < len(cipher):
            vector = [ord(cipher[count]) - ord('A') + 1, ord(cipher[count + 1]) - ord('A') + 1]
            count += 2
            vector = [(self.inverseKeyMatrix[0][0] * vector[0] + self.inverseKeyMatrix[0][1] * vector[1]) % 26,
                    (self.inverseKeyMatrix[1][0] * vector[0] + self.inverseKeyMatrix[1][1] * vector[1]) % 26]
            text = [chr(vector[i] + ord('A') - 1) for i in range(2)]
            output += ''.join(text)
        return output

def main():


    print("Enter the text to be decoded of even length: ")
    text = input().replace(" ", "")

    hillCipher = HillCipher()

    # Encryption
    encryptedText = hillCipher.encrypt(text)
    print("Encrypted Text: ", encryptedText)

    # Decryption
    decryptedText = hillCipher.decrypt(encryptedText)
    print("Decrypted Text: ", decryptedText)


if __name__ == "__main__":
    main()
