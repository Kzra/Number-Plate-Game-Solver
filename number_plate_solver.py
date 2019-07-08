#Setup Environment
import json
process = True

with open('words_dictionary.json', 'r') as f:
     datastore = json.load(f)

def find_character(s,x):
    character = [pos for pos, char in enumerate(s) if char == x]
    return character

def validity_test(val_list):
    valid = False
    if [] in val_list or len(val_list) != 3: 
        return valid
    first_letter_idx = val_list[0][0]
    last_letter_idx = val_list[2][len(val_list[2])-1]
    #if there is an instance of the middle character (mlidx), that doesn't touch either letter, than the word is valid
    for mlidx in val_list[1]:
        if mlidx - first_letter_idx > 1 and last_letter_idx - mlidx > 1: 
            valid = True
    return valid


#Begin Script
while process == True:
    
    print('Welcome to the Number Plate Solver. Press CTRL-C or type \'exit\' to exit.')
    entries = 0 
    
    three_letters = list(str(input('Type in the last three letters of the number plate (e.g\'GCY\') ')).lower())
    if three_letters == list('exit'): process = False; break
    if len(three_letters) != 3: print('Invalid Entry'); continue


    for key in datastore: 
            val_list = [find_character(key,x) for x in three_letters if x in key]
            if validity_test(val_list): print('\n',key); entries += 1 

    print('\nfinished searching! there were ',entries,' results.''\n')