# 3. A spam comment is defined as a text containing following keywords: 
#   “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
#    to detect these
text=input("Enter text: ")

if (text == "Make a lot of money" or text=="buy now" or text=="subscribe this" or text=="click this"):
    print("SCAM !!!")
else:
    print("there isn't any scam")