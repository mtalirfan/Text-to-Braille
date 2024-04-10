import tkinter as tk
from time import sleep  # braille display changes after a set iteration time

from braille_dictionaries import (
    alphanumeric,
    punctuation,
    wordsigns,
    shortforms,
    contractions,
    groupsigns,
)  # dictionaries containing braille

br = [0, 0, 0, 0, 0, 0, 0]  # br[0] is unused, for better index handling

grade1 = False

grade1_input = input(
    "Default to Grade 2 Contracted Braille. Toggle to Grade 1 Uncontracted Braille? (y/n) "
)
if grade1_input.lower() in ["yes", "y"]:
    grade1 = True
else:
    grade1 = False


def display_braille(text):

    # A complex text as reference
    # ME-499 "Final-Year Project" (6CH) (90) (A)
    print(text)

    # for both grade 1 and 2
    # space out symbols and punctuation, convert spaces themselves to empty character ‎
    text_sym_spaced = ""
    for i in range(len(text)):
        if text[i] == " ":
            text_sym_spaced += f" ‎ "
        elif text[i] in punctuation.keys():
            text_sym_spaced += f" {text[i]} "
        else:
            text_sym_spaced += text[i]

    text_list_sym_spaced = text_sym_spaced.split()

    # spaced sym node
    # print(text_sym_spaced)
    # print(text_list_sym_spaced)

    if grade1 == True:  # grade 1
        brailled_text_num = ""
        for i in range(len(text_sym_spaced)):
            if (
                text_sym_spaced[i] in alphanumeric.keys()
                and text_sym_spaced[i].isdigit()
            ):  # number
                brailled_text_num += f" 001111 {alphanumeric.get(text_sym_spaced[i])} "  # numbers in dictionary don't have prefixes
            else:
                brailled_text_num += text_sym_spaced[i]

        # number node
        # print(brailled_text_num)

        brailled_text_punct = ""
        for i in range(len(brailled_text_num)):
            if brailled_text_num[i] in punctuation.keys():  # punctuation
                brailled_text_punct += punctuation.get(brailled_text_num[i])
            else:
                brailled_text_punct += brailled_text_num[i]

        # punctuation node
        # print(brailled_text_punct)

        brailled_text = ""
        for i in range(len(brailled_text_punct)):
            if (
                brailled_text_punct[i] in alphanumeric.keys()
                and brailled_text_punct[i].isalpha()
            ):  # letters, capital letters in dictionary have prefix
                brailled_text += alphanumeric.get(brailled_text_punct[i])
            elif (
                brailled_text_punct[i].isdigit() or brailled_text_punct[i] == " "
            ):  # number or whitespace
                brailled_text += brailled_text_punct[i]
            else:  # unrecognisable character
                brailled_text += " 000000 "

        brailled_list = brailled_text.split()

        # grade 1 brailled node
        # print(brailled_text)
        # print(brailled_list)

    else:  # grade 2

        # treat numbers first so we dont manipulate them later
        # numeric word first
        brailled_text_num_word = ""
        for i in range(len(text_list_sym_spaced)):
            if text_list_sym_spaced[i].isdigit():
                # print(text[i])
                # print(alphanumeric[f"{text[i]}"])
                brailled_text_num_word += f" 001111 {text_list_sym_spaced[i]} "
            else:
                brailled_text_num_word += f" {text_list_sym_spaced[i]} "

        text_list_num_word = brailled_text_num_word.split()

        # number word node
        # print(brailled_text_num_word)
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
                            f' 001111 {alphanumeric[f"{text_list_num_word[i][j]}"]} '
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
                                f' {alphanumeric[f"{text_list_num_word[i][j]}"]} '
                            )
                        else:
                            brailled_text_num += f"{text_list_num_word[i]}"

        text_list_num = brailled_text_num.split()

        # number node
        # print(brailled_text_num)
        # print(text_list_num)

        # treat symbols now, simple conversion to braille
        brailled_text_sym = ""
        for i in range(len(brailled_text_num)):
            if brailled_text_num[i] in punctuation.keys():
                # print(text[i])
                # print(alphanumeric[f"{text[i]}"])
                brailled_text_sym += punctuation[f"{brailled_text_num[i]}"]
            else:
                brailled_text_sym += brailled_text_num[i]

        text_list_sym = brailled_text_sym.split()

        # symbol node
        # print(brailled_text_sym)
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
        # print(brailled_text_caps_word)
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
        # print(brailled_text_caps)
        # print(text_list_caps)

        # Finally lowercase, changing to shorthand and then braille from dictionaries

        # wordsigns, only word check from wordsign dictionary
        # list words, item by item
        brailled_text_wordsigns = ""
        for i in range(len(text_list_caps)):
            if text_list_caps[i].isalpha() and text_list_caps[i] in wordsigns.keys():
                brailled_text_wordsigns += f" {wordsigns.get(text_list_caps[i])} "
            else:
                brailled_text_wordsigns += f" {text_list_caps[i]} "

        text_list_wordsigns = brailled_text_wordsigns.split()

        # wordsigns node
        # print(brailled_text_wordsigns)
        # print(text_list_wordsigns)

        # short forms dictionary
        # list words, item by item
        brailled_text_shortforms_word = ""
        for i in range(len(text_list_wordsigns)):
            if (
                text_list_wordsigns[i].isalpha()
                and text_list_wordsigns[i] in shortforms.keys()
            ):
                brailled_text_shortforms_word += (
                    f" {shortforms.get(text_list_wordsigns[i])} "
                )
            else:
                brailled_text_shortforms_word += f" {text_list_wordsigns[i]} "

        text_list_shortforms_word = brailled_text_shortforms_word.split()

        # shortforms word node
        # print(brailled_text_shortforms_word)
        # print(text_list_shortforms_word)

        # now shortforms substring check
        brailled_text_shortforms = ""
        for i in range(len(text_list_shortforms_word)):
            # if any of the keys is a substring of the larger string, a list element
            # iteration preference determined by elements in match list, which are determined by appearance order in dictionary
            matches = [
                x for x in shortforms.keys() if x in text_list_shortforms_word[i]
            ]
            # print(matches)
            if text_list_shortforms_word[i].isalpha() and matches:
                for j in range(len(matches)):
                    # iterate through the match list, replace all instances of the substring with spaced out, shortform substring
                    text_list_shortforms_word[i] = text_list_shortforms_word[i].replace(
                        f"{matches[j]}", f" {shortforms.get(matches[j])} "
                    )
                brailled_text_shortforms += text_list_shortforms_word[i]
            else:
                brailled_text_shortforms += f" {text_list_shortforms_word[i]} "

        text_list_shortforms = brailled_text_shortforms.split()

        # shortforms node
        # print(brailled_text_shortforms)
        # print(text_list_shortforms)

        # contractions dictionary
        # list words, item by item
        brailled_text_contractions_word = ""
        for i in range(len(text_list_shortforms)):
            if (
                text_list_shortforms[i].isalpha()
                and text_list_shortforms[i] in contractions.keys()
            ):
                brailled_text_contractions_word += (
                    f" {contractions.get(text_list_shortforms[i])} "
                )
            else:
                brailled_text_contractions_word += f" {text_list_shortforms[i]} "

        text_list_contractions_word = brailled_text_contractions_word.split()

        # contractions word node
        # print(brailled_text_contractions_word)
        # print(text_list_contractions_word)

        # now contractions substring check
        brailled_text_contractions = ""
        for i in range(len(text_list_contractions_word)):
            # if any of the keys is a substring of the larger string, a list element
            # iteration preference determined by elements in match list, which are determined by appearance order in dictionary
            matches = [
                x for x in contractions.keys() if x in text_list_contractions_word[i]
            ]
            # print(matches)
            if text_list_contractions_word[i].isalpha() and matches:
                for j in range(len(matches)):
                    # iterate through the match list, replace all instances of the substring with spaced out, shortform substring
                    text_list_contractions_word[i] = text_list_contractions_word[
                        i
                    ].replace(f"{matches[j]}", f" {contractions.get(matches[j])} ")
                brailled_text_contractions += text_list_contractions_word[i]
            else:
                brailled_text_contractions += f" {text_list_contractions_word[i]} "

        text_list_contractions = brailled_text_contractions.split()

        # contractions node
        # print(brailled_text_contractions)
        # print(text_list_contractions)

        # groupsigns dictionary
        # list words, item by item
        brailled_text_groupsigns_word = ""
        for i in range(len(text_list_contractions)):
            if (
                text_list_contractions[i].isalpha()
                and text_list_contractions[i] in groupsigns.keys()
            ):
                brailled_text_groupsigns_word += (
                    f" {groupsigns.get(text_list_contractions[i])} "
                )
            else:
                brailled_text_groupsigns_word += f" {text_list_contractions[i]} "

        text_list_groupsigns_word = brailled_text_groupsigns_word.split()

        # groupsigns word node
        # print(brailled_text_groupsigns_word)
        # print(text_list_groupsigns_word)

        # now groupsigns substring check
        brailled_text_groupsigns = ""
        for i in range(len(text_list_groupsigns_word)):
            # if any of the keys is a substring of the larger string, a list element
            # iteration preference determined by elements in match list, which are determined by appearance order in dictionary
            matches = [
                x for x in groupsigns.keys() if x in text_list_groupsigns_word[i]
            ]
            # print(matches)
            if text_list_groupsigns_word[i].isalpha() and matches:
                for j in range(len(matches)):
                    # iterate through the match list, replace all instances of the substring with spaced out, shortform substring
                    text_list_groupsigns_word[i] = text_list_groupsigns_word[i].replace(
                        f"{matches[j]}", f" {groupsigns.get(matches[j])} "
                    )
                brailled_text_groupsigns += text_list_groupsigns_word[i]
            else:
                brailled_text_groupsigns += f" {text_list_groupsigns_word[i]} "

        text_list_groupsigns = brailled_text_groupsigns.split()

        # groupsigns node
        # print(brailled_text_groupsigns)
        # print(text_list_groupsigns)

        # individual letter decompile
        brailled_text = ""
        for i in range(len(brailled_text_groupsigns)):
            if (  # letters in alphanumeric dictionary
                brailled_text_groupsigns[i] in alphanumeric.keys()
                and brailled_text_groupsigns[i].isalpha()
            ):
                brailled_text += alphanumeric.get(brailled_text_groupsigns[i])
            elif (  # 6 digit numbers and whitespace since whitespace don't hurt
                brailled_text_groupsigns[i].isdigit()
                or brailled_text_groupsigns[i] == " "
            ):
                brailled_text += brailled_text_groupsigns[i]
            else:  # any other unrecognisable character
                brailled_text += " 000000 "
        brailled_list = brailled_text.split()

        # symbol node
        # print(brailled_text)
        # print(brailled_list)

    # All braille node
    # print(brailled_text)
    # print(brailled_list)

    # Display brailled list
    for i in range(len(brailled_list)):  # each list element, a 6 digit code
        for j in range(len(brailled_list[i])):  # iterate through 6 digit code element
            br[j + 1] = brailled_list[i][j]

        print(
            f"""
        {br[1]} {br[4]}
        {br[2]} {br[5]}
        {br[3]} {br[6]}
        """
        )
        sleep(timer)


timer = 0  # 1 second between displays

# text = input("Enter the text you want to convert to Braille: ")
# display_braille(text)

display_braille("ME-499 Final-Year Project (6CH) (90) (A)")
