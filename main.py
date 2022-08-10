import pywhatkit
print("Option 1: Send a message to an individual")
print("Option 2: Send a message to a group ")
opt = str(input("Enter the required option !!"))

if opt == "1":
    number = input("Enter the required Number !!")
    message = input("Enter the content of the message !!! ")
    pywhatkit.sendwhatmsg_instantly(number,message,5,True,1)
elif opt == "2":
    grp_name = input("Enter the name of the group !!")
    message = input("Enter the content of the message !!! ")
    pywhatkit.sendwhatmsg_to_group_instantly(grp_name,message,5,True,1)

