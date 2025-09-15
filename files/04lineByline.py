try:
    file = open("files/arsh.txt", "rt")
    print(content:= file.read())
    for line in file:
        print(line)
        file.close

except Exception as e:
    print(e)
