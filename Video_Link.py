#pip install pyperclip
import pyperclip
import os

link = "https://www.youtube.com/watch?v=D6esTdOLXh4"


pyperclip.copy(link)
print ('Link has been copied to your clipboard')
print ('Watch the video here:',link)

#I don't need this test
#print('testing push/pull')

os.system("start cmd @cmd /k cd djangoproject")

#Manage_Home = 'C:\Users\abbottm\github\DjangoCrash\djangoproject'
#print (Manage_Home)
