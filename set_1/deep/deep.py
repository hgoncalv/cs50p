def answer(ret):
    if(ret):
        return "Yes"
    return "No"

userInput=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
print(answer(userInput.strip().lower().replace("-"," ")=="forty two" or userInput.strip()=="42"))
