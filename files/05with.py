# try:
#     f = open("files/arsh.txt", "r")
#     print(content := f.read())
#     f.close()
# except FileNotFoundError as e :
#     print(e)
# #'r' (Read mode): Opens the file for reading. This is the default mode. If the file doesn't exist, you'll get an error.

try:
    with open("files/arsh.txt") as f:
        print(f.read())
    #no need to close the file, it automatically closes after with end
    
except Exception as e:
    print(e)
