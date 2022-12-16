import pickle

with open('dictionary.pkl', 'rb') as f:
    stuff = pickle.load(f)

def ask():
    print("what do you want to do")
    print("1. new word")
    print("2. view dictinary")
    print("3. translate")
    print("4. stop")
    q = input("")
    print("")

    if q == '1' or q == 'new word' or q == 'new':
        inputthings()
    elif q == '2' or q == 'view dictinary' or q == 'view':
        print(stuff)
        print("")
        ask()
    elif q == '3':
        tra()
    elif q == '4' or q == 'stop':
        with open('dictionary.pkl', 'wb') as f:
            pickle.dump(stuff, f)
        exit()
    else:
        print("try again")
        print("")
        ask()

def inputthings():
    print("say an english word")
    en = input("")
    print("say the word in dutch")
    ne = input("")
    print("")
    stuff[en] = ne
    stuff[ne] = en
    ask()

def tra():
    print("do you want to translate from: ")
    print("1. english to dutch")
    print("2. dutch to english")
    tr = input("")
    print("")
    if tr == '1' or tr == 'en' or tr == 'english' or tr == 'english to dutch':
        print("what word do you want to translate?")
        t = input("")
        print("")
        if t in stuff:
            print("the tranlation of that woord is: " + stuff[t])
            print("")
            ask()
        else:
            print("that word doesnt exist")
            print("would you like to add it? ")
            print("1. yes")
            print("2. no")
            add = input("")
            print("")
            if add == '1' or add == 'yes':
                inputthings()
            else:
                print("ok")
                print("")
                ask()
    elif tr == '2' or tr == 'ne' or tr == 'dutch' or tr == 'dutch to english':
        print("what word do you want to translate?")
        t = input("")
        print("")
        if t in stuff:
            print("the tranlation of that woord is: " + stuff[t])
            print("")
            ask()
        else:
            print("that word doesnt exist")
            print("would you like to add it? ")
            print("1. yes")
            print("2. no")
            add = input("")
            print("")
            if add == '1' or add == 'yes':
                inputthings()
            else:
                print("ok")
                print("")
                ask()



ask()