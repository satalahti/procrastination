
input = input("Please, enter your name: ")

if input.lower() == "SANNI":
    #if just 'input' it will not include Sanni with a capital S
    print("Welcome " + input + "!")
elif input.lower() == "khizzar":
    print("Dont try to hack people, dude.")
else:

    collection = input.split(", ")
    print("This prints our full collection", collection)
    for item in collection:
        print("printing collection item: ", item)



#function is not object specific, method is tied to a specific object
