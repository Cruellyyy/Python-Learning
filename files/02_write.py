#'w' (Write mode): Opens the file for writing. If the file exists, its contents will be overwritten. If the file doesn't exist, a new file will be created.
arshFile = open("files/2_arsh.txt", "wt")
text = '''Arsh is a tech guy.
He is also a gym rat.
Although he is a bio student, he loves engenering fields like coding, electonics, meechanical etc.
He also love bioloy and science, he wants to know the secrects of living beings.
He is curious to know the secrects of this world, he seeks knowledge.
But he is very lazzy and distracted.
'''
arshFile.write(text)
arshFile.close()
arshFile = open("files/2_arsh.txt", "rt")
print(p:= arshFile.read())