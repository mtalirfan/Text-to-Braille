punctuation = {
    # " ": " 000000 ",
    "‎": " 000000 ",  # convert all whitespaces to an empty unicode character, to retain braille space 000000 of the original text
    ".": " 010011 ",
    "…": " 010011 010011 010011 ",
    ",": " 010000 ",
    "?": " 011001 ",
    "“": " 011001 ",
    "”": " 001011 ",
    ":": " 010010 ",
    "∷": " 010010 010010 ",
    ";": " 011000 ",
    "!": " 011010 ",
    # "_": " 000001 001001 ", # long dash
    "_": " 000101 001001 ",  # underscore preferred
    "π": " 000101 111100 ",
    '"': " 000001 011011 ",
    "‘": " 000001 011001 ",
    "’": " 000001 001011 ",
    "'": " 001000 ",  # single quotation
    # "’": " 001000 ", # apostrophe
    "′": " 011011 ",  # feet, single prime
    "″": " 011011 011011 ",  # inches, double prime
    "«": " 000111 011001 ",
    "»": " 000111 001011 ",
    # "/": " 000111 001100 ", # forward slash
    "/": " 001100 ",  # divide sign preferred
    "\\": " 000111 100001 ",
    "{": " 000111 110001 ",
    "}": " 000111 001110 ",
    "∠": " 000111 010101 ",
    "#": " 000111 100111 ",
    "•": " 000111 010011 ",
    "[": " 000101 110001 ",
    "]": " 000101 001110 ",
    "%": " 000101 001011 ",
    "—": " 000010 000001 001001 ",
    "〃": " 000010 010000 ",
    "(": " 000010 110001 ",
    ")": " 000010 001110 ",
    "+": " 000010 011010 ",
    "-": " 001001 ",  # using simple hyphen for minus and dashes
    "–": " 000010 001001 ",
    "×": " 000010 011001 ",  # multiplication
    "÷": " 000010 001100 ",
    "=": " 000010 011011 ",
    "≠": " 000010 011011 000100 100011 ",
    "*": " 000010 001010 ",
    "√": " 000010 100101 ",
    "@": " 000100 100000 ",
    "¢": " 000100 100100 ",
    "€": " 000100 100010 ",
    "₣": " 000100 110100 ",
    "£": " 000100 111000 ",
    "₦": " 000100 101110 ",
    "$": " 000100 011100 ",
    "¥": " 000100 101111 ",
    "&": " 000100 111101 ",
    "<": " 000100 110001 ",
    "^": " 000100 010001 ",  # caret
    "~": " 000100 001010 ",  # tilde
    ">": " 000100 001110 ",
    "✓": " 000100 100101 ",
    "†": " 000100 000001 100111 ",
    "‡": " 000100 000001 110111 ",
    "©": " 000110 100100 ",
    "°": " 000110 010110 ",
    "¶": " 000110 111100 ",
    "®": " 000110 111010 ",
    "§": " 000110 011100 ",
    "™": " 000110 011110 ",
    "♀": " 000110 101101 ",
    "♂": " 000110 101111 ",
    "´": " 000110 001100 ",
    "`": " 000110 100001 ",
    "¨": " 000110 010010 ",  # umlaut
    # "^": " 000110 100101 ", # circumflex
    # "~": " 000110 110111 ", # tilde accent
    "→": " 110011 101010 ",
    "↓": " 110011 100101 ",
    "←": " 110011 010101 ",
    "↑": " 110011 001101 ",
}

wordsigns = {  # all: alphabetic, strong and lower
    # ALPHABETIC WORDSIGNS
    # no sign for a
    "but": "b",
    "can": "c",
    "do": "d",
    "every": "e",
    "from": "f",
    "go": "g",
    "have": "h",
    # no sign for i
    "just": "j",
    "knowledge": "k",
    "like": "l",
    "more": "m",
    "not": "n",
    # no sign for o
    "people": "p",
    "quite": "q",
    "rather": "r",
    "so": "s",
    "that": "t",
    "us": "u",
    "very": "v",
    "will": "w",
    "it": "x",
    "you": "y",
    "as": "z",
    # STRONG WORDSIGNS top bottom left right dots
    "child": " 100001 ",
    "shall": " 100101 ",
    "this": " 100111 ",
    "which": " 100011 ",
    "out": " 110011 ",
    # LOWER WORDSIGNS not dots 1 or 4
    "still": " 001100 ",
    "be": " 011000 ",
    "enough": " 010001 ",
    "were": " 011011 ",
    "his": " 011001 ",
    "in": " 001010 ",
    "was": " 001011 ",
}

shortforms = {
    "about": "ab",
    "above": "abv",
    "according": "ac",
    "across": "acr",
    # "after": "af", # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "afternoon": "afn",
    "afterward": "afw",
    "after": "af",  # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    # "again": "ag", # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "against": "agst",
    "again": "ag",  # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "almost": "alm",
    "already": "alr",
    "also": "al",
    "although": "alth",
    "altogether": "alt",
    "always": "alw",
    "because": "bec",
    "before": "bef",
    "behind": "beh",
    "below": "bel",
    "beneath": "ben",
    "beside": "bes",
    "between": "bet",
    "beyond": "bey",
    "blind": "bl",
    "braille": "brl",
    "children": "chn",
    "conceive": "concv",
    "conceiving": "concvg",
    "could": "cd",
    "deceive": "dcv",
    "deceiving": "dcvg",
    "declare": "dcl",
    "declaring": "dclg",
    "either": "ei",
    "first": "fst",
    "friend": "fr",
    "good": "gd",
    "great": "grt",
    "herself": "herf",
    # "him": "hm", # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "himself": "hmf",
    "him": "hm",  # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "immediate": "imm",
    # "its": "xs", # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "itself": "xf",
    "its": "xs",  # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "letter": "lr",
    "little": "ll",
    "much": "mch",
    "must": "mst",
    "myself": "myf",
    "necessary": "nec",
    "neither": "nei",
    "oneself": "onef",
    "ourselves": "ourvs",
    "paid": "pd",
    "perceive": "percv",
    "perceiving": "percvg",
    "perhaps": "perh",
    "quick": "qk",
    "receive": "rcv",
    "receiving": "rcvg",
    "rejoice": "rjc",
    "rejoicing": "rjcg",
    "said": "sd",
    "should": "shd",
    "such": "sch",
    "themselves": "themvs",
    "thyself": "thyf",
    "today": "td",
    "together": "tgr",
    "tomorrow": "tm",
    "tonight": "tn",
    "would": "wd",
    # "your": "yr", # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "yourself": "yrf",
    "yourselves": "yrvs",
    "your": "yr",  # keeping larger word above smaller substring gives it preference, since it appears first in matches list
}

contractions = {  # smaller substrings should be unique, if they appear in the larger words, put them in lower order
    # STRONG CONTRACTIONS (Part and Whole Word)
    "and": " 111101 ",
    "for": " 111111 ",
    "of": " 111011 ",
    # "the": " 011101 ", # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "with": " 011111 ",
    # INITIAL-LETTER CONTRACTIONS
    "day": " 000010 100110 ",
    "ever": " 000010 100010 ",
    "father": " 000010 110100 ",
    "here": " 000010 110010 ",
    "know": " 000010 101000 ",
    "lord": " 000010 111000 ",
    "mother": " 000010 101100 ",
    "name": " 000010 101110 ",
    "one": " 000010 101010 ",
    "part": " 000010 111100 ",
    "question": " 000010 111110 ",
    "right": " 000010 111010 ",
    "some": " 000010 011100 ",
    "time": " 000010 011100 ",
    "under": " 000010 101001 ",
    "work": " 000010 010111 ",
    "young": " 000010 101111 ",
    "there": " 000010 011101 ",
    "character": " 000010 100001 ",
    "through": " 000010 100111 ",
    "where": " 000010 100011 ",
    "ought": " 000010 110011 ",
    "upon": " 000110 101001 ",
    "word": " 000110 010111 ",
    "these": " 000110 011101 ",
    "those": " 000110 100111 ",
    "whose": " 000110 100011 ",
    "cannot": " 000111 100100 ",
    "had": " 000111 110010 ",
    "many": " 000111 101100 ",
    "spirit": " 000111 011100 ",
    "world": " 000111 010111 ",
    "their": " 000111 011101 ",
    "the": " 011101 ",  # keeping larger word above smaller substring gives it preference, since it appears first in matches list
}

groupsigns = {
    # STRONG GROUPSIGNS
    "ch": " 100001 ",
    "sh": " 100101 ",
    "th": " 100111 ",
    "wh": " 100011 ",
    # "ou": " 110011 ", # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "st": " 001100 ",
    "gh": " 110001 ",
    "ed": " 110101 ",
    "er": " 110111 ",
    "ow": " 010101 ",
    "ar": " 001110 ",
    "ing": " 001101 ",
    # LOWER GROUPSIGNS
    "ea": " 010000 ",
    "bb": " 011000 ",
    "cc": " 010010 ",
    "ff": " 011010 ",
    "gg": " 011011 ",
    "be": " 011000 ",
    "con": " 010010 ",
    "dis": " 010011 ",
    # "en": " 010001 ", # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    # "in": " 001010 ", # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    # FINAL-LETTER GROUPSIGNS
    "ound": " 000101 100110 ",
    "ance": " 000101 100010 ",
    "sion": " 000101 101110 ",
    "less": " 000101 011100 ",
    "ount": " 000101 011110 ",
    "ence": " 000011 100010 ",
    "ong": " 000011 110110 ",
    "ful": " 000011 111000 ",
    "tion": " 000011 101110 ",
    "ness": " 000011 011100 ",
    "ment": " 000011 011110 ",
    "ity": " 000011 101111 ",
    "ou": " 110011 ",  # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "en": " 010001 ",  # keeping larger word above smaller substring gives it preference, since it appears first in matches list
    "in": " 001010 ",  # keeping larger word above smaller substring gives it preference, since it appears first in matches list
}

contractions_retired = {  # not used in UEB, so not used in this project
    "ble": " 001111 ",
    "ation": " 000001 101110 ",
    "ally": " 000001 101111 ",
    "dd": " 010011 ",
    "com": " 001001 ",
    "to": " 011010 ",
    "into": " 001010 011010 ",
    "by": " 001011 ",
    "o'clock": "o'c",
}

indicator = {
    "capital": " 000001 ",
    "letter": " 001111 ",
    "shape": " 110101 ",
    "arrow": " 110011 ",
    "subscript": " 010001 ",
    "superscript": " 001010 ",
}

alphanumeric = (
    {}
)  # we will populate it for patterned characters iteratively instead of manually

alphanumeric_string = "‎1234567890abcdefghijklmnopqrstuvxyz‎‎‎‎wABCDEFGHIJKLMNOPQRSTUVXYZ‎‎‎‎W"
# indices 0, 36, 37, 38, 39, 66, 67, 68, 69 unused

alphanumeric_list = list(alphanumeric_string)

for i in range(len(alphanumeric_list)):
    alphanumeric_code = ""
    if alphanumeric_list[i].isupper():
        alphanumeric_code += "000001 "  # originally capitals were intended to be used from those populated in dictionary, now they are being converted to lowercase during processing
    elif alphanumeric_list[i].islower():
        pass
    else:
        try:
            alphanumeric_list[i].isdigit()
        except:
            pass
        # alphanumeric_code += " 001111 " # originally numbers were populated in dictionary with indicator, now they are being treated as list elements during processing

    str_to_append = ""
    match i % 10:
        case 1:
            str_to_append = "10"
            if i == 21 or i == 51 or i == 31 or i == 61:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "00"
            if i == 31 or i == 61:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append
        case 2:
            str_to_append = "11"
            if i == 22 or i == 52 or i == 32 or i == 62:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "00"
            if i == 32 or i == 62:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append
        case 3:
            str_to_append = "10"
            if i == 23 or i == 53 or i == 33 or i == 63:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "10"
            if i == 33 or i == 63:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append
        case 4:
            str_to_append = "10"
            if i == 24 or i == 54 or i == 34 or i == 64:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "11"
            if i == 34 or i == 64:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append
        case 5:
            str_to_append = "10"
            if i == 25 or i == 55 or i == 35 or i == 65:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "01"
            if i == 35 or i == 65:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append
        case 6:
            str_to_append = "11"
            if i == 26 or i == 56 or i == 36 or i == 66:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "10"
            if i == 36 or i == 66:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append
        case 7:
            str_to_append = "11"
            if i == 27 or i == 57 or i == 37 or i == 67:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "11"
            if i == 37 or i == 67:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append
        case 8:
            str_to_append = "11"
            if i == 28 or i == 58 or i == 38 or i == 68:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "01"
            if i == 38 or i == 68:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append
        case 9:
            str_to_append = "01"
            if i == 29 or i == 59 or i == 39 or i == 69:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "10"
            if i == 39 or i == 69:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append
        case 0:
            str_to_append = "01"
            if i == 30 or i == 60:
                str_to_append += "1"
            else:
                str_to_append += "0"
            str_to_append += "11"
            if i == 40 or i == 70:
                str_to_append += "1 "
            else:
                str_to_append += "0 "
            alphanumeric_code += str_to_append

    # print(alphanumeric_code)

    alphanumeric[f"{alphanumeric_list[i]}"] = alphanumeric_code
alphanumeric.pop("\u200e")

# print(alphanumeric)
