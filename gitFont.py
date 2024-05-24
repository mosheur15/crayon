
import requests
import json

class Font:
    def __init__(self, username="mosheur15", repo="nerdFonts_termux", branch="main", mapName="gitFontMap.json"):
        self.username = username
        self.repo = repo
        self.branch = branch
        self.mapName = mapName
        self.linkPlaceholder = 'https://raw.githubusercontent.com/$USERNAME/$REPONAME/$BRANCH/$FILEPATH'

    def mapUrl(self):
        link = self.linkPlaceholder
        link = link.replace("$REPONAME", self.repo)
        link = link.replace("$USERNAME", self.username)
        link = link.replace("$BRANCH", self.branch)
        link = link.replace("$FILEPATH", self.mapName)
        return link

    def fontUrl(self, family, flavor):
        path = f'{family}/{flavor}'
        link = self.linkPlaceholder
        link = link.replace("$REPONAME", self.repo)
        link = link.replace("$USERNAME", self.username)
        link = link.replace("$BRANCH", self.branch)
        link = link.replace("$FILEPATH", path)
        return link
 

    def getMap(self):
        url = self.mapUrl()
        res = requests.get(url)
        return json.loads(res.text)

    def getFont(self, family, flavor):
        url = self.fontUrl(family, flavor)
        res = requests.get(url)
        return res.content

