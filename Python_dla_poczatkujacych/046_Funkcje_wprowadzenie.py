def printHello():
    #this function just prints "hello"
    print("Hello")
    return
printHello()
printHello()
printHello()
printHello()


#Funkcje wprowadzenie - LAB

def printCat():
    #this function prints ascii-art cat
    txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
    print(txt)
    return

def printBear():
    #This function prints ascii-art bear
    txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    print(txt)
    return

def printBat():
    #This function prints ascii-art bat
    txt = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/  
         '''
    print(txt)
    return

printCat()
printBear()
printBat()