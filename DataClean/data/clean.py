import json
import re
f = open('deck.json')
deck = json.loads(f.read())

notes = deck["children"][0]["notes"]

vocabs = []

for note in notes:
    content = note["fields"]
    level = note["tags"][1]

    vocab = {}

    vocab["id"] = str(int(content[0]) - 1) #!
    vocab["simplifiedChinese"] = content[1] #!
    vocab["traditionalChinese"] = content[2]
    vocab["pinyin"] = content[3] #!
    vocab["pinyinNunber"] = content[4]
    vocab["meaning"] = content[5] #!
    vocab["wordType"] = content[6]
    vocab["wordSound"] = content [7] #!
    vocab["sentenceWithSimplified"] = content[10] #!
    vocab["sentenceWithTraditional"] = content[11]
    vocab["sentencePinyin"] = content[14] #!
    vocab["sentencePinyinNumber"] = content[15]
    vocab["sentenceMeaning"] = content[16] #!
    vocab["sentenceSound"] = content[17] #!
    try:
        vocab["img"] = 'require("../../../assets/data/media/' + re.findall(r'"(.*)"', content[18])[0] + '")'#!
    except:
        vocab["img"] = ""
    vocab["level"] = level

    print(vocab)

    vocabs.append(vocab)

with open("vocabs.ts", "w") as outFile:
    json.dump(vocabs, outFile, indent=4)