import json

def change_value(file, index, key, value) :
    with open(file, 'r') as json_file :
        data_r = json.load(json_file)
        data_r[index][key] = value

    with open(file, 'w') as file :
        json.dump(data_r, file, indent=2)


def read_value(file, index, key) :
    with open(file) as json_file :
        login_data = json.load(json_file)

    return login_data[index][key]

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
    #Delete last two lines
    lines = lines_in_file(file)
    delete_line(file, lines-1)
    delete_line(file, lines-2)

    #Append data to it
    with open(file, "a") as myfile:
        myfile.write('''
    },
    {
        "username": "''' + value1 + '''",
        "pasword": "''' + value2 + '''"
    }
]
        ''')
