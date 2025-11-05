from string import ascii_letters, ascii_lowercase

def convert_decimal_to_binary(num:int):
    return apply_length(bin(num).replace("0b",""))
    
def convert_binary_to_decimal(binary_string:str):
    total = 0
    current_multiple = 1
    for bit in binary_string[::-1]:
        if bit == "1":
            total += current_multiple
        current_multiple *= 2
        
    return total

def apply_length(binary_code:str):
    new_binary_code = binary_code
    length = len(binary_code)
    for _ in range(8-length):
        new_binary_code = "0" + new_binary_code

    return new_binary_code

def apply_xor_to_string(binary1:str,binary2:str):
    final_binary_string = ""
    for i in range(len(binary1)):
        final_binary_string += apply_xor(int(binary1[i]),int(binary2[i]))
    
    return final_binary_string

def apply_xor(bit1:int,bit2:int):
    if (bit1 == 1 or bit2 == 1) and not (bit1 == 1 and bit2 == 1):
        return "1"
    return "0"

def extract_file_data():
    with open("Euler 1-100\Euler 51-100\Euler 51-60\Euler59.txt","r") as file:
        file_data = file.readlines()[0].split(",")
        file_data = map(int,file_data)
        return list(file_data)
    
def apply_list_seperation(given_list:list):
    #seperating the list into 3 for each mini key inside the key
    list_length = len(given_list)
    key1_list,key2_list,key3_list = [],[],[]
    
    for i in range(list_length//3):
        key1_list.append(given_list[3*i])
        key2_list.append(given_list[3*i+1])
        key3_list.append(given_list[3*i+2])
    
    if list_length%3 >= 1:
        key1_list.append(given_list[-1])
        if list_length%3 == 2:
            key2_list.append(given_list[-2])
    
    return key1_list,key2_list,key3_list    

def apply_string_combination(string1,string2,string3):
    total_length = len(string1 + string2 + string3)
    final_string = ""
    for i in range(total_length):
        if i % 3 == 0:
            final_string += string1[i//3]
        elif i % 3 == 1:
            final_string += string2[i//3]
        else:
            final_string += string3[i//3]
    
    return final_string

def apply_key_to_encryption(encryted_list:list[str]):
    decoded_strings = {}
    for key in ascii_lowercase:
        binary_key = convert_decimal_to_binary(ord(key))
        decoded_string = ""
        condition = True
        
        for encoded_binary in encryted_list:
            decoded_binary = apply_xor_to_string(binary_key,encoded_binary)
            decoded_ascii = chr(convert_binary_to_decimal(decoded_binary))
            
            # if decoded_ascii not in ascii_letters:
            #     condition = False
                
            decoded_string += decoded_ascii

        decoded_strings[key] = decoded_string
            
    return decoded_strings
            

def main():
    coded_decimal_list = extract_file_data()
    coded_binary_list = list(map(convert_decimal_to_binary,coded_decimal_list))
    text_length = len(coded_binary_list)
    
    key1_list,key2_list,key3_list = apply_list_seperation(coded_binary_list)
    
    key1_strings_dict = apply_key_to_encryption(key1_list)
    key2_strings_dict = apply_key_to_encryption(key2_list)
    key3_strings_dict = apply_key_to_encryption(key3_list)
    
    for key1,string1 in key1_strings_dict.items():
        for key2,string2 in key2_strings_dict.items():
            for key3,string3 in key3_strings_dict.items():
                final_string = apply_string_combination(string1,string2,string3)
                
                if "Euler" in final_string:
                    print(final_string)
                    ascii_sum = 0
                    for character in final_string:
                        ascii_sum += ord(character)
                    print(ascii_sum)
        
                                                
if __name__ == "__main__":
    main()