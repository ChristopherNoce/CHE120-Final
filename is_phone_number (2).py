#Christopher Noce | 21143999

def is_kitchener_phone_number(phone_number): 

    """ 

    This function takes a string and determines whether or not that string corresponds to a Kitchener area phone number.  

    It must contain 519, 226, or 548 as the area code.  

    If the phone number is valid, it will return True, if not, it will return False.  
    
    Examples:
        Enter a phone number: 289-553-1364
        Is 289-553-1364 a valid Kitchener phone number?
        No, but it is still a valid Canadian number!
        
       Enter a phone number: 226-123-1324
       Is 226-123-1324 a valid Kitchener phone number?
       Yes, it is! 
       
       Enter a phone number: 123-1234-1324
       Is 123-1234-1324 a valid Kitchener phone number?
       No, invalid entry!
    """ 
   
    phone_number = phone_number.replace("-","") #because phone numbers are in the format 123-456-7890, I wanted to remove the dashes so I can just work with the numbers, making it much easier
    
    area_code = phone_number[0:3] #area code only stores the first three characters of phone_number. I did index 0-3 because it's not inclusive of the last in the range (only include 0, 1, 2 - first three)
    area_codes_kitchener = ['519', '226', '548'] #list of valid Kitchener area codes. Will use this to test if their area code is within the list.

    if len(phone_number) != 10:   # if the phone number is longer than 10 digits, it cannot be a Canadian phone number, making it invalid
        return None 
    elif not phone_number[0:10].isdigit(): # If it is 10 digits, it will go to this conditional. If all 10 characters (index 0:10 (10 not inclusive)) are digits, then it is a valid phone number. If someone enters abc-def-ghij, that is 10 characters, but they aren't all digits, so this conditional would return None.  
        return None 
    
    #If it is a valid Canadian phone number, it will proceed to this set of conditionals
    
    if area_code in area_codes_kitchener: #if the first 3 digits of their phone number matches with a valid Kitchener area code, it is a Kitchener phone number
        return True 
    elif area_code not in area_codes_kitchener:  #if the first 3 digits do not correspond to a Kitchener area code, it is Canadian but not from Kitchener.
        return False 

if __name__ =='__main__': #only runs when code is executed  
    phone_number = input("Enter a phone number: ") #asks user for input
    if is_kitchener_phone_number(phone_number) == True:
        print(f"Is {phone_number} a valid Kitchener phone number?\nYes, it is!\n",is_kitchener_phone_number(phone_number))
    elif is_kitchener_phone_number(phone_number) == False:
        print(f"Is {phone_number} a valid Kitchener phone number?\nNo, but it is still a valid Canadian number!\n",is_kitchener_phone_number(phone_number))
    else:
        print(f"Is {phone_number} a valid Kitchener phone number?\nNo, invalid entry!\n",is_kitchener_phone_number(phone_number))

        