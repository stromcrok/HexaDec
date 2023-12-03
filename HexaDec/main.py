#!/usr/bin/python3

def run(): #Function
    while True: #Do Loop
        try:
            opTion = input("\n Do you want to (E)ncode or (D)ecode ? ") #Ask for encode or decode

            enCode = ["E", "e", "Encode", "encode"]  #Any input in here will go to Encode
            deCode = ["D", "d", "Decode", "decode"]  #Any input in here will go to Decode

            if opTion in enCode: #Checking Input in enCode
                string = input(" Give a string : ").encode("utf-8") #Requests String
                print(" Here is your Hex:\n", string.hex()) #Display Encode String
                continue

            elif opTion in deCode: #Checking Input in deCode
                hex = input(" NO-SPACE!\n Give a Hex : ").strip(" ") #Requests Hex and (strip) remove space in input
                print(" Here is your string:\n", bytes.fromhex(hex).decode("utf-8")) #Display Decoded Hex
                continue

            else: #If none of the input in enCode or deCode
                print("\n Try Again\n")
                continue

        except ValueError: #If user give non-hexadecimal input
            print("\n Non-hexadecimal input detected")
            break

        except KeyboardInterrupt: #If user press Ctrl+C
            print("\n Stopped")
            break

        except: #If error
            print("\n An error occurred",)
            break

if "__main__" == __name__:
    print("\n","="*40, "\n Tools Encode/Decode For Hexadecimal\n Author: stromcrok\n", "="*40)
    run()
    exit() #Exit