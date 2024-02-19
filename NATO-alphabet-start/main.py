import pandas
nato=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato)
nato_values={row.letter:row.code for (index,row) in nato.iterrows()}
# print(nato_values)
user_word= input("Please enter a word: ").upper()
output_list= [nato_values[letter]for letter in user_word]
print(output_list)
