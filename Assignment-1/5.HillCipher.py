## GOAL :
# Write a program that can encrypt and Decrypt using a 2 X 2 Hill Cipher

# =======================================
## By Shaurya Singhal - MCA-2ndYr-3rdSem
## Date: 20-10-2021
# =======================================


class HillCipher:

    # Helper function to convert ascii to character

    def getChar(self, ascii):
        return chr(ascii + 65)

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

        determinant = (keyMatrix[0][0] * keyMatrix[1][1]
                       - keyMatrix[0][1] * keyMatrix[1][0]) % 26
        return (keyMatrix, determinant)

    def getInverseKeyMatrix(self):

        # get Inverse of Key matrix , will be used in decryption
        # inverse of a 2X2 matrix
        #   | a , b |         | d  , -b|
        #   | c , d |  is     | -c , a|  whole divided by determinant

        inverse_key_matrix = [[0, 0], [0, 0]]

        for i in range(26):
            if self.determinant * i % 26 == 1:
                self.determinant = i
                break

        inverseKeyMatrix = [[self.keyMatrix[1][1] // self.determinant
                            % 26, -1 * self.keyMatrix[0][1]
                            // self.determinant % 26], [-1
                            * self.keyMatrix[1][0] // self.determinant
                            % 26, self.keyMatrix[0][0]
                            // self.determinant % 26]]

        return inverseKeyMatrix

    def __init__(self, key='SHAU'):
        self.key = key
        (self.keyMatrix, self.determinant) = self.getKeyMatrix()
        self.inverseKeyMatrix = self.getInverseKeyMatrix()

    def encrypt(self, text):
        if len(text) & 1:
            raise Exception('')

        encryptedtext = ''
        count = 0
        while count < len(text):
            vector = [ord(text[count]) - ord('A'), ord(text[count + 1])
                      - ord('A')]
            vector = [(self.keyMatrix[0][0] * vector[0]
                      + self.keyMatrix[0][1] * vector[1]) % 26,
                      (self.keyMatrix[1][0] * vector[0]
                      + self.keyMatrix[1][1] * vector[1]) % 26]
            cipher_text = [chr(vector[i] + ord('A')) for i in range(2)]
            encryptedtext += ''.join(cipher_text)
            count += 2
        return encryptedtext

    def decrypt(self, cipher):
        if len(cipher) & 1:
            raise Exception('')

        output = ''
        count = 0
        while count < len(cipher):
            vector = [ord(cipher[count]) - ord('A'), ord(cipher[count
                      + 1]) - ord('A')]
            count += 2
            vector = [(self.inverseKeyMatrix[0][0] * vector[0]
                      + self.inverseKeyMatrix[0][1] * vector[1]) % 26,
                      (self.inverseKeyMatrix[1][0] * vector[0]
                      + self.inverseKeyMatrix[1][1] * vector[1]) % 26]
            text = [chr(vector[i] + ord('A')) for i in range(2)]
            output += ''.join(text)
        return output


def main():

    hillCipher = HillCipher()

    print 'Enter the text to be decoded of even length: '
    text = input().replace(' ', '')

    # Encryption

    encryptedText = hillCipher.encrypt(text)
    print ('Encrypted Text: ', encryptedText)

    # Decryption

    decryptedText = hillCipher.decrypt(encryptedText)
    print ('Decrypted Text: ', decryptedText)


if __name__ == '__main__':
    main()
