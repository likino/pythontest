from sys import argv

script, filename = argv

test = open(filename)

print test.read()

print "open again: "
test1 = raw_input("filename:")

open_again = open(test1)
print open_again.read()
test.close()