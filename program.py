import os
import sys

# Cleaning function accepts list of file names
def cleanFiles(targetFileNames: list):

    # Adjusting variables
    acceptableFileTypes = ["txt", "py", "pyw"]
    outputDirectory = "CleanupOutput"

    # Prepare the output directory
    os.mkdir(outputDirectory)

    # Types of conditions for each line
    clearBlanklines = True
    clearComments = True

    # Looping through each filename supplied
    for targetFileName in targetFileNames:

        # Manipulating strings (Filename)
        targetFileNameReversed = targetFileName[::-1]
        extensionReversed, _, basenameReversed = str(targetFileNameReversed).partition(".")
        basenameStraightened = basenameReversed[::-1]
        extensionStraightened = extensionReversed[::-1]

        # Go to next file if filetype isn't what we're ready for
        if extensionStraightened not in acceptableFileTypes:
            continue

        # Reading contents of current target file
        openedFile = open(targetFileName, "r")
        fileContents = openedFile.read()
        openedFile.close()
        contentSplitted = fileContents.split("\n")

        # Preparing vessel to collect each successful line
        finalContents = []

        # Looping through each line of content
        for line in contentSplitted:

            # We're assuming the line starts off successful
            lineClearsConditions = True

            # Fail the line if it seems to be an empty line
            if clearBlanklines:
                if (line.strip()) == "":
                    lineClearsConditions = False
            
            # Fail the line if it seems to start with a '#', indicating a comment
            if clearComments:
                if (line.lstrip()).startswith("#"):
                    lineClearsConditions = False
            
            # If it did not trigger any of the above checks, then it remains successful and will be added to the final result
            if lineClearsConditions:
                finalContents.append(line)
        
        # Join each line back
        finalTowrite = "\n".join(finalContents)

        # Write the finalised (cleaned) contents back to the file
        newFilename = f"{outputDirectory}/{basenameStraightened}.{extensionStraightened}"
        writeFile = open(newFilename, "w")
        writeFile.write(finalTowrite)
        writeFile.close()

    # If we've run the program and there seems to be no valid output files, we delete the output directory (To avoid clutter)
    if len(os.listdir(outputDirectory)) == 0:
        os.rmdir(outputDirectory)

# Getting the list of files in the current directory
ownName = os.path.basename(sys.argv[0])
filesHere = os.listdir('.')
filesHere.remove(ownName)

# If we're the sole file in the directory, we exit
if len(filesHere)<= 0:
    sys.exit()

# Run the program
cleanFiles(filesHere)