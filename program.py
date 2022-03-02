import os
import sys
import shutil



def cleanFiles(targetFileNames: list):

    acceptableFileTypes = ["txt", "py", "pyw"]

    outputDirectory = "CleanupOutputOld"

    os.mkdir(outputDirectory)

    clearBlanklines = True
    clearComments = True

    for targetFileName in targetFileNames:

        # print("-------------------------")

        targetFileNameReversed = targetFileName[::-1]

        extensionReversed, _, basenameReversed = str(targetFileNameReversed).partition(".")

        basenameStraightened = basenameReversed[::-1]
        extensionStraightened = extensionReversed[::-1]

        # fullnameStraightened = f"{basenameStraightened}.{extensionStraightened}"

        # print(f"{targetFileName} == {fullnameStraightened}")

        if extensionStraightened not in acceptableFileTypes:

            # print(f"{targetFileName} wasn't part of the acceptable file types of {str(acceptableFileTypes)}")

            continue

        
        
        # print(f"Cleaning the file: {targetFileName}")






        openedFile = open(targetFileName, "r")

        fileContents = openedFile.read()

        openedFile.close()

        
        contentSplitted = fileContents.split("\n")

        finalContents = []

        for line in contentSplitted:

            lineClearsConditions = True

            if clearBlanklines:
                
                if (line.strip()) == "":
                    lineClearsConditions = False
                #     # continue
                # else:
                #     finalContents.append(line)
                    # continue

            
            if clearComments:

                if (line.lstrip()).startswith("#"):
                    lineClearsConditions = False
                #     continue
                # else:
                #     finalContents.append(line)

            # finalC


            # print(f"for line: {line}, lineClearscondition is {lineClearsConditions}")

            if lineClearsConditions:
                finalContents.append(line)


            # if clearBlanklines:
            #     if not (line.strip() == ""):
            #         finalContents.append(line)
            #         continue

            # if clearComments:

            #     # if not ((line).lstrip().startswith("#")):
                
            #     if not ((line.lstrip()).startswith("#")):
            #         finalContents.append(line)
            #         continue


        
        finalTowrite = "\n".join(finalContents)

        # print(finalContents)

        # print(finalTowrite)

            # print(line)

        # finalTowrite = "\n".join(finalContents)

        # print(finalTowrite)

        # newFilename = f"{outputDirectory}/{basenameStraightened}_clean.{extensionStraightened}"
        
        # newFilename = f"{outputDirectory}/{basenameStraightened}.{extensionStraightened}"
        kindaOriginalFilename = f"{basenameStraightened}.{extensionStraightened}"
        shouldMoveOldFileTo = f"{outputDirectory}/{basenameStraightened}.{extensionStraightened}"


        # writeFile = open(newFilename, "w")

        shutil.move(kindaOriginalFilename, shouldMoveOldFileTo)
        
        writeFile = open(kindaOriginalFilename, "w")
        writeFile.write(finalTowrite)
        writeFile.close()

    # print(len(os.listdir(outputDirectory)))

    if len(os.listdir(outputDirectory)) == 0:
        os.rmdir(outputDirectory)












ownName = os.path.basename(sys.argv[0])


# print((ownName))

filesHere = os.listdir('.')

# print(filesHere)

filesHere.remove(ownName)


if len(filesHere)<= 0:
    sys.exit()


# if len(filesHere) == 1:
#     targetFile = filesHere[0]

#     # print(targetFile)

#     if not targetFile == ownName:
#         # runprocess()
#         cleanFile(targetFile)

# else:
#     print("no suitable target")


cleanFiles(filesHere)




# input()