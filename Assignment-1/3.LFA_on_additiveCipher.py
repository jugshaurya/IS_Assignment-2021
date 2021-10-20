## GOAL : 
# - Write a program that can perform a letter frequency attack on an additive cipher without human intervention. 
# - Your software should produce possible plain text in rough order of likelihood. 
# - It would be good if your user interface allows user to specify "Give me top 10 possible plain texts"

# =======================================
## By Shaurya Singhal - MCA-2ndYr-3rdSem
## Date: 20-10-2021
# =======================================


# Letter frequency Attack on Additive Cipher (Ceaser Cypher)
# As `additiveCipher` is a subset of `Any monoalphabetc Substitution Cipher`, code is same as 4th question.

class LFA_ON_AC : 
    
    # string formed from most frequently occuring letters in decreasing order.
    # Ex. `E` is more frequent that `A` which is more in comparison to `C`
    DECIPHER_STRING = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    def __init__(self, cipher):
        self.cipher = cipher

    def getAscii(self,ch):
        return ord(ch) - 65

    def getChar(self, ascii):
        return chr(ascii + 65)

    def LFA(self, no_of_predictions = 10):
        
        # Calculating the frequency of letters in cipher
        freq = [0] * 26
        for i in range(len(self.cipher)):
            if self.cipher[i] != ' ':
                ascii = self.getAscii(self.cipher[i])
                freq[ascii] += 1
        
        # Sorting the frequency to get most frequent first
        sorted_freq = [None] * 26
        for i in range(26):
            sorted_freq[i] = freq[i]
        sorted_freq.sort(reverse = True)

        # find out the letter most frequent in cipher and is most frequent in decipher string
        used = [0] * 26
        outputs = [None] * no_of_predictions
        for prediction in range(no_of_predictions):
            idx = -1
            for letter in range(26):
                if sorted_freq[prediction] == freq[letter] and (not used[letter]):
                    used[letter] = 1
                    idx = letter
                    break
            if idx == -1:
                break

            # once we got the index `idx`, we can calculate shift
            shift = self.getAscii(LFA_ON_AC.DECIPHER_STRING[prediction])  - idx

            # geneate the string by shiftingthe letters of cipher and appending to the outputs.
            temp = ""
            for i in range(len(self.cipher)):
                if self.cipher[i] == ' ':
                    temp += " "
                    continue
                letterShift = (shift + self.getAscii(self.cipher[i])+ 26) % 26
                temp += self.getChar(letterShift)
            
            outputs[prediction] = temp
        
        return outputs;


def main():

    print("Enter the cipher: ")
    cipher = input()
    cipher = cipher.upper()

    outputs = LFA_ON_AC(cipher).LFA()
    print(*outputs, sep="\n")

if __name__ == "__main__":
    main()
