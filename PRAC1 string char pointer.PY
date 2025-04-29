# write a java/c/c++/python program that contains a string (char pointer) with a value \Hello World'. The program should AND or and XOR 
# each character in this string with 127 and display the result

def main():
    original_string = "Hello World"
    print(f"Original string: {original_string}\n")
    print("Character | ASCII | AND with 127 | XOR with 127")
    print("-----------------------------------------------")
    for char in original_string:
        ascii_val = ord(char)
        and_result = ascii_val & 127
        xor_result = ascii_val ^ 127
        print(f"{char:9} | {ascii_val:5} | {and_result:12} | {xor_result:13}")
if __name__ == "__main__":
    main()
