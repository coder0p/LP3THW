#EXERCISE :15 
#Reading Files

from sys import argv
script, filename = argv

"""
testing in file handling of read, write, append and create a new file 
"""
# txt = open("readme2.txt","x")
# txt = txt.write("hello this is a new file!")
# txt = open("readme2.txt","r")
# print(txt.read())
# txt.close()
#txt = open(filename,"a")
# txt = open(filename)
# txt.write("\nThis is something new!")
# txt = open(filename,"r")
# print(txt.read())
#----------------------------------

txt = open(filename)

print(f"here is your file {filename} isn't it:")
response = input()
if(response=='yes'):
    print("\n"+txt.read())
elif(response=='no'):
    print("Please check the file name you've specified!")
print("\nDo you want one more file: ")
response2 = input()
if(response2=='yes'):
    print("type another filename to view")
    file_again = input("--> ")
    txt_again = open(file_again)
    print(txt_again.read())
elif(response2=='no'):
    print("Ok bie, come back later")
else:
    print("Something went wrong!")
