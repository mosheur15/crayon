import questionary
from colorama import Fore
import shutil
import os


TERMUX_HOME_DIR  = os.path.expanduser('~')
TERMUX_FONT_NAME = "font.ttf"
TERMUX_FONT_PATH = f"{TERMUX_HOME_DIR}/.termux/{TERMUX_FONT_NAME}"
TERMUX_RELOAD    = "termux-reload-settings"


def err(msg):
    """
    color the error text
    """
    return f'{Fore.MAGENTA}{msg}{Fore.RESET}'



def chooseInstallOption():
    """
    asks user for install options.
    """
    nerd     = "install nerd font"
    manual   = "install your own"
    question = questionary.select("select a option", choices=[nerd, manual])
    ans      = question.ask()
    
    if ans==None:
        exit(0)

    if ans==nerd:
        return 1
    return 2



def chooseFont(fontList):
    """
    asks user to choose a font name from given list.
    """
    question = questionary.select("select a font Family",choices=fontList)
    return question.ask()



def chooseFlavor(flavors):
    """
    asks user to choose a font flavor from given list.
    """
    question = questionary.select("select a flavor", choices=flavors)
    return question.ask()



def askFilePath():
    """
    asks user to enter ttf file path.
    """

    # questionary path returns None if user press CTRL+C 
    # but at the same time CTRL+D throws EOFError.
    # to prevent this weird behavior TypeError is catched.
    # which means if user pressed CTRL+C then is should return None.
    # since os.path.exists(None) will throw a TypeError it can be 
    # handle by catching it.
    while True:
        try:
            question = questionary.path("ttf file path:")
            ans = question.ask()
        

            if not os.path.exists(ans):
                print (err("\npath don't exists. try again!\n"))
                continue

            if not os.path.isfile(ans):
                print (err(f"\n'{ans}' is not a file!\n"))
                continue

            if not ans.endswith('.ttf'):
                print (err(f"\n'{ans}' is not a ttf file!\n"))
                continue

            return ans
        
        except TypeError:
            exit(0)

        except EOFError:
            print ('\nCanceled by User\n')
            exit (0)


def continueEditing():
    question = questionary.confirm('continue editing font?')
    return question.ask()


def setFont(FilePath):
    if not os.path.exists(FilePath): return False
    if not os.path.isfile(FilePath): return False
    if not FilePath.endswith('.ttf'): return False

    shutil.copy2(FilePath, TERMUX_FONT_PATH)
    os.system(TERMUX_RELOAD)
    return True



def writeFont(content):
    with open(TERMUX_FONT_PATH, 'wb') as file:
        file.write(content)
        os.system(TERMUX_RELOAD)



