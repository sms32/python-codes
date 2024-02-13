with open("a.txt", 'r') as file:
    content = file.read()
    words = content.split()
    rev = words[::-1]
    with open("rev_hello.txt", 'w') as f:
        for i in rev:
            f.write(i)
            f.write(" ")
with open("rev_hello.txt", 'r') as f:
    print(f.read())
