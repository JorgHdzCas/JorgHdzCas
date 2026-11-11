"""Fetch public GitHub data, preserve existing data on failure, and render the cards."""
from pathlib import Path
from datetime import datetime,timezone
from html.parser import HTMLParser
import json, urllib.request, os
from render import main, D
ROOT=Path(__file__).resolve().parents[1]
class Calendar(HTMLParser):
    def __init__(self): super().__init__();self.days=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('data-date') and a.get('data-level') in ['0','1','2','3','4']:
            self.days.append({'date':a['data-date'],'level':int(a['data-level'])})
def get(url):
    headers={'User-Agent':'JorgHdzCas-profile'}
    if url.startswith('https://api.github.com/') and os.environ.get('GH_TOKEN'):headers['Authorization']='Bearer '+os.environ['GH_TOKEN']
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30) as r:return r.read()
def update():
    user=D['username']; data=json.loads(get('https://api.github.com/users/'+user))
    for key in ['public_repos','followers','following']:D[key]=data[key]
    calendar=Calendar();calendar.feed(get('https://github.com/users/'+user+'/contributions').decode())
    if not calendar.days:raise ValueError('GitHub calendar unavailable; previous files preserved.')
    D['contributions']=sorted(calendar.days,key=lambda d:d['date'])[-182:]
    D['updated']=datetime.now(timezone.utc).strftime('%Y-%m-%d UTC')
    tmp=ROOT/'profile.tmp';tmp.write_text(json.dumps(D,ensure_ascii=False,indent=2));tmp.replace(ROOT/'profile.json');main()
if __name__=='__main__':update()
