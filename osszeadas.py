import random
import os

print("ATTENTION!!! ONLY WORKS WITH POSITIVE INTEGERS AT THE MOMENT!!!!")
print("AND DON'T GIVE TOO BIG NUMBERS! IT'S GONNA WORK WITH THEM BUT IT'LL TAKE FOREVER TO FINISH!!!!!!!!")
print(
    "YOU CAN RUN THE COMMENTED LINES TOO IF YOU WANT BUT AN AVERAGE HUMAN'S LIFESPAN IS MUCH SHORTER THEN THE PROCESS THAT WAY!!!!")


def rand_lnum(x, s1, s2):
    l = []
    num = 0
    for i in range(1, x + 1):
        num = random.randint(s1, s2)
        l.append(num)
    print(l)
    return l


a = str(input("1. szam: "))
b = str(input("2. szam: "))
ossz_str = a + b

num1len = len(a)
num2len = len(b)
nums1 = ""
nums2 = ""
for i in range(0, num1len):
    nums1 += ossz_str[i]
for i in range(num1len, len(ossz_str)):
    nums2 += ossz_str[i]

num1 = int(nums1)
num2 = int(nums2)

ossznum = num1 + num2

l = []
for i in range(0, 100):
    l.append(num1)
    l.append(num2)
    l.append(random.randint(0, 100))

for i in l:
    if i == num1:
        num1_f = i
    elif i == num2:
        num2_f = i

lrand1 = rand_lnum(10, 0, num1_f)

while True:
    if num1_f in lrand1:
        new_num1 = num1_f
        break
    else:
        # time.sleep(2)
        lrand1 = rand_lnum(10, 0, num1_f)
lrand2 = rand_lnum(10, 0, num2_f)
while True:
    if num2_f in lrand2:
        new_num2 = num2_f
        break
    else:
        # time.sleep(2)
        lrand2 = rand_lnum(10, 0, num2_f)

print(new_num1)
print(new_num2)

splitter1 = random.randint(1, new_num1)
while True:
    if new_num1 % splitter1 == 0:
        newer_num1 = new_num1
        break
    else:
        # time.sleep(2)
        print(splitter1)
        splitter1 = random.randint(1, new_num1)

splitter_2 = random.randint(1, new_num2)
while True:
    if new_num2 % splitter_2 == 0:
        newer_num2 = new_num2
        break
    else:
        # time.sleep(2)
        print(splitter_2)
        splitter_2 = random.randint(1, new_num2)

print(newer_num1)
print(newer_num2)
newer_str1 = str(newer_num1)
newer_str2 = str(new_num2)

secret1 = ""
secret2 = ""
secret = {"0": "n",
          "1": "a",
          "2": "bb",
          "3": "ccc",
          "4": "dddd",
          "5": "eeeee",
          "6": "ffffff",
          "7": "ggggggg",
          "8": "hhhhhhhh",
          "9": "iiiiiiiii"}

lstr1 = []
print(lstr1)

for i in range(0, len(newer_str1)):
    lstr1.append(newer_str1[i])

for i in lstr1:
    secret1 += secret[i] + " "

print(lstr1)
print(secret1)

lstr2 = []
print(lstr2)

for i in range(0, len(newer_str2)):
    lstr2.append(newer_str2[i])

for i in lstr2:
    secret2 += secret[i] + " "

print(lstr2)
print(secret2)

decodel1 = []
part1 = ""
for i in secret1:
    if i != " ":
        part1 += i
    else:
        decodel1.append(part1)
        part1 = ""

print(decodel1)

decodel2 = []
part2 = ""
for i in secret2:
    if i != " ":
        part2 += i
    else:
        decodel2.append(part2)
        part2 = ""

print(decodel2)

decodeint1 = ""

for i in decodel1:
    decodeint1 += str(len(i))
print(decodeint1)

decodeint2 = ""

for i in decodel2:
    decodeint2 += str(len(i))
print(decodeint2)

newest_number1 = int(decodeint1)
newest_number2 = int(decodeint2)

lstr_rand = ["fuzzy",
             "ray",
             "transport",
             "hand",
             "tight",
             "abstracted",
             "attack",
             "run",
             "history",
             "root",
             "acceptable",
             "fang",
             "flow",
             "argument",
             "beam",
             "power",
             "dysfunctional",
             "volcano",
             "tidy",
             "geese",
             "rhyme",
             "suppose",
             "stove",
             "gigantic",
             "incredible",
             "uptight",
             "punish",
             "thundering",
             "huge",
             "juvenile",
             "contain",
             "bolt",
             "shy",
             "quill",
             "mint",
             "waiting",
             "apparatus",
             "competition",
             "flood",
             "disappear",
             "agree",
             "degree",
             "abandoned",
             "wink",
             "suspect",
             "daffy",
             "crash",
             "flash",
             "meal",
             "flippant",
             "report",
             "cheer",
             "anger",
             "market",
             "voyage",
             "spy",
             "attach",
             "mundane",
             "trap",
             "fancy",
             "building",
             "fine",
             "explain",
             "callous",
             "obedient",
             "cobweb",
             "memorize",
             "highfalutin",
             "rush",
             "sour",
             "recondite",
             "white",
             "humor",
             "crate",
             "continue",
             "hulking",
             "quince",
             "wind",
             "gather",
             "fantastic",
             "comparison",
             "stir",
             "homeless",
             "laughable",
             "plate",
             "smile",
             "outgoing",
             "chubby",
             "expect",
             "awesome",
             "corn",
             "size",
             "glossy",
             "walk",
             "foamy",
             "brick",
             "porter",
             "cemetery",
             "spiders",
             "table",
             "proud",
             "approval",
             "close",
             "peace",
             "authority",
             "form",
             "futuristic",
             "eager",
             "mean",
             "soothe",
             "night",
             "hunt",
             "tree",
             "helpless",
             "hurt",
             "pigs",
             "hour",
             "potato",
             "pot",
             "ugly",
             "grate"]

randword1 = random.choice(lstr_rand)
randword2 = random.choice(lstr_rand)

while True:
    word = random.choice(lstr_rand)
    if word == randword1:
        final_number1 = newest_number1
        break
    else:
        word = random.choice(lstr_rand)
        print(word)

print(final_number1)

while True:
    word2 = random.choice(lstr_rand)
    if word2 == randword2:
        final_number2 = newest_number2
        break
    else:
        word2 = random.choice(lstr_rand)
        print(word2)

print(final_number2)

cwd = os.getcwd()
print(cwd)
final = final_number1 + final_number2
final_number1_str = str(final_number1)
final_number2_str = str(final_number2)
final_str = str(final)
file = ""
file += final_number1_str
file += " + "
file += final_number2_str
file += " = "
file += final_str
file += "\nThis is the world's longest addition operation ran in Python(at least I think so, I didn't check)\nPS: This thing took my friday afternoon+night. It's 22:55 right now and I'm really tired so I hope I'm gonna get a Guinness for this."
filename = "megoldas.txt"

txt = open(filename, "w")
txt.write(file)
txt.close()
amogus = open("SUPER_SECRET_FILE.txt", "w")
amogus.write(
    "                            XXXXXXXXXXXXXXXXXXXXXXXXXX\n                       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n                 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXXXXXXXX000000000000000000000000000000000000\n       XXXXXXXXXXXXXXXXXXXXXXXXXX0000000000000000000000000000000000000000\n       XXXXXXXXXXXXXXXXXXXXXXXXXX0000000000000000000000000000000000000000\n       XXXXXXXXXXXXXXXXXXXXXXXXXX0000000000000000000000000000000000000000\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0000000000000000000000000000000000000000\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0000000000000000000000000000000000000000\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0000000000000000000000000000000000000000\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0000000000000000000000000000000000000000\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX000000000000000000000000000000000000\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX\n       XXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXX")
amogus.close()
print(
    f"Finally, the operation is done!\nYou can check the final result in your current working directory(cwd).\nI'll help. This is your cwd: {cwd}")