#Q1 -- Create a function that return the first name of anyone

def first_name():
    f_name = "Joe"
    return f_name

#Create a function that return the last name of anyone

def name_last():
    l_name = "Bobby"
    return l_name

#Create a function to concatenate the first and last name

def full_name():
    combined_name = first_name() +" " + name_last()
    message = (f"My full name is {combined_name}")
    return message

#print(full_name())


#Q2 Create a list of the below attributes
 
detail_list = ["first name", "last_name","date of birth"]

#Transform the name of the attributes
detail_first_name = "first name"
transformed_name = detail_first_name.replace(" ", "_")
#print(transformed_name) 

detail_dob = "date of birth"
transformed_date = detail_dob.replace(" ", "_")
#print(transformed_date)

detail_last_name = "last_name"

#Newly transformed list
final_list = [transformed_name, detail_last_name, transformed_date]
#print(final_list)


#Q3 Create a list with names 
names = ["Mayowa", "chizoba", "Chigozie"]

# Write a code to extract names that begins with capital letter and with a letter "a"

for name in names:
    if name[0].isupper():
        conversion = name.replace('Chigozie', 'Chigozia')
        new_list = []
        new_list.append(conversion)
        #print(new_list)


#Q4 Create a list with names from the marketing team

def name_check(name):
    """
    This function raises an excpetion when it encounters a string with an integer in a list
    
    Args:
        A list containing elements.
    
    Returns:  
        This function raises an exception
    """
    for nam in name:
        if nam.isalpha():
            return "Valid"
        else:
            raise ValueError (f"{nam} is a bad entry")    
    return name

entry_list= name_check(["A4atullah", "Wofia", "Zanaib"])

#print(entry_list)


#Q5 Build a generic function that will filter out bad entries and also accommodate yield.

def bad_entry(list_names):

    for name in list_names:
        if type(name) != str:
            yield name 

x = bad_entry([3, 4, "Victor", "Bola", 22, "Mayowa", 50])

#for i in x:
    #print(i)
