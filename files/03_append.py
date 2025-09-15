#'a' (Append mode): Opens the file for appending. Data will be added to the end of the file. If the file doesn't exist, a new file will be created
arshFile = open("files/2_arsh.txt", "at")
text = '''He is currently learning python, then he will learn api, database and then flask so he could make his gym app with prince.
'''
arshFile.write(text)
arshFile.close()
arshFile = open("files/2_arsh.txt", "rt")
print(p:= arshFile.read())