from utils.common import *
from bs4 import BeautifulSoup
import utils.database
import urllib3
import os

try:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except:
    pass

os.chdir(os.path.dirname(__file__))
db = utils.database.DBTool('./fofa.db')
url = "https://fofa.so/about_client"

html = http_request_get(url)
bs = BeautifulSoup(html.text, 'lxml')
poc = bs.select('.poc_row li')
ob = []
res = []
T = db.executeQuery('select * from data order by ID desc')
index = T.fetchall()[0][1]

for i, j in enumerate(poc):
    if i % 4 == 0 and i != 0:
        ob.append(tuple(res))
        res = []
    if j.a:
        x = j.a.string
    else:
        x = j.string
    if x == index:
        exit()
    res.append(x)

sql = 'insert into data (POC_NAME, POC_DETAIL, HARM, RULE) values (?,?,?,?)'
T = db.executeUpdate(sql, ob)
db.close()

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))