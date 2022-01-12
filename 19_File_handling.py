"""

# File IO basics
"r" -- open file for reading       -- Default
"w" -- open file fot writing
"x" -- creates file if not exits
"a" -- add more content to a file
"t" -- text mode                   -- Default
"b" -- binary mode
"+" -- Read and Write
"""

# f=open("vinayak.txt","rt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# for line in f:
#     print(line,end="")
# content=f.read()
# content1=f.read(35)
# print(content)
# print(f.readlines())
# f.close()


#############        File writing    ##########
# x=open("vinayak.txt","w") # writing on file
# cnt=x.read()
# x=open("vinayak.txt","a")   # appending a file ..... or adding a content on file
# x.write("vinayak is a good boy \n")
# x.write("vinayak is a good boy \n")
# x.write("vinayak is a good boy \n")
# x.close()


####### Handling read and write both operation #######
# b=open("vinayak.txt","r+")
# print(b.read())
# b.write("thank you")
# b.close()


########  seek() and tell() functions in file handling
# g=open("vinayak.txt")
# # print(g.tell())   # showing the where is file pointer is present on text file line
# print(g.readline())
# # print(g.tell())
# print(g.readline())
# g.seek(0)
# # print(g.tell())
# print(g.readline())
# print(g.readline())
# # print(g.tell())
# g.close()


####### opening file using with Block   ####

with open("vinayak.txt") as l:
    print(l.readline())

n=open("vinayak.txt")
print(n.readline())
n.close()



