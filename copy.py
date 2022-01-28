#  Developed by : v.charan sai
#  Reference number : 21003158
#  Copying of content from one text file to another text file.
with open('text1','r') as file1:
    with open('text2','w') as file2:
        for i in file1:
            file2.write(i)