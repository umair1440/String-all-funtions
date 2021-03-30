                                            #  How to declear a string 

# In single Cuotation
name1='Umair'

# In double Cuotation
name2="Umair"

# In triple Cuotation
name3="'umair'"

                                                # String functions
# Captalize   Function: .captalize()
firstname = 'Umair'
print(firstname.capitalize())

# Check the string is Upper case or not. function: .isupper()
print(firstname.isupper())

# TO convert string in to lower case we have .lower() and casefold() fuctions 
print(firstname.casefold())
print(firstname.lower())

# To check the string is in lower case or not. function: .islower()
print(firstname.islower())

# if we want to print over string in center of the line we use function .center(amount)
print(firstname.center(100))

# for count the character from the string; funtion: .count("character that you want to count")
print(firstname.count("m"))

# check the last character of the string is the given character or not .endswith("r")
print(firstname.endswith("r"))

# check the first character of the string start with given character or not .startswith("U")
print(firstname.startswith("U"))

# find the number of the character from the give string .find("character that you want to find")
print(firstname.find("m"))

# find the format for the string
print(firstname.format())

# for check if the string is numeric form or not function .isnumeric()
print(firstname.isnumeric())

# for check if the string is identifie or not function .isidentifier()
print(firstname.isidentifier())

# for check if the string is in digit form or not function .isdigit()
print(firstname.isdigit())

# for check if the string is in printable form or not function .isprintable()
print(firstname.isprintable())

# for check if the all character in the string is white spaces or not function .isspace()
print(firstname.isspace())

# for check if the string is title or not function .istitle()
print(firstname.istitle())

# for adding character in string function .join("")
print(firstname.join("N"))

# for removing the black spaces from the string....   function:strip()
print(firstname.strip())

# for removing blank spaces from the left side of the string....  fucntion    .lstrip()
print(firstname.lstrip())

# for removing the black spaces of the right side of the string... function .rstrip()
print(firstname.rstrip())

# for replacing the character or letters from the string.....   function   .replace("for which you want to replace","for what you want to replace")
print(firstname.replace("Umair","r"))

# for finding the position of the character from the string.... fucntion .rfind("what you want to find")
print(firstname.rfind("U"))

# for spliting the string from any character from the string.... function .split("charater")
print(firstname.split("a"))


#                                                Functions completed

