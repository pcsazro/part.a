from datetime import datetime

def collectWord(word) :
    title = datetime.today().strftime("%Y-%m-%d")
    with open("search/util/file/"+title+'.txt','a',encoding='utf-8') as f:
        f.write(word+" ")