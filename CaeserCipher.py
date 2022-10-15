
def CaeserCipher (word ):

    word = word.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dit = { alpha[i] : i  for i in range(len(alpha))}
    caeser_dit = {i :alpha[i] for i in range(len(alpha))}
    plain = [i for i in word.split()]
    cipher = ""
    for j in  plain :
        for i in j :
            val = dit[i] - 3
            val %= 26
            cipher += caeser_dit[val]
        cipher += "  "
    return cipher
if __name__ == "__main__" :
    inp = input("Enter the MESSAGE  that NEEDED to ENCRPTED in UPPERCASE:):):)")
    print("HERE IS YOUR MESSAGE :::>>>")
    print(CaeserCipher(inp))




