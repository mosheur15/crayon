import gitFont
import utils


def main():
    while True:
        ans = utils.chooseInstallOption()
        if ans==1:
            nerdFont   = gitFont.Font()
            fontmap    = nerdFont.getMap()
            fontFamily = utils.chooseFont([i for i in fontmap])
            flavor     = utils.chooseFlavor(fontmap[fontFamily])
            font       = nerdFont.getFont(fontFamily, flavor)
            utils.writeFont(font)            
            
        else:
            path = utils.askFilePath()
            utils.setFont(path)
        
        if not utils.continueEditing():
            exit(0)
main()

