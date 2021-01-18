def only_letters(string):
    specials = "'.-,´'"
    for letter in string:
        if(letter in specials):
            return False
    return True
        

read_file = open("Alle_danske_ord.txt", "r")
Lines = read_file.readlines()

write_file = open("fixed_danske_ord.txt", "w")

for line in Lines:
    if(line[0].islower() and only_letters(line)):
        write_file.write(line)

read_file.close()
write_file.close()
