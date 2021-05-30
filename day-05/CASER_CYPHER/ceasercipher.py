import caeser_cypher_logo

print(caeser_cypher_logo.logo)

def ceaser_cypher_encryption(text, cypher_shift, ch):
    text_list = []
    for c in text:
        text_list.append(c)
    factor = 1
    if ch == "encode":
        for i in range(len(text_list)):
            cur_val = ord(text_list[i])
            if cur_val + cypher_shift > 122:
                text_list[i] = chr(cur_val + cypher_shift - 26)
            else:
                text_list[i] = chr(cur_val + cypher_shift) 
    
    elif ch == "decode":
        for i in range(len(text_list)):
            cur_val = ord(text_list[i])
            if cur_val - cypher_shift < 97:
                text_list[i] = chr(cur_val - cypher_shift + 26)
            else:
                text_list[i] = chr(cur_val - cypher_shift) 
    
    else:
        print("ERROR: Wrong input !!")
        return       
    
    res = ""
    for ch in text_list:
        res += ch

    print(f"Encrypted text is : {res}")

exit = False
while not exit:
    choice = input("What do you want to perform (Encode/ Decode) : ").lower()
    text = input("Enter your code : ").lower()
    cypher_shift = int(input("Enter the shift number : "))
    ceaser_cypher_encryption(text=text, cypher_shift=cypher_shift, ch = choice)

    ex = input("Do you want to enter more (y/ n) : ").lower()
    if ex != 'y':
        print("Have a nice day.")
        exit = True
