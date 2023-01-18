dictionary = {
              "cat": "cica",
              "dog": "kutya",
              "horse": "ló",
              }
words=""
while dictionary != words:
    if words == " ":
        break
    words = input("Unknown words: ")

    if words in dictionary:
        print(words,"=",dictionary[words])
    else:
        print(words,"=","is not in dictionary")

################################################################

dictionary2 = {
              "cat": "cica",
              "dog": "kutya",
              "horse": "ló"
              }
#dictionary2['cat'] = 'macska'

word = input("Cserelje ki a kulcsszot: ")
dictionary2['cat'] = word
print(dictionary2)

################################################################

dictionary3 = {
              "cat": "cica",
              "dog": "kutya",
              "horse": "ló"
              }
for i in range(10):
    new_word = input("Uj szo: ")
    new_key = input("Uj kulcsszo: ")
    dictionary3.update({new_word:new_key})
print(dictionary3)

################################################################

szotar = {
        "table":"asztal",
        "key":"kulcs",
        "value":"ertek"
}
for english, magyar in szotar.items():
    print(english,"=",magyar)
for magyar in szotar.values():
    print(magyar)

################################################################

