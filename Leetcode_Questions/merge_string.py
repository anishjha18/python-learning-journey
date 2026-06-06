word1="helo"
word2="yup"
for i in range (len(word1)):
    if i<len(word2):
        print(word1[i]+word2[i],end="")
    else:
        print(word1[i],end="")


