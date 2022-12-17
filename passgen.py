
while True:
    try:
        import os
        import time
        import random
        break
    except ImportError:
        print("[!] WARNING! COULD NOT RUN SCRIPT DUE TO AN IMPORT ERROR, PLEASE REFER TO help.txt TO FIX IT.")
        input("Press any key and enter to kill script: ")
        quit()

#provided combinattions
low_password_body = ["apple", "mango", "india", "compare", "blue", "physical", "beach", "beautiiful", "children", "sample", "camphor", "love", "sweden", "hijackme", "stopme", "kitebite"]

moderate_password_body = ["dorTos", "ciRcle", "goOgle", "bottLE", "StUdLyCaPs", "whAtiN", "puPpYlOver", "feEtMan","stAcK", "ExchANgE" "ranDOm", "wHymUstYou", "bEreMember", "lOlcAtRun", "EroPeN" "KobRa", "dRopMe"]

high_password_body = ["iHaveAbAs", "eXTENDED", "gNERERATOR", "eXCePTioNaLLy", " SeNTeNCe", "PisHOkiy", "PHnjIkoJG", "RukkOUsiNa", "pInerIne", "yUirIN", "nOTatiOn ", "oGErCuHog", "reQuIRes", " efFOrThigHME", " aDdiTiOnAl", "olMoOseRuCL", "kaOYfhaTT", "kaOPHTaj"]

low_password_ending = ["52", "56", "72", "3", "89", "32", "96", "64", "33", "76", "43", "48", "68", "11", "9", "31", "41", "95", "55", "33", "99", "88", "66", "22"]

moderate_password_ending = ["@8*2", "#65%", "*67", "954", "42", "&683%", "%46#2", "97%1@", "5#$@", "32#%", "9&#&", "$#2@", "32&@", "$%31", "7%7", "89##$", "64#$%"]

high_password_ending = ["#*4@1!", "!5$#", "567&" , "6$83%", "6@#1", "67%*4!", "9%$4", "56$43@", "$#4524", "@#$23$@", "35$%@%#", "&*789", "@#$4%4", "45$%#", "$@2452", "34#%$@", "34@#$"]
print("""______                                   _ _____             __
| ___ \                                 | |  __ \                  __|  |__
| |_/ /_ _ ___ _____      _____  _ __ __| | |  \/ ___ _ __   ___  _| _   __|____  ____
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | __ / _ \ '_ \ /  __'  _ /  |   __ \/  '__|
| | | (_| \__ \__ \\ V  V / (_) | | | (_| | |_\ \  __/ | | |  | |  (_|   |__(__) |   |
\_|  \__,_|___/___/ \_/\_/\___/|_|  \__,_|\____/\___|_| |_|_|   \___,_|_ ___)___ /__|
                                                                   """)
print("WELCOME")
how_messed_up = input("HOW DO YOU WANT YOUR PASSWORD TO BE? (high, moderate and low, Default is low): ")

if how_messed_up == "high":
    print(" Generating high password...")
    password_body_high=random.choice(high_password_body)
    password_endings_high=random.choice(high_password_ending)
    print(" Password Generated! Your password is: " + password_body_high + password_endings_high)
    save_to_file_high = input("[*] Would you like to save it to a file? (y/n): ")
    full_pass_high = password_body_high + password_endings_high

    if save_to_file_high == "y":
        print("WARNING!PLEASE SEARCH YOUR SYSTEM FOR THE FILE")
        file = open("Saved_Password.txt", "w+")
        file.write(full_pass_high)
        file.close()
        print(" Password saved as Saved_Password.txt")
        print(" File saved successfully!")


if how_messed_up == "moderate":
    print(" Generating moderate password...")
    password_body_moderate=random.choice(moderate_password_body)
    password_endings_moderate=random.choice(moderate_password_ending)
    print(" Password Generated! Your password is: " + password_body_moderate + password_endings_moderate)
    save_to_file_moderate = input("[*] Would you like to save it to a file? (y/n): ")
    full_pass_moderate = password_body_moderate + password_endings_moderate

    if save_to_file_moderate == "y":
        print("WARNING!PLEASE SEARCH YOUR SYSTEM FOR THE FILE")
        file = open("Saved_Password.txt", "w+")
        file.write(full_pass_moderate)
        file.close()
        print(" Password saved as Saved_Password.txt")
        print(" File saved successfully!")


if how_messed_up == "low":
    print(" Generating low password...")
    password_body_low=random.choice(low_password_body)
    password_endings_low=random.choice(low_password_ending)
    print(" Password Generated! Your password is: " + password_body_low + password_endings_low)
    save_to_file_low = input("[*] Would you like to save it to a file? (y/n): ")
    full_pass_low = password_body_low + password_endings_low

    if save_to_file_low == "y":
        print("[!] WARNING!PLEASE SEARCH YOUR SYSTEM FOR THE FILE")
        file = open("Saved_Password.txt", "w+")
        file.write(full_pass_low)
        file.close()
        print("Password saved as Saved_Password.txt")
        print("File saved successfully!")
    
