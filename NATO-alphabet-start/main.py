import pandas
nato=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato)
nato_values={row.letter:row.code for (index,row) in nato.iterrows()}
# print(nato_values)

def generate_phonetic():
    user_word= input("Please enter a word: ").upper()
    try:
        output_list=[nato_values[letter] for letter in user_word]

    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()