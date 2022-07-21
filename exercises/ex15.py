#EXERCISE :15 
#Reading Files

from sys import argv
script, filename = argv
txt = open(filename)

print(f"here is your file {filename} isn't it:")
response = input()
if(response=='yes'):
    print(txt.read())
elif(response=='no'):
    print("Please check the file name you've specified!")
print("Do your want more: ")
response2 = input()
if(response2=='yes'):
    print("type another filename to view")
    file_again = input("--> ")
    txt_again = open(file_again)
    print(txt_again.read())
elif(response2=='no'):
    print("Ok bie, come back later")
