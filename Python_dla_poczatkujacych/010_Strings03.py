somethingLikeNumber = '1000'
print(somethingLikeNumber)
print(int(somethingLikeNumber) + 1)
print(somethingLikeNumber + str(1))
print(type(somethingLikeNumber))
print(type(int(somethingLikeNumber) + 1))

# Funkcja "String 03" LAB
article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who 
created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five
episodes were made over four series. The Python phenomenon developed from the television series into something larger in
scope and impact, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy has
been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture, their
sketch show has been referred to as being "an important moment in the evolution of television comedy".[7]'''
print(article.upper())
print(article.lower().replace("monty", "flying"))
print(article.split(" "))
x = article.lower().count("python")
print("word python appears" + str(x) + "times")
text1 = r"to print the \ you need to put \ twice in your text like this: \\ "
print(text1)
text2 = 'The best hits of \'80s!!!'
print(text2)
text3 = "The best hits of '80s!!!"
print(text3)
amountPLN = 234
USD = amountPLN/3.65
EUR = amountPLN/4.23
print("cur", "\t", "exchange amount")
print("USD", "\t", str(USD))
print("EUR", "\t", str(EUR))
valueAsText = '123.45'
factor = 1.23
result = float(valueAsText)*factor
print("value is " + valueAsText + " factor is " + str(factor) + " value*factor=" + str(result))
