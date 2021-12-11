#--------------------------------NON-ESSENTIAL FUNCTIONS---------------------------#

#1
def compare_two_files(file1, file2):
#input : Filenames as strings
# opens both file1 and file2 for reading (filename1, filename2)
# reads contents of file and stores it in a string (fp1, fp2)
# compares both strings and stores the difference in an object (diff)
# closes files
#output: Prints the difference object with the + and - (print('\n'.join(diff)))
    filename1 = open(file1, 'r')
    filename2 = open(file2,'r')
    fp1 = filename1.read()
    fp2 = filename2.read()
    import difflib
    diff = difflib.ndiff(fp1.splitlines(),fp2.splitlines())
    filename1.close()
    filename2.close()
    print('\n'.join(diff))

#2
def binary_to_ascii(file) -> str:
#input: Name of binary file as a string
# opens file for reading (t2)
# reads contents of file and stores it in a result string (res)
# open new file to write binary converted ascii text (t3)
# convert binary string (res) into ascii text (ascii_text)
# write text to file
#output: return name of textfile created (asciiFile)
    t2 = open(file, 'r')
    res = t2.read()
    asciiFile = 'ascii_' + file
    t3 = open(asciiFile, 'w')
    binary_int = int(res, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    t3.write(ascii_text)
    t3.close()
    t2.close()
    return asciiFile

#--------------------------ESSENTIAL FUNCTIONS-----------------------------#

#3
def ascii_to_binary(file, size) -> str:
#input: Name of text file as string, Size of new file to be created in bits
# opens file for reading (filename)
# reads contents of file and stores it in a string (fp)
# converts the string fp to an integer array (asc2bi)
# create a string for binary file name (bin_file)
# open bin_file for writing (t1)
# Writes the first 'size' elements of asc2bi to the bin_file
# close both files
#output : Returns name of the binary file created (bin_file) as string
    filename = open(file,'r')
    fp = filename.read()
    asc2bi = ''.join(format(ord(i), '08b') for i in fp)
    bin_file = 'bin_' + file
    t1 = open(bin_file, 'w')
    for count in range(0,size):
        t1.write(asc2bi[count])
    t1.close()
    filename.close()
    return bin_file

#4
def mismatch(file1, file2):
#input : File (Binary, in this case) names as strings
# opens both file1 and file2 for reading (bit1,bit2)
# reads contents of file and stores it in a string (mismatch1, mismatch2)
# compare both strings (of equal length) containing 1's and 0's
# increment counter variable (mismatch) for every difference in characters
#output : print counter variable (print(mismatch))
    iter = 0
    mismatch = 0
    bit1 = open(file1,'r')
    bit2 = open(file2,'r')
    mismatch1 = bit1.read()
    mismatch2 = bit2.read()
    if len(mismatch1) == len(mismatch2):
        for iter in range(0, len(mismatch1)):
            if(mismatch1[iter] != mismatch2[iter]):
                mismatch += 1
    return mismatch

#-------------------------------END OF FUNCTIONS SECTION-----------------------#
#
#
#
#
#-------------------------------MAIN SECTION-----------------------------------#

if __name__ == "__main__":
#input: Text files in .log or .txt format to be compared (inputFile, outputFile)
# CAUTION : No console input for file names. Change lines 102 103
# Console input to enter size of files to be compared (s)
# Convert user input from console in string format to int (size)
# Call function #3 : Create text files of size (size) in .log format
# Call function #4 : Compare the files and store the number of mismatched bits as an integer (mismatchedBits)
#output: print number of mismatched bits (print(mismatchedBits))
    inputFile = 'Correct_Zynq.log'
    outputFile = 'Corrupt_Correct_Zynq.log'
    s = input("\n\nEnter size of file in number of bits\n")
    size = int(s)
    binFile1 = ascii_to_binary(inputFile, size)
    binFile2 = ascii_to_binary(outputFile, size)
    mismatchedBits = mismatch(binFile1, binFile2)
    print('\nNumber of Mismatched bits : ' + str(mismatchedBits))

#----------------------------END OF MAIN SECTION-------------------------------#
#
#
#
#
#-------------------------------OPTIONAL SECTION-------------------------------#

    #   # Call function #2
    #   asciiFile1 = binary_to_ascii(binFile1)
    #   asciiFile2 = binary_to_ascii(binFile2)
    #   # Call function #1
    #   compare_two_files(asciiFile1,asciiFile2)

#---------------------------END OF OPTIONAL SECTION----------------------------#
