#
import binascii
import difflib


#input the file names. Change file names on li 7,8,43 appropriately
f = open('Correct_Zynq.log', 'r')
testSample1 = open('Corrupt_Correct_Zynq.log', 'r')

#Simple comparision of two log files
contents = f.read()
test1 = testSample1.read()
diff = difflib.ndiff(test1.splitlines(),contents.splitlines())
print('\n'.join(diff))
##Convert the file contents from ascii to binary
fres = ''.join(format(ord(i), '08b') for i in contents)
testSample1.close()
f.close()

#Specifying bit length
s = input("\n\nEnter size of file in number of bits\n")
size = int(s)

#Writing binary contents to new bin file till bit length is reached
t1 = open('trunc_correct_bin.log', 'w')
for count in range(0,size):
    t1.write(fres[count])
t1.close()

#convert binary to ascii and write to file
t2 = open('trunc_correct_bin.log', 'r')
res = t2.read()
t3 = open('trunc_correct.log', 'w')
binary_int = int(res, 2)
byte_number = binary_int.bit_length() + 7 // 8
binary_array = binary_int.to_bytes(byte_number, "big")
ascii_text = binary_array.decode()
t3.write(ascii_text)
t3.close()
t2.close()

#truncate corrupt binary file contents
t4 = open('Corrupt_Correct_Zynq.log', 'r')
trunc = t4.read()
tres = ''.join(format(ord(j), '08b') for j in trunc)
t5 = open('trunc_corrupt_Hello_bin.log','w')
for c in range(0,size):
    t5.write(tres[c])
t5.close()
t4.close()

#(redundant) convert binary to ascii and write truncated contents to file
t6 = open('trunc_corrupt_Hello_bin.log', 'r')
res1 = t6.read()
t7 = open('trunc_corrupt_Hello.log', 'w')
binary_int1 = int(res1, 2)
byte_number1 = binary_int1.bit_length() + 7 // 8
binary_array1 = binary_int1.to_bytes(byte_number1, "big")
ascii_text1 = binary_array1.decode()
t7.write(ascii_text1)
t7.close()
t6.close()

#(redundant) compare truncated files
final1 = open('trunc_corrupt_Hello.log','r')
final2 = open('trunc_correct.log','r')
filec1 = final1.read()
filec2 = final2.read()
diff1 = difflib.ndiff(filec1.splitlines(),filec2.splitlines())
print('\n'.join(diff1))

#number of mismatched bytes
iter = 0
mismatch = 0
bit1 = open('trunc_correct_bin.log','r')
bit2 = open('trunc_corrupt_Hello_bin.log','r')
mismatch1 = bit1.read()
mismatch2 = bit2.read()
if len(mismatch1) == len(mismatch2):
    for iter in range(0, len(mismatch1)):
        if(mismatch1[iter] != mismatch2[iter]):
            print(mismatch1[iter])
            mismatch += 1
print('\nNumber of Mismatched bits : ')
print(mismatch)
