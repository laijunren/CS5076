# reading lines
f = open("example.txt")
ln1 = f.readline()
print(ln1)
ln2 = f.readline()
print(ln2)
f.close()

# writing two extra lines into file means appending lines.
f = open("example.txt","a")
f.write("\nThis is line 3")
f.write("\nThis is line 4")
f.close()