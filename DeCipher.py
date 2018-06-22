import enchant
dictionary = enchant.Dict("en_US")

def deciph(cipher_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    # splitted phrases
    itr=0
    splitted_cipher = cipher_text.split(' ')
    for l in range(len(splitted_cipher)):
        key = 0
        decipher = ""
        while itr<26:
            splitted_cipher_character = list(splitted_cipher[l])
            for i in range(len(splitted_cipher_character)):
                pos = alphabet.find(splitted_cipher_character[i])
                newpos = (pos + key) % 26
                newchar = alphabet[newpos]
                splitted_cipher_character[i] = newchar

            # print(splitted_cipher_character)
            decipher = ''.join(map(str, splitted_cipher_character))
            if dictionary.check(decipher):
                # print(True)
                # print(decipher)
                # print("key: +" + str(key))
                result += " " + decipher
                break
            key += 1
            itr+=1
    return result,key

def main():
    while True:
        cipher_message = input("Enter the sceret code:")
        decipher_message,ans_key =deciph(cipher_message)
        print("Decipher:"+decipher_message+"\nKey:"+ str(ans_key))

main()