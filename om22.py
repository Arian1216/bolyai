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

#-----------------------------------------------------------------------------------------------------------------------

