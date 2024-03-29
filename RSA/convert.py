def convert(x):
    alphabet = {
        "100": "0",
        "101": "1",
        "102": "2",
        "103": "3",
        "104": "4",
        "105": "5",
        "106": "6",
        "107": "7",
        "108": "8",
        "109": "9",
        "110": "a",
        "111": "b",
        "112": "c",
        "113": "d",
        "114": "e",
        "115": "f",
        "116": "g",
        "117": "h",
        "118": "i",
        "119": "j",
        "120": "k",
        "121": "l",
        "122": "m",
        "123": "n",
        "124": "o",
        "125": "p",
        "126": "q",
        "127": "r",
        "128": "s",
        "129": 't',
        "130": "u",
        "131": "v",
        "132": "w",
        "133": "x",
        "134": "y",
        "135": "z",
        "136": " ",
        "0": "100",
        "1": "101",
        "2": "102",
        "3": "103",
        "4": "104",
        "5": "105",
        "6": "106",
        "7": "107",
        "8": "108",
        "9": "109",
        "a": "110",
        "b": "111",
        "c": "112",
        "d": "113",
        "e": "114",
        "f": "115",
        "g": "116",
        "h": "117",
        "i": "118",
        "j": "119",
        "k": "120",
        "l": "121",
        "m": "122",
        "n": "123",
        "o": "124",
        "p": "125",
        "q": "126",
        "r": "127",
        "s": "128",
        "t": "129",
        "u": "130",
        "v": "131",
        "w": "132",
        "x": "133",
        "y": "134",
        "z": "135",
        " ": "136",
        "137": "A",
        "138": "B",
        "139": "C",
        "140": "D",
        "141": "E",
        "142": "F",
        "143": "G",
        "144": "H",
        "145": "I",
        "146": "J",
        "147": "K",
        "148": "L",
        "149": "M",
        "150": "N",
        "151": "O",
        "152": "P",
        "153": "Q",
        "154": "R",
        "155": "S",
        "156": "T",
        "157": "U",
        "158": "V",
        "159": "W",
        "160": "X",
        "161": "Y",
        "162": "Z",
        "163": ".",
        "164": ",",
        "165": "/",
        "166": "!",
        "167": "`",
        "168": "~",
        "169": "@",
        "170": "#",
        "171": "$",
        "172": "%",
        "173": "^",
        "174": "&",
        "175": "*",
        "176": "(",
        "177": ")",
        "178": "_",
        "179": "-",
        "180": "=",
        "181": "+",
        "182": "[",
        "183": "]",
        "184": "{",
        "185": "}",
        "186": "\n",
        "187": "|",
        "188": ":",
        "189": ";",
        "190": "'",
        "191": "\"",
        "192": "<",
        "193": ">",
        "194": "«",
        "195": "»",
        "196": "…",
        "197": "©",
        "198": "™",
        "199": "?",
        "A": "137",
        "B": "138",
        "C": "139",
        "D": "140",
        "E": "141",
        "F": "142",
        "G": "143",
        "H": "144",
        "I": "145",
        "J": "146",
        "K": "147",
        "L": "148",
        "M": "149",
        "N": "150",
        "O": "151",
        "P": "152",
        "Q": "153",
        "R": "154",
        "S": "155",
        "T": "156",
        "U": "157",
        "V": "158",
        "W": "159",
        "X": "160",
        "Y": "161",
        "Z": "162",
        ".": "163",
        ",": "164",
        "/": "165",
        "!": "166",
        "`": "167",
        "~": "168",
        "@": "169",
        "#": "170",
        "$": "171",
        "%": "172",
        "^": "173",
        "&": "174",
        "*": "175",
        "(": "176",
        ")": "177",
        "_": "178",
        "-": "179",
        "+": "180",
        "=": "181",
        "[": "182",
        "]": "183",
        "{": "184",
        "}": "185",
        "\n": "186",
        "|": "187",
        ":": "188",
        ";": "189",
        "'": "190",
        "\"": "191",
        "<": "192",
        ">": "193",
        "«": "194",
        "»": "195",
        "…": "196",
        "©": "197",
        "™": "198",
        "?": "199",
        "а": "200",
        "б": "201",
        "в": "202",
        "г": "203",
        "д": "204",
        "е": "205",
        "ё": "206",
        "ж": "207",
        "з": "208",
        "и": "209",
        "й": "210",
        "к": "211",
        "л": "212",
        "м": "213",
        "н": "214",
        "о": "215",
        "п": "216",
        "р": "217",
        "с": "218",
        "т": "219",
        "у": "220",
        "ф": "221",
        "х": "222",
        "ц": "223",
        "ч": "224",
        "ш": "225",
        "щ": "226",
        "ъ": "227",
        "ы": "228",
        "ь": "229",
        "э": "230",
        "ю": "231",
        "я": "232",
        "А": "233",
        "Б": "234",
        "В": "235",
        "Г": "236",
        "Д": "237",
        "Е": "238",
        "Ё": "239",
        "Ж": "240",
        "З": "241",
        "И": "242",
        "Й": "243",
        "К": "244",
        "Л": "245",
        "М": "246",
        "Н": "247",
        "О": "248",
        "П": "249",
        "Р": "250",
        "С": "251",
        "Т": "252",
        "У": "253",
        "Ф": "254",
        "Х": "255",
        "Ц": "256",
        "Ч": "257",
        "Ш": "258",
        "Щ": "259",
        "Ъ": "260",
        "Ы": "261",
        "Ь": "262",
        "Э": "263",
        "Ю": "264",
        "Я": "265",
        "200": "а",
        "201": "б",
        "202": "в",
        "203": "г",
        "204": "д",
        "205": "е",
        "206": "ё",
        "207": "ж",
        "208": "з",
        "209": "и",
        "210": "й",
        "211": "к",
        "212": "л",
        "213": "м",
        "214": "н",
        "215": "о",
        "216": "п",
        "217": "р",
        "218": "с",
        "219": "т",
        "220": "у",
        "221": "ф",
        "222": "х",
        "223": "ц",
        "224": "ч",
        "225": "ш",
        "226": "щ",
        "227": "ъ",
        "228": "ы",
        "229": "ь",
        "230": "э",
        "231": "ю",
        "232": "я",
        "233": "А",
        "234": "Б",
        "235": "В",
        "236": "Г",
        "237": "Д",
        "238": "Е",
        "239": "Ё",
        "240": "Ж",
        "241": "З",
        "242": "И",
        "243": "Й",
        "244": "К",
        "245": "Л",
        "246": "М",
        "247": "Н",
        "248": "О",
        "249": "П",
        "250": "Р",
        "251": "С",
        "252": "Т",
        "253": "У",
        "254": "Ф",
        "255": "Х",
        "256": "Ц",
        "257": "Ч",
        "258": "Ш",
        "259": "Щ",
        "260": "Ъ",
        "261": "Ы",
        "262": "Ь",
        "263": "Э",
        "264": "Ю",
        "265": "Я"
    }
    return alphabet[x]

if __name__ == '__main__':
    pass
