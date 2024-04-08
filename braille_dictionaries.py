punctuation_dic = {
    # " ": " 000000 ",
    ".": " 010011 ",
    ",": " 010000 ",
    "?": " 011001 ",
    ":": " 010010 ",
    ";": " 011000 ",
    "!": " 011010 ",
    "‘": " 000001 011001 ",
    "’": " 000001 001011 ",
    "'": " 001000 ",
    "“": " 011001 ",
    '"': " 000001 011011 ",
    "”": " 001011 ",
    "_": " 000001 001001 ",
    "—": " 000010 000001 001001 ",
    "-": " 001001 ",
    "/": " 000111 001100 ",
    "\\": " 000111 100001 ",
    "(": " 000010 110001 ",
    ")": " 000010 001110 ",
    "[": " 000101 110001 ",
    "]": " 000101 001110 ",
    "{": " 000111 110001 ",
    "}": " 000111 001110 ",
    "<": " 000100 110001 ",
    ">": " 000100 001110 ",
    "^": " 000100 010001 ",
    "+": " 000010 011010 ",
    "-": " 000010 001001 ",
    "×": " 000010 011001 ",  # multiplication
    "÷": " 000010 001100 ",
    "=": " 000010 011011 ",
    "¢": " 000100 100100 ",
    "$": " 000100 011100 ",
    "€": " 000100 100010 ",
    "£": " 000100 111000 ",
    # "‘": " 011011 ", feet
    # "“": " 011011 011011 ", inches
    "%": " 000101 001011 ",
    "°": " 000110 010110 ",
    "∠": " 000111 010101 ",
    "#": " 000111 100111 ",
    "&": " 000100 111101 ",
    "©": " 000110 100100 ",
    "™": " 000110 011110 ",
    "@": " 000100 100000 ",
    "*": " 000010 001010 ",
    "✓": " 000100 100101 ",
}


alphanumeric_dic = (
    {}
)  # we will populate it for patterned characters iteratively instead of manually

alphanumeric = "‎1234567890abcdefghijklmnopqrstuvxyz‎‎‎‎wABCDEFGHIJKLMNOPQRSTUVXYZ‎‎‎‎W"  # indices 0, 36, 37, 38, 39, 66, 67, 68, 69 unused

alphanumeric_list = list(alphanumeric)

for i in range(len(alphanumeric_list)):
    alphanumeric_code = ""
    if alphanumeric_list[i].isupper():
        alphanumeric_code += "000001 "  # originally capitals were intended to be used from those populated in dictionary, now they are being converted to lowercase during processing
    elif alphanumeric_list[i].islower():
        pass
    else:
        try:
            int(alphanumeric_list[i])
        except:
            pass
        alphanumeric_code += " 001111 "

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

    alphanumeric_dic[f"{alphanumeric_list[i]}"] = alphanumeric_code
alphanumeric_dic.pop("\u200e")


# print(alphanumeric_dic)
