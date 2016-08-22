#!/usr/bin/python
import sys
from colorama import init, Fore
init()


strPidgey = "Pidgey"
strCaterpie = "Caterpie"
strWeedle = "Weedle"
strRattata = "Rattata"


valPWC = 12
valRat = 25

varVal = 0
varCount = 0
x = 1
varPoke = ''
print (Fore.RED + "      ##############################################")
print (Fore.RED + "      #" + Fore.CYAN + "   _____      _         _____      _        " + Fore.RED + "#")
print (Fore.RED + "      #" + Fore.CYAN + "  |  __ \    | |       / ____|    | |       " + Fore.RED + "#")
print (Fore.RED + "      #" + Fore.CYAN + "  | |__) |__ | | _____| |     __ _| | ___   " + Fore.RED + "#")
print (Fore.RED + "      #" + Fore.CYAN + "  |  ___/ _ \| |/ / _ \ |    / _` | |/ __|  " + Fore.RED + "#")
print (Fore.RED + "      #" + Fore.CYAN + "  | |  | (_) |   <  __/ |___| (_| | | (__   " + Fore.RED + "#")
print (Fore.RED + "      #" + Fore.CYAN + "  |_|   \___/|_|\_\___|\_____\__,_|_|\___|  " + Fore.RED + "#")
print (Fore.RED + "      ##############################################")
print (Fore.RESET + "Welcome To PokeCalc, a CLI pokemon lucky egg use calculator! \n \nPlease Select the pokemon(s) you plan to use.")
print "1. Pidgey"
print "2. Caterpie"
print "3. Weedle"
print "4. Rattata"

varChoice = raw_input('Please select an option by pressing the corresponding number \nor press ''Enter'' to exit.\n'
                      'Selection: ')
while x == 1:
    try:
        if varChoice in ["1", "2", "3"]:
            if varChoice == "1":
                varPoke = strPidgey
            elif varChoice == "2":
                varPoke = strCaterpie
            elif varChoice == "3":
                 varPoke = strWeedle
            varVal = valPWC
            x = 0
        elif varChoice == "4":
            varPoke = strRattata
            varVal = valRat
            x = 0
        elif varChoice == "":
            sys.exit()
        elif varChoice not in ['1', '2', '3', '4', '']:
            raise Exception('Uh Oh...')
    except Exception as e:
        varChoice = raw_input('Let''s try this again shall we, please make a VALID selection: ')

if varVal == valPWC:
    varCount = raw_input('\nYou have selected a %s, a 12 candy evolution \nPlease enter how many of this pokemon '
                         'you have: ' % varPoke)

elif varVal == valRat:
        varCount = raw_input('\nYou have selected a %s, a 25 candy evolution \nPlease enter how many of this pokemon'
                             ' you have: ' % varPoke)

varCandy = raw_input('\nand how many of the corresponding candy: ')

if int(varCandy) >= (int(varCount)*int(varVal)):
    print "\nGreat! looks like you have enough candy!\n\nIt will take you %s " \
          "minutes to evolve that many %s." % ((int(varCount)*0.5), varPoke)
    print "\nWe recommend collecting %s more %ss and %s more %s candy so you get the most use of your " \
          "lucky egg." % (60-(int(varCount)*0.5), varPoke,
                          ( (60*int(varVal))-(int(varCandy)-(int(varVal)*int(varCount)))), varPoke)
elif int(varCandy) < (int(varCount)*int(varVal)):
    print "\nHmm, almost enough, looks like you need %s more %s candy to evolve all of the %s you " \
          "have." % ((int(varCount)*int(varVal)-int(varCandy)), varPoke, varPoke)
    print "\nCurrently you can evolve only %s %s(s)" % ((int(varCandy)/int(varVal)), varPoke)
    print "\nThis would take %s minutes, leaving you with %s minutes remaining on your lucky " \
        "egg" % (((int(varCandy)/int(varVal))*0.5),30-((int(varCandy)/int(varVal))*0.5))
    print "\nWe recommend collecting %s more %ss and %s more %s candy so you get the most use of your " \
        "lucky egg." % (60-(int(varCount)*0.5), varPoke,
                        ( (60*int(varVal))-(int(varCandy)-(int(varVal)*int(varCount)))), varPoke)
raw_input()
