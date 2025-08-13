# import mymath
# print(mymath.add(18,19))
# RE = open('demo.txt','w+')
# print(RE.read())

# try:
#     for i in range(12):
#         RE.write("I AM IN THE SECTION\n THIS IS RAHUL %d\n" % (i+4-3))
# finally:
#     RE.write('Hello, world!.\n THIS IS RAHUL')
#     RE.close()
re = open('demo.txt','r+')

for line in re:
    print(len(line))
    print(line.split(" "))
re.close() 