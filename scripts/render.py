"""Render local SVG cards from editable profile.json and ASCII portrait data. Python 3, no dependencies."""
from pathlib import Path
from html import escape
import json

ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'profile.json').read_text())
A=ROOT/'assets'
BG='#0d1117'; FG='#c9d1d9'; BLUE='#58a6ff'; MUTED='#8b949e'; GREEN='#7ee787'
def text(x,y,s,size=16,color=FG,weight='normal',anchor=None):
    return f'<text x="{x}" y="{y}" font-family="DejaVu Sans Mono,monospace" font-size="{size}" font-weight="{weight}" fill="{color}"'+(f' text-anchor="{anchor}"' if anchor else '')+f' xml:space="preserve">{escape(str(s))}</text>'
def rect(x,y,w,h,fill,rx=0,stroke='none'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'
def svg(w,h,b,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title)}</title>'+b+'</svg>'
def shell(w,h,cmd,window=True):
    b=rect(1,1,w-2,h-2,BG,12,'#30363d')
    if window:
        b+=rect(2,2,w-4,35,'#161b22',11)
        for x,c in [(22,'#ff5f57'),(42,'#febc2e'),(62,'#28c840')]: b+=f'<circle cx="{x}" cy="19" r="5" fill="{c}"/>'
        b+=text(26,76,'$ '+cmd,17,FG,'bold')
    else: b+=text(26,38,D['username']+'@github',15,BLUE,'bold')+text(222,38,':~$ '+cmd,15)
    return b
def section(x,y,label,width):
    return text(x,y,label,16,BLUE,'bold')+f'<path d="M{x+len(label)*10+14} {y-5}H{x+width}" stroke="#30363d"/>'
def hero(mobile=False):
    w,h=(600,1070) if mobile else (1000,602)
    b=shell(w,h,'neofetch',False)
    px,py=(150,68) if mobile else (30,88)
    rows=(A/'portrait.txt').read_text().splitlines()
    for i,row in enumerate(rows):
        b+=f'<text x="{px}" y="{py+i*8}" font-family="DejaVu Sans Mono,monospace" font-size="8.2" textLength="285" lengthAdjust="spacingAndGlyphs" fill="{GREEN}" xml:space="preserve">{escape(row)}</text>'
    x,y,width=(28,548,544) if mobile else (350,88,620)
    b+=section(x,y,D['username']+'@github',width)
    fields=[('Name',D['name']),('Role','Full Stack Developer'),('Location','Durango, México'),('Focus','Web / Data / Automation'),('Since','2024 · GitHub'),('Languages','JS, TS, Python, PHP, SQL')]
    for i,(key,value) in enumerate(fields):
        yy=y+30+i*27
        b+=text(x,yy,key+':',15,BLUE)+text(x+110,yy,'·'*(14 if mobile else 20),13,'#484f58')+text(x+width,yy,value,15,FG,anchor='end')
    yy=y+214;b+=section(x,yy,'About',width)
    for i,line in enumerate(['Ingeniero en Sistemas Computacionales.','Aplicaciones web para problemas reales.','Aprender, construir y cuidar los detalles.']): b+=text(x,yy+26+i*24,line,14)
    yy=y+326;b+=section(x,yy,'Contact',width)
    b+=text(x,yy+28,'GitHub:',15,BLUE)+text(x+width,yy+28,'github.com/'+D['username'],15,anchor='end')
    b+=text(x,yy+54,'Website:',15,BLUE)+text(x+width,yy+54,'jorghrndz.dev',15,anchor='end')
    yy=y+420;b+=section(x,yy,'GitHub Stats',width)
    b+=text(x,yy+29,f"Repos: {D['public_repos']}   Followers: {D['followers']}   Following: {D['following']}",15)
    b+=text(26,h-25,D['username']+'@github:~$ ',14,BLUE,'bold')
    b+=rect(225,h-37,8,15,GREEN)
    b+=text(w-25,h-25,D['updated'],11,MUTED,anchor='end')
    return svg(w,h,b,'Jorge Hernández — perfil Neofetch')

def projects(mobile=False):
    w,h=(600,555) if mobile else (1000,370)
    b=shell(w,h,'ls ~/projects')
    for i,p in enumerate(D['projects']):
        y=124+i*(102 if mobile else 60)
        b+=text(26,y,'drwx',13,GREEN)+text(89,y,p['slug']+'/',16,BLUE,'bold')
        if mobile:
            b+=text(89,y+25,p['short'],13,MUTED)+text(89,y+48,p['stack'],12,FG)
        else:
            b+=text(380,y,p['short'],13,MUTED)+text(972,y,p['label'],11,GREEN,anchor='end')
        b+=f'<path d="M26 {y+(66 if mobile else 27)}H{w-26}" stroke="#21262d"/>'
    b+=text(26,h-22,'4 projects · web, community & workflow',12,MUTED)
    return svg(w,h,b,'Proyectos de Jorge Hernández')

def skills(mobile=False):
    w,h=(600,440) if mobile else (1000,270)
    b=shell(w,h,'cat ~/stack.conf')
    groups=[('languages','HTML · CSS · JavaScript · TypeScript','Python · PHP · SQL'),('frontend','React · Vite · Tailwind CSS','Responsive UI'),('backend','Node.js · Prisma ORM · JWT','PostgreSQL · Supabase'),('workflow','Git · GitHub · VS Code','Excel · VBA')]
    for i,(k,v,v2) in enumerate(groups):
        y=115+i*(73 if mobile else 33)
        b+=text(26,y,k,14,BLUE)
        if mobile:b+=text(26,y+22,v,14)+text(26,y+42,v2,14,MUTED)
        else:b+=text(160,y,v+' · '+v2,14)
    b+=text(26,h-20,'Herramientas en práctica y aprendizaje continuo.',12,MUTED)
    return svg(w,h,b,'Tecnologías y herramientas')

def activity(mobile=False):
    w,h=(600,240) if mobile else (1000,255)
    b=shell(w,h,'git log --contributions')
    days=D.get('contributions',[])[-182:]
    if days:
        # Actual GitHub contribution levels, ordered chronologically.
        b+=text(26,108,'Actividad pública · últimas 26 semanas',13,MUTED)
        size,gap=(12,4) if mobile else (13,4)
        for i,d in enumerate(days):
            col=i//7;row=i%7
            b+=rect(26+col*(size+gap),123+row*(size+gap),size,size,['#161b22','#0e4429','#006d32','#26a641','#39d353'][d['level']],2)
        if not mobile:
            b+=text(560,146,'PUBLIC REPOSITORIES',12,MUTED)+text(560,181,D['public_repos'],28,BLUE,'bold')
            b+=text(785,146,'FOLLOWERS',12,MUTED)+text(785,181,D['followers'],28,GREEN,'bold')
    else:
        b+=text(26,120,'Repos públicos  '+str(D['public_repos']),18,BLUE)+text(26,154,'Seguidores      '+str(D['followers']),18,GREEN)
    return svg(w,h,b,'Actividad pública de GitHub; snapshot '+D['updated'])

def main():
    for name,fun in [('neofetch',hero),('projects',projects),('skills',skills),('activity',activity)]:
        for mobile in [False,True]:(A/(name+('-mobile' if mobile else '')+'.svg')).write_text(fun(mobile))
if __name__=='__main__': main()
