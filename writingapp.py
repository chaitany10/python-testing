def write():
    text='Hello'
    savefile=open('examplefile.txt','w')
    savefile.write(text)
    savefile.close()
def append():
    text1="\tChaitany"
    savefile1=open('examplefile.txt','a')
    savefile1.write(text1)
    savefile1.close()

write()
append()

write()
