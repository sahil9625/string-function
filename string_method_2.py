# strings are immutable

a = "!!!Sahil!! !!!!!!!!!!!!! Sahil"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
# rstrip se hum ! isko hta dete hai
print(a.replace("Sahil","Sameer"))
print(a.split(" "))
blogheading = "introduction to blog"
print(blogheading.capitalize())

str1 = "Welcome to the console!!!"
print(len(str1))
print((str1.center(50)))
print(len(str1.center(50)))
print(a.count("Sahil"))
str1 = "welcome to the console !!!"
print((str1.endswith("!!!")))
# ye batyega ki ye string !!! end ho rhi hai isee agar haa to true or na to false

str1 = "welcome to the console !!!"
print((str1.endswith("to",4,10)))

str1 = "he's name is dan. he is an honest man."
print(str1.find("is"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
# A-Z , a-z , 0-9 ke beech me bani string hai to 

str1 = "Welcome"
print(str1.isalpha())

str1 = "welcome"
print(str1.islower())

str1 = "We wish you a Merry Chritmas\n"
print(str1)
print(str1.isprintable())

str1 = "        "
#using spacebar
print(str1.isspace())

str1 = "      " # using tab
print(str1.isspace())

str1 = "World Health Org"
print(str1.istitle())

str1 = "Python is a language"
print(str1.startswith("Python"))

str1 = "Python is a language"
print(str1.swapcase())
# bade ko chota kar dega or chote letter ko bada

str1 = "he is a good boy."
print(str1.title())

