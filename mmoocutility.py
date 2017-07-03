import sys
import time

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

mmoocSleep = 7

#Colors from https://gist.github.com/vratiu/9780109
Color_Off="\033[0m"

# Bold High Intensty
BIBlack="\033[1;90m"      # Black
BIRed="\033[1;91m"        # Red
BIGreen="\033[1;92m"      # Green
BIYellow="\033[1;93m"     # Yellow
BIBlue="\033[1;94m"       # Blue
BIPurple="\033[1;95m"     # Purple
BICyan="\033[1;96m"       # Cyan
BIWhite="\033[1;97m" # White


# High Intensty backgrounds
On_IBlack="\033[0;100m"   # Black
On_IRed="\033[0;101m"     # Red
On_IGreen="\033[0;102m"   # Green
On_IYellow="\033[0;103m"  # Yellow
On_IBlue="\033[0;104m"    # Blue
On_IPurple="\033[10;95m"  # Purple
On_ICyan="\033[0;106m"    # Cyan
On_IWhite="\033[0;107m" # White



def MMOOCPASSED():
    sys.stdout.write(On_IGreen)
    sys.stdout.write("PASSED")
    sys.stdout.write(Color_Off)
    sys.stdout.write("\n")

def MMOOCFAILED():
    sys.stdout.write(On_IRed)
    sys.stdout.write("FAILED")
    sys.stdout.write(Color_Off)
    sys.stdout.write("\n")

def MMOOCWAIT():
    for x in range(0, mmoocSleep):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
