import re

landline_check = re.compile(r'^(11|12|120|124)')    # Various STD codes for landline in India: (011,012,0120,0124)
mobile_check = re.compile(r'^(\+91)')               # Country code for India: +91 (National)
remove_chars = re.compile(r'^0|\s|-')               # For trailing 0 at the start, white space characters and '-'

# To check valid Phone Number fields
def is_phone_field(field):
    if field in ["contact:mobile", "contact:phone", "phone"]:
        return True
    else:
        return False

character_check = re.compile(r'[,*;/]')  # Pattern match to extract multiple numbers from same string
def find_char_split(string):
    if len(character_check.split(string, maxsplit=1)) > 1:  # Less than 1 signifies no split and hence no character found in string
        my_strings = character_check.split(string, maxsplit=1)
    else:
        my_strings = False
    return my_strings

def phone_format(ten_digit_number_as_string):
    ##According to National Numbering Plan 2003: +91 XXXX NNNNNN
    return "+91 "+ten_digit_number_as_string[0:4]+" "+ten_digit_number_as_string[4:]

# Various checks and subsequent conversion to +91 XXXX NNNNNN format
def convert_to_mobile(temp):
    # For checking multiple numbers separated by delimiter
    multiple_nums = find_char_split(temp)

    if len(temp) == 10 and temp[0] in ["6","7","8","9"]:    # Basic Format (XXXXNNNNNN)
        correct = phone_format(temp)

    elif len(temp) > 10 and re.search(r'^([91]|[+9111])',temp) is not None:  # In the form of +91-11-XXXX-NNNNNN or 91-XXXX-NNNNNN
        temp = re.sub(r'^([91]|[+9111])',"",temp)
        correct = phone_format(temp)

    elif multiple_nums != False and find_char_split(multiple_nums[1]) == False:         # Multiple numbers in a single string, with only a single split. Multiple splits treated as ambiguous
        if len(multiple_nums[0]) == 10 and multiple_nums[0][0] in ["6","7","8","9"]:    # Checking basic format
            change = len(multiple_nums[1])
            temp_alt = multiple_nums[0][0:-change] + multiple_nums[1]
            alt_number = phone_format(temp_alt)
            main_number = phone_format(multiple_nums[0])
            correct = main_number+","+alt_number
        else:
            #print("Ambiguity in split => "+temp)
            correct =  False                                # Return False as indication for no change
    else:
        #print("Defaulter => "+temp)
        correct = False                                     # Return False as indication for no change

    return correct



## MAIN FUNCTION BEING CALLED
def correct_number_format(number):
    # Only correcting Mobile numbers due to a lot of discrepancies in landline numbers

    number_new = ""
    temp = remove_chars.sub("", number)

    if landline_check.search(temp) is not None:
        #number_new = convert_to_landline(temp)
        number_new = False                                # Return False as indication for no change

    elif mobile_check.search(temp) is not None or re.search(r'^[6-9]\d{9}$', temp) is not None:     # If no country code or STD code is added, just 10 digit number
        temp = mobile_check.sub("", temp)
        if landline_check.search(temp) is None:           # Corrected string should'nt be  a landline number
            number_new = convert_to_mobile(temp)
        else:
            ##number_new = convert_to_landline(temp)
            number_new = False                            # Return False as indication for no change
    else:
        #print("Issue in 1st Level => "+temp)
        number_new = False                                # Return False as indication for no change

    if number_new != False:
        return number_new
    else:
        return number

#############################################################################################
# Not being used presently, for future purposes
def convert_to_landline(number):
    correct_landline = ""
    if number[0:2] == "11":
        #Delhi STD Code : 11
        if len(number[2:]) == 8:
            temp = number[2:]
            correct_landline = "+91 "+"11 "+temp[0:4]+" "+temp[4:]
    elif number[0:3] in ["120", "124"]:
        ##Noida: 120, Gurgaon :124
        if len(number[3:]) == 7:
            correct_landline = "+91 " +number[0:3]+ " " + number[3:6] + " " + number[6:]
    else:
        correct_landline = number

    #return correct_landline
###############################################################################################