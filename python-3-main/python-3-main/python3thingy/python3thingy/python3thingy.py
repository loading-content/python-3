import pickle

with open('dictionary.pkl', 'rb') as f:
    stuff = pickle.load(f)

def ask():
    del_check = 0
    print("what do you want to do: ")
    print("1. new word")
    print("2. delete word")
    print("3. view dictinary")
    print("4. translate")
    print("5. stop")
    q = input("")
    print("")

    if q == '1' or q == 'new word' or q == 'new':
        inputthings()
    elif q == '2' or q == 'delete word' or q == 'delete':
        for k in stuff.items():
            del_check += 1
        if del_check <= 2:
            print("you only have one wordset in the dictionary so if you do this the program will stop working")
            print(" ")
            ask()
        else:
            delete()
    elif q == '3' or q == 'view dictinary' or q == 'view':
        for k,v in stuff.items():
            print(f"{k}:{v}")
        print("")
        ask()
    elif q == '4':
        tra()
    elif q == '5' or q == 'stop':
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
    if en not in stuff:
        print("say the word in dutch")
        ne = input("")
        print("")
        stuff[en] = ne
        stuff[ne] = en
        ask()
    else:
        print("that already exists")
        print("would you like to change it? ")
        change = input("")
        if change == "yes":
            del stuff[stuff[en]]
            del stuff[en]
            inputthings()
        else:
            print("ok")
            print("")
            ask()

def delete():
    for k,v in stuff.items():
        print(f"{k}:{v}")
    print("what wordset would you like to delete ")
    delet = input("")
    print("")
    if delet in stuff:
        del stuff[stuff[delet]]
        del stuff[delet]
        print("done")
        print("")
        ask()
    else:
        print("that word isnt in the list would you like to:")
        print("1. try again")
        print("2. add it to the dictionary")
        print("3. stop")
        no_word = input("")
        if no_word == "1" or no_word == "try again" or no_word == "again":
            print("")
            delete()
        elif no_word == "add" or no_word == "2":
            print("")
            inputthings()
        elif no_word == "stop" or no_word == "3":
            print("")
            ask()

def tra():
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