sourceFile = 'target.txt' #sets the target file to a variable

#sets a function to open the file, and returns the value read
def readFile(): 

    #opens the file from the global variable set on line 1, reads
    infile = open(sourceFile, 'r')
    
    #reads the opened file and sets it to the variable 'num'
    num = infile.readline()
    
    #closes the file, best practice
    infile.close()
    
    #retuns the value of 'num' when the function is called, sets it to an interger for math functions
    return int(num)


#sets a function to collect an input
def manualInput():
    
    #sets a var to an input value
    numInput = input('Enter a Number: ')
    
    #retuns the value of 'num' when the function is called, sets it to an interger for math functions
    return int(numInput)

#sets a fuction, and passes the var writeText to it
def writeFile(writeText):
    
    #opens the file from the global variable set on line 1, appends
    infile = open(sourceFile, 'a')
    
    #takes the wreiteText argument and sets it to a string, writes it to a new line of the text file
    infile.write("\n" + str(writeText))
    
    #closes the file, best practice
    infile.close()
    
    

#sets a fuction to call others defined earlier
def main ():
    
    #sets a var to the value returned by readFile
    x = readFile()
    #sets a var to the value returned by manualInput
    y = manualInput()
    
    #adds readFile to manualInput
    math = x + y
    
    #prints the result of math
    writeFile(math)
    
#calls the main function
main()