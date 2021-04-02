try:
    user = open(r"C:\username.txt", "r+")
    
except:
    import os 
    path = 'C:\\'
    file = 'username.txt'
    username = input("Username: ")
    with open(os.path.join(path, file), 'w') as fp: 
        pass
        fp.write(username)
    print("Username successfully generated\n")

    
displayMsgs = open("messages.txt", "r+")
appendMags =  open("messages.txt", "a+")
    
try:
    for line in displayMsgs:
        print(line)
    msg = input("\nReply: ")
    appendMags.write("\n"+user.read()+": "+msg)
    appendMags.close()
    print(displayMsgs.read())
    print("Message successfully sent!")
except:
    print("\nMessage failed to send. Please report it.\nThanks!")
finally:
    appendMags.close()
    displayMsgs.close()
