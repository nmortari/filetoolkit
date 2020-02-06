#Import modules
import csv
import os

#Initialize variables
FileList = []
counter = 0
FileChoice = 0
LineNumberChoice = 0
LineCount = 0
OutputFileNumber = 1

#List all CSV files in the current folder
for files in os.listdir("./"):
        if files.endswith('.csv'):
                FileList.append(files)
print("List of CSV files in your folder\n-----------------------------------------")

#Prepends a number to each file to help the user select a file
for file in FileList:
        counter = counter + 1
        print(counter, " - ", file)

print("-----------------------------------------")

#Get input from the user to select a file
print("\nEnter the file number to split: ", end = "")
FileChoice = int(input())
print("You chose file:", FileList[FileChoice-1])

#Get input from the user to choose how many lines per file before splitting
print("\nHow many lines in each output file before splitting: ", end = "")
LineNumberChoice = int(input())
print("Each output file will write", LineNumberChoice, "lines before splitting")

print("\nEnter a name for your output files: ", end = "")
OutputFileName = input()
print("You have entered", OutputFileName, "as your output file name")

#Open the file the user picked from the list
with open('%s' %FileList[FileChoice-1], 'r') as csvimport:
        lines = csv.reader(csvimport, delimiter = ',')
        #Skip the first line (header information)
        next(csvimport)
        for allrows in lines:
                #If the max number of lines have been reached, create a new file
                if LineCount == 0:
                        OutputFile = open(OutputFileName + '-' + str(OutputFileNumber) + '.csv', 'w')
                        OutputFileNumber = OutputFileNumber + 1

                LineCount = LineCount + 1
                OutputFile.write(','.join(allrows) + '\n')
                #If the max number of lines have been reached, close the file and reset the line count
                if LineCount == LineNumberChoice:
                        OutputFile.close()
                        LineCount = 0

#Get the current directory
Directory = os.getcwd()

#Display the final result to the user
print("\n\n-----------------------------------------")
print("Splitting Complete\nYour CSV file has been split into " + str(OutputFileNumber-1) + " Files")
print("Your files have been saved in: " + Directory)