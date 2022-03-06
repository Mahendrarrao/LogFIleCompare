# File content mismatch checker and plotter

## What does it do?
Python code to compare two text files, convert them to binary bits and compare the number of bits mismatched between them while specifying the total number of bits from the start that are to be compared.

<b>Input</b> :  

        * <input filename 1>.log
        * <input filename 2>.log
        * Number of bits compared (NOBC)

- Input two text files of .log format
- Input total number of bits to be compared between the two files.

<b>Action</b> :
- Converts the text content to 1 and 0 binary bits.
- Entire file contents are converted but the resulting binary files generated for both files will have the NOBC bits written to them.
- The binary files which are of equal length are compared and the number of mismatched bits are tracked.

<b>Output</b> :

        * Total number of mismatched bits
        * Line graph of occurence of mismatched bits across NOBC bits.

### Running the program

#### Requirements:
Python 3 [ https://www.python.org/downloads/]

#### How to run the file:
- <i>DON'T</i> change <b>main.py</b> filename.
- Refer the code comments under <b>Main Section</b> if changing the names of one or both files to be checked.
- Open terminal/cmd
- Navigate to the directory having the two files and main.py :

          $ python3 main.py
#####  Update:
- pip is a python package that needs to be installed so that we can import and run the matplotlib python library. Follow the below steps to install pip and the matplotlib python library:
  - Verify if pip is installed in your system with the following command:
          $ pip --version
  - If pip is not installed, you will get an output saying <i>'pip' is not recognized</i>. There's enough resources online to help you install the latest version of pip. If you don't have the time, You can run the get-pip.py file with this command (This is not preferred since the file is not the latest version):

          $ python get-pip.py
  - Once pip is installed and verified, run the below command to install the library for the graphs and plots:

          $ pip install matplotlib

### Understanding the code
<b>main.py</b> is divided into 4 sections. The comments on the code help to identify each of these sections, their inputs and outputs, and how they work.
These sections are :

#### Non-Essential functions
* They are used in the [Optional Section](https://github.com/Mahendrarrao/LogFIleCompare#optional-section) of the code.
* You can safely delete this section from <b>main.py</b> for the output.
* A file containing <b>binary</b> characters is converted <b>to text</b> and <b>written to a file</b>
* Two such text files are compared with their differences being the output.

#### Essential functions
* <i>DON'T</i> delete this section in the code.
* A file containing <b>ASCII text</b> is converted <b>to binary</b> characters and <b>written to a file</b>
* It is important to note :
  - the <b>file created</b> is still a <b>text file</b> and the 1's and 0's are <b>stored as characters</b>(text) in a string and <b>not as integers</b>/numbers/bin
  - The size of the output file is truncated if it is larger than the size specified. Example : If size of input file after conversion is 4000 but size specified is 200, then only the first 200 characters of the input file are written to the new file.
* Two such files are compared with the number of different characters being the output.

#### Main Function
* <i>DON'T</i> delete this section in the code.
* Takes the filenames as strings for input.
* Calls the essential functions to process the files
* Outputs the number of mismatched bits in numerical and graphical form.

#### Optional Section
* This section has been commented out as it slows down the program.
* Gives better clarity for finding which of the different characters in the original logs are mismatched.
* If required to be used, remember to uncomment and properly indent this section. It is an extension of the main block and should be indented accordingly.

##### Optional features
* [Non-Essential functions](https://github.com/Mahendrarrao/LogFIleCompare#non-essential-functions)
* Graphing function in Essential functions -> ascii_to_binary (Lines 74-81/main.py)
  - This section has been commented out since it is CPU intensive and inefficient for comparing 1000000+ bits.
  - Uncomment this section for cases where smaller number of bits are to be compared and open the .svg file in a browser for best results.
