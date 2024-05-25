import os
import questionary
import gitFont
import shutil

def askForOption():
    nerd = "install nerd font"
    manual = "install your own"
    question = questionary.select("select a option", choices=[nerd, manual])
    ans = question.ask()
    
    if ans==nerd:
        return 1
    return 2



def chooseFont(fontList):
    question = questionary.select("select a font Family",choices=fontList)
    return question.ask()



def chooseFlavor(flavors):
    question = questionary.select("select a flavor", choices=[flavors])
    return question.ask()


def askPath():
    question = questionary.path("ttf file path:")
    return question.ask()


def main():
    ans = askForOption()
    if ans == 1:
        nerdFont = gitFont.Font()
        fontMap = nerdFont.getMap()
        fontNames = [i for i in fontMap.keys()]

        choice = chooseFont(fontNames)
        flavor = chooseFont(fontMap[choice])
        font = nerdFont.getFont(choice, flavor)
        fontPath = os.path.expanduser('~')
        fontPath = f'{fontPath}/.termux/font.ttf'

        with open(fontPath, "wb") as f:
            f.write(font)
            os.system("termux-reload-settings")

    else:
        fontPath = os.path.expanduser('~')
        fontPath = f'{fontPath}/.termux/font.ttf'
        path = askPath()
        shutil.copy2(path, fontPath)
        os.system("termux-reload-settings")

main()

