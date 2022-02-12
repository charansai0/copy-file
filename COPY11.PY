#  Developed by : v.charan sai
#  Reference number : 21003158
#  Copying of content from one text file to another text file.
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
       # read content from first file
    for line in firstfile:
               
        # append content to second file
             secondfile.write(line)