import tkinter
from time import sleep  # braille display changes after a set iteration time

from braille_dictionaries import (
    alphanumeric_dic,
    punctuation_dic,
)  # dictionaries containing braille

br = [0, 0, 0, 0, 0, 0, 0]  # br[0] is unused, for better index handling

# grade1 = False
# grade1_input = input(
#     "Default to Grade 2 Contracted Braille. Toggle to Grade 1 Uncontracted Braille? (y/n) "
# )
# if grade1_input.lower() in ["yes", "y"]:
#     grade1 = True
# else:
#     grade1 = False


def display_braille(text):

    # A complex text as reference
    # ME-499 "Final-Year Project" (6CH) (90) (A)
    print(text)

    # for both grade 1 and 2
    # space out symbols and punctuation, convert spaces themselves to empty character ‎
    text_sym_spaced = ""
    text_list = text.split()
    for i in range(len(text)):
        if text[i] == " ":
            text_sym_spaced += f" ‎ "
        elif text[i] in punctuation_dic.keys():
            text_sym_spaced += f" {text[i]} "
        else:
            text_sym_spaced += text[i]

    text_list_sym_spaced = text_sym_spaced.split()

    # spaced sym node
    print(text_sym_spaced)
    # print(text_list_sym_spaced)

    # treat numbers first so we dont manipulate them later
    # numeric word first
    brailled_text_num_word = ""
    for i in range(len(text_list_sym_spaced)):
        if text_list_sym_spaced[i].isdigit():
            # print(text[i])
            # print(alphanumeric_dic[f"{text[i]}"])
            brailled_text_num_word += f" 001111 {text_list_sym_spaced[i]} "
        else:
            brailled_text_num_word += f" {text_list_sym_spaced[i]} "

    text_list_num_word = brailled_text_num_word.split()

    # number word node
    print(brailled_text_num_word)
    # print(text_list_num_word)

    # now number character by character
    brailled_text_num = ""
    for i in range(len(text_list_num_word)):
        if text_list_num_word[i] == "001111":  # number indicator from above
            brailled_text_num += f" {text_list_num_word[i]} "
        elif (text_list_num_word[i].isdigit() == False) and any(
            char.isdigit() for char in text_list_num_word[i]
        ):  # individual numbers when occur in mixture with other symbols
            for j in range(len(text_list_num_word[i])):
                if text_list_num_word[i][j].isdigit():
                    brailled_text_num += (
                        f' 001111 {alphanumeric_dic[f"{text_list_num_word[i][j]}"]} '
                    )
                else:
                    brailled_text_num += f"{text_list_num_word[i][j]}"
        else:  # word number char conversion without the indicator 001111
            if (
                any(char.isdigit() for char in text_list_num_word[i]) == False
            ):  # none of the characters are digits
                brailled_text_num += f" {text_list_num_word[i]} "
            else:
                for j in range(
                    len(text_list_num_word[i])
                ):  # iterate through individual characters if word numbers

                    if text_list_num_word[i][j].isdigit():
                        brailled_text_num += (
                            f' {alphanumeric_dic[f"{text_list_num_word[i][j]}"]} '
                        )
                    else:
                        brailled_text_num += f"{text_list_num_word[i]}"

    text_list_num = brailled_text_num.split()

    # number node
    print(brailled_text_num)
    # print(text_list_num)

    # treat symbols now, simple conversion to braille
    brailled_text_sym = ""
    for i in range(len(brailled_text_num)):
        if brailled_text_num[i] in punctuation_dic.keys():
            # print(text[i])
            # print(alphanumeric_dic[f"{text[i]}"])
            brailled_text_sym += punctuation_dic[f"{brailled_text_num[i]}"]
        else:
            brailled_text_sym += brailled_text_num[i]

    text_list_sym = brailled_text_sym.split()

    # symbol node
    print(brailled_text_sym)
    # print(text_list_sym)

    # treat capitals next, add 000001 before and convert to lower, will do shorthand conversion later

    # List item by item
    brailled_text_caps_word = ""
    for i in range(len(text_list_sym)):
        if text_list_sym[i].isupper() and len(text_list_sym[i]) != 1:
            brailled_text_caps_word += f" 000001 000001 {text_list_sym[i].lower()}"
        else:
            brailled_text_caps_word += f" {text_list_sym[i]} "

    text_list_caps_word = brailled_text_caps_word.split()

    # caps word node
    print(brailled_text_caps_word)
    # print(text_list_caps_word)

    # Character by character, better option is doing list item by list item first then char by char
    brailled_text_caps = ""
    for i in range(len(brailled_text_caps_word)):
        if brailled_text_caps_word[i].isupper():
            brailled_text_caps += f" 000001 {brailled_text_caps_word[i].lower()}"
        else:
            brailled_text_caps += brailled_text_caps_word[i]

    text_list_caps = brailled_text_caps.split()

    # caps node
    print(brailled_text_caps)
    # print(text_list_caps)

    # Original basic code for lowercases
    # brailled_text = text
    # text_list = list(brailled_text)
    # for i in range(len(text_list)):
    #     braille_code = alphanumeric_dic[f"{text_list[i]}"]
    #     braille_list = list(braille_code)

    #     print(braille_list)

    #     for j in range(len(braille_list)):
    #         br[j] = braille_list[j-1]

    #     print(
    #         f"""
    #     {br[1]} {br[4]}
    #     {br[2]} {br[5]}
    #     {br[3]} {br[6]}
    #     """
    #     )


text = input("Enter the text you want to convert to Braille: ")
display_braille(text)

# display_braille("ME-499 Final-Year Project (6CH) (90.50) (A)")
