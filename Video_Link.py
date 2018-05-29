#pip install pyperclip
import pyperclip

link = "https://www.youtube.com/watch?v=D6esTdOLXh4"


pyperclip.copy(link)
print ('Link has been copied to your clipboard')
print ('Watch the video here:',link)

#I don't need this test
#print('testing push/pull')
