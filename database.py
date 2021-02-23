import json


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
                if b+ENCRYPTION_KEY > len(letters) :
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
                elif b+ENCRYPTION_KEY*2 > len(letters) :
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

print (encrypt("JaneLovesCats123!"))