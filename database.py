import json
from datetime import *


#TODO: Change before deployment
ENCRYPTION_KEY = 5
letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']


#Uses Ceaser Cipher. Only letters and numbers are encrypted
def encrypt(string) :
    encryption = ""
    global encrypted 
    encrypted = 0

    #Convert string to array
    string = [ch for ch in string]

    for i in range(0, len(string)):
        encrypted = 0
        for b in range(0, len(letters)) :
            if string[i] == letters[b] :
                if b+ENCRYPTION_KEY >= len(letters) :
                    encryption = encryption + letters[b-ENCRYPTION_KEY]
                else :
                    encryption = encryption + letters[b+ENCRYPTION_KEY]
                encrypted = 1
            b = b + 1

        if encrypted == 0:
            encryption = encryption + string[i]
        i = i + 1 
    return encryption


def decrypt(string) :
    decryption = ""
    global decrypted 
    decrypted = 0

    #Convert string to array
    string = [ch for ch in string]

    for i in range(0, len(string)):
        decrypted = 0
        for b in range(0, len(letters)) :
            if string[i] == letters[b] :
                if b+ENCRYPTION_KEY > len(letters) :
                    decryption = decryption + letters[b-ENCRYPTION_KEY]
                elif b+ENCRYPTION_KEY*2 >= len(letters) :
                    decryption = decryption + letters[b+ENCRYPTION_KEY]
                else :
                    decryption = decryption + letters[b-ENCRYPTION_KEY]
                decrypted = 1
            b = b + 1

        if decrypted == 0:
            decryption = decryption + string[i]
        i = i + 1 
    return decryption
    

def change_value(file, index, key, value) :
    key = encrypt(key)
    value = encrypt(value)
    with open(file, 'r') as json_file :
        data_r = json.load(json_file)
        data_r[index][key] = value

    with open(file, 'w') as file :
        json.dump(data_r, file, indent=2)


def read_value(file, index, key) :
    with open(file) as json_file :
        login_data = json.load(json_file)

    return decrypt(login_data[index][key])

def delete_line(file, line_number) :
    i = 0
    fn = file
    f = open(fn)
    output = ""

    #Read file and save it to output, missing out the line at line_number
    for line in f:
        if i != line_number:
            output = output + line
        i = i + 1
    f.close()

    #Write output to the file
    f = open(fn, 'w')
    f.writelines(output)
    f.close()

def lines_in_file(file):
    i = 0
    f = open(file)

    #count the lines in file
    for line in f:
        i = i + 1
    f.close()
    return i


def append_value(file, value1, value2) :
    value1 = encrypt(value1)
    value2 = encrypt(value2)
    #Delete last two lines
    lines = lines_in_file(file)
    delete_line(file, lines-1)
    delete_line(file, lines-2)

    #Append data to it
    with open(file, "a") as myfile:
        myfile.write('''    },
    {
        "username": "''' + value1 + '''",
        "password": "''' + value2 + '''"
    }
]''')


#I could have combined both arrays below into one but then when they are called it would be difficuly to know what each parameter does so I decided not to for the 
#Sake of simplicity and ease of use for other programmers
def get_study_length_today(file, username) :
    length_today = []

    #Get length of file
    with open(file) as json_file :
        length = len(json.load(json_file))

    for i in range(0, length) :
        if read_value(file, i, "username") == username: 
            if read_value(file, i, "password").split("%")[2] == str(date.today()):
                length = read_value(file, i, "password").split("%")[1]
                try :
                    length_today.append(int(length)/60)
                except:
                    length_today.append(length + " seconds")
        else :
            pass
    return length_today

def get_study_date_today(file, username) :
    length_today = []

    #Get length of file
    with open(file) as json_file :
        length = len(json.load(json_file))

    for i in range(0, length) :
        if read_value(file, i, "username") == username: 
            if read_value(file, i, "password").split("%")[2] == str(date.today()):
                length = read_value(file, i, "password").split("%")[2]
                length_today.append(length)
        else :
            pass
    return length_today

def get_study_time_today(file, username) :
    length_today = []

    #Get length of file
    with open(file) as json_file :
        length = len(json.load(json_file))

    for i in range(0, length) :
        if read_value(file, i, "username") == username: 
            if read_value(file, i, "password").split("%")[2] == str(date.today()):
                length = read_value(file, i, "password").split("%")[3]
                length_today.append(length)
        else :
            pass
    return length_today
        
def get_tags_today(file, username) :
    tags_today = []

    #Get length of file
    with open(file) as json_file :
        length = len(json.load(json_file))

    #For each item in file, if the usename is correct save the tag to tags_today
    for i in range(0, length) :
        if read_value(file, i, "username") == username: 
            if read_value(file, i, "password").split("%")[2] == str(date.today()):
                tag = read_value(file, i, "password").split("%")[0]
                if tag == "" :
                    tags_today.append("No tags") 
                else :
                    tags_today.append(tag)
        else :
            pass
    return tags_today


def get_total_time_spent_today (file, username) :
    #Get the array of all the time spent focusing today
    minutes_arr = get_study_length_today(file, username)
    minutes_string = 0  

    #Convert minutes_arr to string
    for i in range(0, len(minutes_arr)) :
        minutes_string = minutes_string + int(minutes_arr[i])
    return minutes_string


def get_most_productive_hour (file, username) :
    longest_time = 0

    #Get the array of all the time spent focusing today
    minutes_arr = get_study_length_today(file, username)
    #Get the array of all the times focused at today
    times_arr = get_study_time_today(file, username)

    for i in range(0, len(minutes_arr)) :
        if minutes_arr[i] > minutes_arr[longest_time] :
            longest_time = i

    return times_arr[longest_time]