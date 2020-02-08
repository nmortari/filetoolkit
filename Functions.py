import csv
import os

def splitcsv():
    # Initialize variables
    file_choice = 0
    line_number_choice = 0
    line_count = 0
    output_file_number = 1

    # List all CSV files in the current folder
    while True:
        #print("topppppp\n\n")
        file_list = []
        counter = 0
        for files in os.listdir("./"):
            if files.endswith('.csv'):
                file_list.append(files)
        print("List of CSV files in your folder\n-----------------------------------------")

        # Prepends a number to each file to help the user select a file
        for file in file_list:
            counter = counter + 1
            print(counter, " - ", file)

        if counter == 0:
            print("No CSV files found in current directory\nPress Enter to retry")
            print("-----------------------------------------")
            input()
            continue
        else:
            print("-----------------------------------------")

        # Get input from the user to select a file
        print("\nEnter the file number to split: ", end="")
        try:
            file_choice = int(input())
            print("You chose file:", file_list[file_choice - 1])
        except:
            print("ERROR: Please enter a number between 1 and " + str(counter) + "\n\n\n")
        else:
            break

    # Get input from the user to choose how many lines per file before splitting
    print("\nHow many lines in each output file before splitting: ", end="")
    line_number_choice = int(input())
    print("Each output file will write", line_number_choice, "lines before splitting")

    print("\nEnter a name for your output files: ", end="")
    OutputFileName = input()
    print("You have entered", OutputFileName, "as your output file name")

    # Open the file the user picked from the list
    with open('%s' % file_list[file_choice - 1], 'r') as csvimport:
        lines = csv.reader(csvimport, delimiter=',')
        # Skip the first line (header information)
        next(csvimport)
        for allrows in lines:
            # If the max number of lines have been reached, create a new file
            if line_count == 0:
                OutputFile = open(OutputFileName + '-' + str(output_file_number) + '.csv', 'w')
                output_file_number = output_file_number + 1

            line_count = line_count + 1
            OutputFile.write(','.join(allrows) + '\n')
            # If the max number of lines have been reached, close the file and reset the line count
            if line_count == line_number_choice:
                OutputFile.close()
                line_count = 0

    # Get the current directory
    Directory = os.getcwd()

    # Display the final result to the user
    print("\n\n-----------------------------------------")
    print("Splitting Complete\nYour CSV file has been split into " + str(output_file_number - 1) + " Files")
    print("Your files have been saved in: " + Directory)