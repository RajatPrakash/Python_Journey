# creating a text file

file = open('new_file.txt', 'a')  # append will open and write , if file does not exits then it will create that file

file.write('''This is the text file that has been created by python code

    CREATE: RAJAT PRAKASH   
    DATE: 26 JAN 2020
    
                            ''')

file.close()  # closing the file is important
