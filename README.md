### RUNNING THE PROGRAM

#### Requirements:

Python 3 [ https://www.python.org/downloads/]

#### How to run the file:

* <i>DON'T</i> change <b>main.py</b> filename.
* Refer the code comments under <b>Main Section</b> if changing the names of one or both files to be checked.
* Open terminal/cmd
* Navigate to the directory having the two files and main.py :
      $ python3 main.py

### UNDERSTANDING THE CODE
<b>main.py</b> is divided into 4 sections. The comments on the code help to identify each of these sections, their inputs and outputs, and how they work.
These sections are :

#### Non-Essential functions
* They are used in the optional section of the code.
* You can safely delete this section from <b>main.py</b> for the output.
* A file containing <b>binary</b> characters is converted <b>to text</b> and <b>written to a file</b>
* Two such text files are compared with their differences being the output.

#### Essential Functions
* <i>DON'T</i> delete this section in the code.
* A file containing <b>ASCII text</b> is converted <b>to binary</b> characters and <b>written to a file</b>
* It is important to note :
  - the <b>file created</b> is still a <b>text file</b> and the 1's and 0's are <b>stored as characters</b>(text) in a string and <b>not as integers</b>/numbers/bin
  - The size of the output file is truncated if it is larger than the size specified. Example : If size of input file after conversion is 4000 but size specified is 200, then only the first 200 characters of the input file are written to the new file.
* Two such files are compared with the number of the different characters being the output.

#### Main Function
* <i>DON'T</i> delete this section in the code.
* Takes the filenames as strings for input.
* Calls the essential functions to process the files
* Outputs the number of mismatched bits.

#### Optional Section
* This section has been commented out as it slows down the program.
* Gives better clarity for finding which of the different characters in the original logs are mismatched.
* If required to be used, remember to uncomment and properly indent this section. It is an extension of the main block and should be indented accordingly.
