#!/usr/bin/env python3
import pycurl
from io import BytesIO
import re
import json
from pathlib import Path
import glob, os, subprocess
import sys
def getPage(link: str) -> str:
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, link)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.TIMEOUT, 10)
        c.setopt(c.USERAGENT,"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0")
        try:
            c.perform()
            c.close()
            body = buffer.getvalue()
            doc = body.decode('utf-8')
        except:
            doc=None
        return(doc)

if len(sys.argv) < 2:
    print("Not enough arguments, first one should be your MAL name and second (optional) should be the target folder")
doc=json.loads(getPage("https://themes.moe/api/mal/"+sys.argv[1]))
opMatcher = re.compile(r"OP([0-9]*).*")
res=dict()
for anime in doc:
    name = anime["name"]
    if anime["watchStatus"] != 2:
        continue
    for theme in anime["themes"]:
        if (m:=opMatcher.match(theme["themeType"])) is not None:
            if (m.group(1) == ""):
                opNumber = 1
            else:
                opNumber=m.group(1)
            title = name.replace(":","").replace(" ","_").replace("/","_")+"-"+"OP"+str(opNumber)
            # Check for already existing op because of versions
            if title not in res:
                # We save the title so we can add it up later. We want to use the simple title for easy key checking.
                res[title]=[theme["themeName"],theme["mirror"]["mirrorURL"]]

res={title+"-"+res[title][0].replace(":","").replace(" ","_").replace("/","_"):res[title][1]  for title in res}

destFolder = "Animes" if len(sys.argv) == 2 else sys.argv[2]
Path(destFolder).mkdir(parents=True, exist_ok=True)
os.chdir(destFolder)

files= set(map(lambda x: x.replace(".mp3"  ,""),glob.glob("*.mp3")))
files2 = set(map(lambda x: x.replace(".webm"  ,""),glob.glob("*.webm")))

files= files.union(files2)

keys = [el for el in res]
keys=set(keys)
missing=keys.difference(files)
while len(missing)>0 :
    anime=missing.pop()
    print(str(len(missing))+" animes remaining")
    if not (os.path.isfile(anime+".webm") or os.path.isfile(anime+".mp3")):
        with open(anime+".webm","wb") as f:
            print("Downloading: " + anime)
            try:
                c = pycurl.Curl()
                c.setopt(c.URL,res[anime])
                c.setopt(c.FOLLOWLOCATION, True)
                c.setopt(c.TIMEOUT, 20)
                c.setopt(c.USERAGENT,"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0")
                c.setopt(c.WRITEDATA, f)
                c.perform()
                c.close()
            except pycurl.error:
                print("Failed, retrying:"+anime)
                missing.add(anime)
        


        

    





        
            
            
