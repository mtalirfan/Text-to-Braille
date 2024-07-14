from time import sleep  # braille display changes after a set iteration time

from braille_dictionaries import (
    unicode,
    alphanumeric,
    punctuation,
    wordsigns,
    shortforms,
    contractions,
    groupsigns,
    groupsigns_final,
)  # dictionaries containing braille

br = [0, 0, 0, 0, 0, 0, 0]  # br[0] is unused, for better index handling

grade1 = False  # grade 1 or 2
timer = 0  # seconds between displays


def toggle_grade():
    """Toggle between Grade 1 and Grade 2 Braille. Default to Grade 2 Contracted Braille."""

    global grade1
    grade1_input = input(
        "Default to Grade 2 Contracted Braille. Toggle to Grade 1 Uncontracted Braille? (y/n): "
    )
    if grade1_input.lower() in ["yes", "y"]:
        grade1 = True
    else:
        grade1 = False


def space_out_symbols_punctuation(text):
    """space out symbols and punctuation, convert spaces to empty character ‎"""

    # print(text)

    text_sym_spaced = ""
    for i in range(len(text)):
        if text[i] == " ":
            text_sym_spaced += f" ‎ "
        elif text[i] in punctuation.keys():
            text_sym_spaced += f" {text[i]} "
        else:
            text_sym_spaced += text[i]

    # count all double quotations to replace for opening and closing
    quotation_count = text_sym_spaced.count('"')
    # print(quotation_count)

    # 2 = set nth substrings of "foo" to be replaced
    # Replace nth subs in super string
    for n in range(2, quotation_count + 2, 2)[::-1]:
        text_sym_spaced = text_sym_spaced.replace('"', "”", n).replace(
            "”", '"', n - 1
        )  # replace every 2nd with closing quotation
        # print(n, n - 1, text_sym_spaced)

    text_sym_spaced = text_sym_spaced.replace(
        '"', "“"
    )  # replace the rest with opening quotation

    # spaced symbols node
    # print(text_sym_spaced)

    return text_sym_spaced


def space_out_alphanumeric(text_sym_spaced):
    """space out mixed alphanumeric strings"""
    text_list_sym_spaced = text_sym_spaced.split()

    text_alphanumeric_spaced = ""
    for i in range(len(text_sym_spaced)):
        if i < (len(text_sym_spaced) - 1):
            if (
                # character is digit, next is letter OR character is letter, next is digit
                (text_sym_spaced[i].isdigit() and text_sym_spaced[i + 1].isalpha())
                or (text_sym_spaced[i].isalpha() and text_sym_spaced[i + 1].isdigit())
                # # both are letters, first is lower, next is upper
                # or (
                #     (text_sym_spaced[i].isalpha() and text_sym_spaced[i].islower())
                #     and (
                #         text_sym_spaced[i + 1].isalpha()
                #         and text_sym_spaced[i + 1].isupper()
                #     )
                # )
                # # both are letters, first is upper, next is lower
                # or (
                #     (text_sym_spaced[i].isalpha() and text_sym_spaced[i].isupper())
                #     and (
                #         text_sym_spaced[i + 1].isalpha()
                #         and text_sym_spaced[i + 1].islower()
                #     )
                # )
            ):
                text_alphanumeric_spaced += f"{text_sym_spaced[i]} "
            else:
                text_alphanumeric_spaced += text_sym_spaced[i]
        else:
            text_alphanumeric_spaced += text_sym_spaced[i]

    # spaced symbols node
    # print(text_alphanumeric_spaced)

    return text_alphanumeric_spaced


def convert_numeric_word(text_alphanumeric_spaced):
    """treat numbers first so we dont manipulate them later"""

    text_list_alphanumeric_spaced = text_alphanumeric_spaced.split()

    # numeric word first
    brailled_text_num_word = ""
    for i in range(len(text_list_alphanumeric_spaced)):
        if text_list_alphanumeric_spaced[i].isdigit():
            brailled_text_num_word += f" 001111 {text_list_alphanumeric_spaced[i]} "
        else:
            brailled_text_num_word += f" {text_list_alphanumeric_spaced[i]} "

    # number word node
    # print(brailled_text_num_word)

    return brailled_text_num_word


def convert_numeric_character(brailled_text_num_word):
    """treat numbers character by character"""

    text_list_num_word = brailled_text_num_word.split()

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

    # number node
    # print(brailled_text_num)

    return brailled_text_num


def convert_symbols_punctuation(brailled_text_num):
    """treat symbols/punctuation now, simple conversion to braille"""

    text_list_num = brailled_text_num.split()

    # treat symbols/punctuation now, simple conversion to braille
    brailled_text_sym = ""
    for i in range(len(brailled_text_num)):
        if brailled_text_num[i] in punctuation.keys():
            # print(text[i])
            # print(alphanumeric[f"{text[i]}"])
            brailled_text_sym += punctuation[f"{brailled_text_num[i]}"]
        else:
            brailled_text_sym += brailled_text_num[i]

    # symbol node
    # print(brailled_text_sym)

    return brailled_text_sym


def convert_capital(brailled_text_sym):
    """treat capitals next, add 000001 before and convert to lower, will do shorthand conversion later"""

    text_list_sym = brailled_text_sym.split()

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
            brailled_text_caps += f"{brailled_text_caps_word[i]}"

    # caps node
    # print(brailled_text_caps)

    return brailled_text_caps


# Finally lowercase, changing to shorthand and then braille from dictionaries


def convert_lowercase_grade1(brailled_text_caps):
    """grade 1 individual letter decompile"""

    text_list_caps = brailled_text_caps.split()

    # individual letter decompile
    brailled_text = ""
    for i in range(len(brailled_text_caps)):
        if (  # letters in alphanumeric dictionary
            brailled_text_caps[i] in alphanumeric.keys()
            and brailled_text_caps[i].isalpha()
        ):
            brailled_text += alphanumeric.get(brailled_text_caps[i])
        elif (  # 6 digit numbers and whitespace since whitespace don't hurt
            brailled_text_caps[i].isdigit() or brailled_text_caps[i] == " "
        ):
            brailled_text += brailled_text_caps[i]
        else:  # any other unrecognisable character
            brailled_text += " 000000 "

    # grade 1 brailled node
    # print(brailled_text)

    return brailled_text


def convert_lowercase_grade2_wordsigns(brailled_text_caps):
    """wordsigns, only word check from wordsign dictionary
    list words, item by item
    """

    text_list_caps = brailled_text_caps.split()

    # wordsigns, only word check from wordsign dictionary
    # list words, item by item
    brailled_text_wordsigns = ""
    for i in range(len(text_list_caps)):
        if text_list_caps[i].isalpha() and text_list_caps[i] in wordsigns.keys():
            brailled_text_wordsigns += f" {wordsigns.get(text_list_caps[i])} "
        else:
            brailled_text_wordsigns += f" {text_list_caps[i]} "

    # wordsigns node
    # print(brailled_text_wordsigns)

    return brailled_text_wordsigns


def convert_lowercase_grade2_shortforms_word(brailled_text_wordsigns):
    """short forms dictionary
    list words, item by item
    """
    text_list_wordsigns = brailled_text_wordsigns.split()

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

    # shortforms word node
    # print(brailled_text_shortforms_word)

    return brailled_text_shortforms_word


def convert_lowercase_grade2_shortforms_substring(brailled_text_shortforms_word):
    """shortforms substring check"""
    text_list_shortforms_word = brailled_text_shortforms_word.split()

    # now shortforms substring check
    brailled_text_shortforms = ""
    for i in range(len(text_list_shortforms_word)):
        # if any of the keys is a substring of the larger string, a list element
        # iteration preference determined by elements in match list, which are determined by appearance order in dictionary
        matches = [x for x in shortforms.keys() if x in text_list_shortforms_word[i]]
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

    # shortforms node
    # print(brailled_text_shortforms)

    return brailled_text_shortforms


def convert_lowercase_grade2_contractions_word(brailled_text_shortforms):
    """contractions dictionary
    list words, item by item
    """
    text_list_shortforms = brailled_text_shortforms.split()

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

    # contractions word node
    # print(brailled_text_contractions_word)

    return brailled_text_contractions_word


def convert_lowercase_grade2_contractions_substring(brailled_text_contractions_word):
    """contractions substring check"""
    text_list_contractions_word = brailled_text_contractions_word.split()

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
                text_list_contractions_word[i] = text_list_contractions_word[i].replace(
                    f"{matches[j]}", f" {contractions.get(matches[j])} "
                )
            brailled_text_contractions += text_list_contractions_word[i]
        else:
            brailled_text_contractions += f" {text_list_contractions_word[i]} "

    # contractions node
    # print(brailled_text_contractions)

    return brailled_text_contractions


def convert_lowercase_grade2_groupsigns_final(brailled_text_contractions):
    """groupsigns final dictionary
    groupsigns final substring check only
    """
    text_list_contractions = brailled_text_contractions.split()

    # groupsigns final dictionary
    # groupsigns final substring check only
    brailled_text_groupsigns_final = ""
    for i in range(len(text_list_contractions)):
        # if any of the keys is a substring of the larger string, a list element
        # iteration preference determined by elements in match list, which are determined by appearance order in dictionary
        matches = [x for x in groupsigns_final.keys() if x in text_list_contractions[i]]
        # print(matches)
        if text_list_contractions[i].isalpha() and matches:
            for j in range(len(matches)):
                if (
                    text_list_contractions[i].startswith(matches[j]) == False
                ):  # if string does not start with matched substring
                    # iterate through the match list, replace all instances of the substring with spaced out, shortform substring
                    text_list_contractions[i] = text_list_contractions[i].replace(
                        f"{matches[j]}", f" {groupsigns_final.get(matches[j])} "
                    )
            brailled_text_groupsigns_final += text_list_contractions[i]
        else:
            brailled_text_groupsigns_final += f" {text_list_contractions[i]} "

    # groupsigns final node
    # print(brailled_text_groupsigns_final)

    return brailled_text_groupsigns_final


def convert_lowercase_grade2_groupsigns_substring(brailled_text_groupsigns_final):
    """groupsigns substring check"""
    text_list_groupsigns_final = brailled_text_groupsigns_final.split()

    # now groupsigns substring check
    brailled_text_groupsigns = ""
    for i in range(len(text_list_groupsigns_final)):
        # if any of the keys is a substring of the larger string, a list element
        # iteration preference determined by elements in match list, which are determined by appearance order in dictionary
        matches = [x for x in groupsigns.keys() if x in text_list_groupsigns_final[i]]
        # print(matches)
        if text_list_groupsigns_final[i].isalpha() and matches:
            for j in range(len(matches)):
                if (
                    text_list_groupsigns_final[i] != matches[j]
                ):  # if string does not equal to matched substring
                    # iterate through the match list, replace all instances of the substring with spaced out, shortform substring
                    text_list_groupsigns_final[i] = text_list_groupsigns_final[
                        i
                    ].replace(f"{matches[j]}", f" {groupsigns.get(matches[j])} ")
            brailled_text_groupsigns += text_list_groupsigns_final[i]
        else:
            brailled_text_groupsigns += f" {text_list_groupsigns_final[i]} "

    # groupsigns node
    # print(brailled_text_groupsigns)

    return brailled_text_groupsigns


def convert_lowercase_grade2_decompile_character(brailled_text_groupsigns):
    """individual letter decompile"""
    text_list_groupsigns = brailled_text_groupsigns.split()

    # individual letter decompile
    brailled_text = ""
    for i in range(len(brailled_text_groupsigns)):
        if (  # letters in alphanumeric dictionary
            brailled_text_groupsigns[i] in alphanumeric.keys()
            and brailled_text_groupsigns[i].isalpha()
        ):
            brailled_text += alphanumeric.get(brailled_text_groupsigns[i])
        elif (  # 6 digit numbers and whitespace since whitespace don't hurt
            brailled_text_groupsigns[i].isdigit() or brailled_text_groupsigns[i] == " "
        ):
            brailled_text += brailled_text_groupsigns[i]
        else:  # any other unrecognisable character
            brailled_text += " 000000 "

    # grade 2 brailled node
    # print(brailled_text)

    return brailled_text


def display_braille(brailled_text):
    """Takes processed text that has been converted to braille and displays it in braille format."""

    brailled_list = brailled_text.split()

    braille_text_1 = ""
    braille_text_2 = ""
    braille_text_3 = ""
    braille_unicode_spaced = ""
    braille_unicode = ""

    # Display brailled list
    for i in range(len(brailled_list)):  # each list element, a 6 digit code
        if brailled_list[i] in unicode.keys():
            braille_unicode += f"{unicode.get(brailled_list[i])}"
            braille_unicode_spaced += f"  {unicode.get(brailled_list[i])}  "
        for j in range(len(brailled_list[i])):  # iterate through 6 digit code element
            br[j + 1] = brailled_list[i][j]

        single_braille = f"""
 {br[1]} {br[4]} 
 {br[2]} {br[5]} 
 {br[3]} {br[6]} """
        braille_text_1 += f" {br[1]} {br[4]} "
        braille_text_2 += f" {br[2]} {br[5]} "
        braille_text_3 += f" {br[3]} {br[6]} "
        # print(single_braille)
        sleep(timer)

    # braille text node
    print(f"Text:\n{text}\n")
    if grade1:
        print("Grade 1 Uncontracted Braille:")
    else:
        print("Grade 2 Contracted Braille:")
    print(braille_text_1)
    print(braille_text_2)
    print(braille_text_3)
    print(braille_unicode_spaced)
    print("")
    print(braille_unicode)


# Input
toggle_grade()
text = input("Enter the text you want to convert to Braille: ")

# Process
text_sym_spaced = space_out_symbols_punctuation(text)
text_alphanumeric_spaced = space_out_alphanumeric(text_sym_spaced)
brailled_text_num_word = convert_numeric_word(text_alphanumeric_spaced)
brailled_text_num = convert_numeric_character(brailled_text_num_word)
brailled_text_sym = convert_symbols_punctuation(brailled_text_num)
brailled_text_caps = convert_capital(brailled_text_sym)

# lowercase conversion
if grade1:
    brailled_text = convert_lowercase_grade1(brailled_text_caps)
else:  # grade 2
    brailled_text_wordsigns = convert_lowercase_grade2_wordsigns(brailled_text_caps)
    brailled_text_shortforms_word = convert_lowercase_grade2_shortforms_word(
        brailled_text_wordsigns
    )
    brailled_text_shortforms = convert_lowercase_grade2_shortforms_substring(
        brailled_text_shortforms_word
    )
    brailled_text_contractions_word = convert_lowercase_grade2_contractions_word(
        brailled_text_shortforms
    )
    brailled_text_contractions = convert_lowercase_grade2_contractions_substring(
        brailled_text_contractions_word
    )
    brailled_text_groupsigns_final = convert_lowercase_grade2_groupsigns_final(
        brailled_text_contractions
    )
    brailled_text_groupsigns = convert_lowercase_grade2_groupsigns_substring(
        brailled_text_groupsigns_final
    )
    brailled_text = convert_lowercase_grade2_decompile_character(
        brailled_text_groupsigns
    )

# Output
display_braille(brailled_text)


# # Debug
# print(text_sym_spaced, text_sym_spaced.split())
# print(text_alphanumeric_spaced, text_alphanumeric_spaced.split())
# print(brailled_text_num_word, brailled_text_num_word.split())
# print(brailled_text_num, brailled_text_num.split())
# print(brailled_text_sym, brailled_text_sym.split())
# print(brailled_text_caps, brailled_text_caps.split())
# if grade1:
#     print(brailled_text, brailled_text.split())
# else:
#     print(brailled_text_wordsigns, brailled_text_wordsigns.split())
#     print(brailled_text_shortforms_word, brailled_text_shortforms_word.split())
#     print(brailled_text_shortforms, brailled_text_shortforms.split())
#     print(brailled_text_contractions_word, brailled_text_contractions_word.split())
#     print(brailled_text_contractions, brailled_text_contractions.split())
#     print(brailled_text_groupsigns_final, brailled_text_groupsigns_final.split())
#     print(brailled_text_groupsigns, brailled_text_groupsigns.split())
#     print(brailled_text, brailled_text.split())
