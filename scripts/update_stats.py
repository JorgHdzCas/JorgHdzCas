"""Refresh the local snapshot; failures leave the last good SVG intact."""
import argparse
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import re
import urllib.request

def render(data):
    date = datetime.now(timezone.utc).strftime('%Y-%m-%d UTC')
    body = '<rect width="1000" height="200" rx="16" fill="#0D1117"/>'
    def text(x,y,value,size,color):
        return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-family="monospace">{escape(str(value))}</text>'
    body += text(28,36,'PUBLIC SNAPSHOT / '+data['login'],16,'#00FF9C')
    for x,label,key in [(28,'Public repos','public_repos'),(360,'Followers','followers'),(680,'Public gists','public_gists')]:
        body += text(x,99,data[key],34,'#F0F6FC')+text(x,132,label,18,'#8BA2B5')
    body += text(28,178,'Updated '+date+' / public data only',14,'#8BA2B5')
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 200">'+body+'</svg>'

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('username')
    args=parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',args.username):
        parser.error('Provide a real GitHub username.')
    headers={'Accept':'application/vnd.github+json','User-Agent':'profile-snapshot'}
    if os.environ.get('GH_TOKEN'): headers['Authorization']='Bearer '+os.environ['GH_TOKEN']
    request=urllib.request.Request('https://api.github.com/users/'+args.username,headers=headers)
    with urllib.request.urlopen(request,timeout=30) as response: data=json.load(response)
    for key in ['public_repos','followers','public_gists']:
        if type(data[key]) is not int or data[key]<0: raise ValueError('Invalid API response')
    target=Path(__file__).resolve().parents[1]/'assets'/'analytics.svg'
    temporary=target.with_suffix('.tmp')
    temporary.write_text(render(data),encoding='utf-8')
    temporary.replace(target)
    print('Snapshot updated for '+data['login'])

if __name__=='__main__': main()
