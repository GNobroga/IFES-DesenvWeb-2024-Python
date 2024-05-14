import os 

if not os.path.exists('./temp'):
    os.mkdir('./temp')
    
if not os.path.exists('/temp/temp.txt'):
    open('./temp/temp.txt', mode='w').close()