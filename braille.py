import tkinter
from time import sleep  # braille display changes after a set iteration time

from braille_dictionaries import (
    alphanumeric_dic,
    punctuation_dic,
)  # dictionaries containing braille

br = [0, 0, 0, 0, 0, 0, 0]  # br[0] is unused, for better index handling


def display_braille(text):

    # treat numbers first so we dont manipulate them later, simple conversion to braille
    brailled_text_num = ""
    for i in range(len(text)):
        if text[i].isdigit():
            # print(text[i])
            # print(alphanumeric_dic[f"{text[i]}"])
            brailled_text_num += alphanumeric_dic[f"{text[i]}"]
        else:
            brailled_text_num += text[i]

    text_list_num = brailled_text_num.split()

    # number node
    print(brailled_text_num)
    print(text_list_num)

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
    print(text_list_sym)

    # treat capitals next, add 000001 before and convert to lower, will do shorthand conversion later

    # List item by item
    brailled_text_caps_word = ""
    for i in range(len(text_list_sym)):
        if text_list_sym[i].isupper():
            brailled_text_caps_word += f" 000001 000001 {text_list_sym[i].lower()}"
        else:
            brailled_text_caps_word += f" {text_list_sym[i]} "

    text_list_caps_word = brailled_text_caps_word.split()

    # caps word node
    print(brailled_text_caps_word)
    print(text_list_caps_word)

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
    print(text_list_caps)

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
