import requests
import sys
import webbrowser
import urllib
tag="" #tag is a variable that holds the programming language of the error, so that the search of the stack overflow api can be more precise
for line in sys.stdin:
        if "error:" in line:#logic to determine if compiled program has errors and to determine what programming language the compiled program is written in
                if ".c" in line:
                        tag="c"
                elif ".py" in line:
                        tag="python"
                elif ".java" in line:
                        tag="java"
                else:
                        tag=""
                index=line.find("error:")#locate the name of your error
                search=line[index:]
                chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
                url="https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&q="+search+"&accepted=True&tagged="+tag+"&site=stackoverflow"
                url= urllib.quote(url)# clean up url for spaces and special characters
                r=requests.get("https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&q="+search+"&accepted=True&tagged="+tag+"&site=stackoverflow")
                print(r.status_code)
                response=r.json()
                #get top 3 search results from calling stackoverflow api
                url1=(response["items"][0]["link"])
                url2=(response["items"][1]["link"])
                url3=(response["items"][2]["link"])
                #open all three search results in default web browser
                webbrowser.open(url1)
                webbrowser.open_new_tab(url2)
                webbrowser.open_new_tab(url3)
