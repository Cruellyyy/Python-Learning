try:
    f = open("files/arsh.txt", "r")
    print(content := f.read())
    f.close()
except FileNotFoundError as e :
    print(e)
#'r' (Read mode): Opens the file for reading. This is the default mode. If the file doesn't exist, you'll get an error.