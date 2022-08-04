from lib2to3.pytree import convert
import random


while (True):
    ceaser =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    offset = 0
    split = ""
    encrypted = ""
    overlap = 0
    mode = ""
    print("Mode?")
    print("(e)ncrypt, (d)ecrypt")
    
    mode = input()
    if mode == "e":
        print("Decrypted message?")
        decrypted = input()
        print("Offset?")
        offset = int(input())
        decrypted = decrypted.lower()
        for i in decrypted:
            split = i
            x = 0
            while x < len(ceaser):
                if split == ceaser[x]:
                    if (x + offset > 25):
                        overlap = offset
                        offset = -x
                        offset + overlap
                    encrypted += ceaser[x + offset]
                x += 1
        print(encrypted)
        print(offset)
    if mode == "d":
        print("Encrypted message?")
        decrypted = input()
        print("Offset?")
        offset = int(input())
        decrypted = decrypted.lower()
        for i in decrypted:
            split = i
            x = 0
            while x < len(ceaser):
                if split == ceaser[x]:
                    if (x - offset < 0):
                        overlap = -offset
                        offset = 25
                        offset = offset + overlap
                        encrypted += ceaser[offset + 1]
                    else:
                        encrypted += ceaser[x - offset]
                x += 1
        print(encrypted)