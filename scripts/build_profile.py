from pathlib import Path
from html import escape
import urllib.request, concurrent.futures, shutil
from PIL import Image, ImageDraw, ImageFont
P=Path(__file__).resolve().parents[1]; A=P/'assets'
def svg(w,h,body):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" rx="16" fill="#0D1117"/>{body}</svg>'
def t(x,y,s,size=16,color='#C9D1D9'):
 return f'<text x="{x}" y="{y}" font-family="monospace" font-size="{size}" fill="{color}" xml:space="preserve">{escape(s)}</text>'
def hero(mobile=False):
 w,h=(560,730) if mobile else (1000,414)
 b=t(28,36,'●  ●  ●',18,'#58A6FF')+t(150,35,'jorge@github:~$ whoami',14)
 px,py=(160,75) if mobile else (32,96)
 b+=f'<rect x="{px}" y="{py}" width="240" height="250" rx="12" fill="#111C25" stroke="#253A48"/>'
 for i,line in enumerate(['   [ PHOTO REQUIRED ]','', '       J H / _','', '  ASCII portrait pending','  Add your reference photo']):
  b+=t(px+12,py+62+i*26,line,13,'#00FF9C' if i==2 else '#8BA2B5')
 x,y=(28,380) if mobile else (310,93)
 lines=[('const developer = {','#58A6FF'),('  name: "Jorge Hernández",','#C9D1D9'),('  role: "Full Stack Developer",','#C9D1D9'),('  location: "Durango, México",','#C9D1D9'),('  portfolio: "jorghrndz.dev",','#00FF9C'),('  focus: [','#C9D1D9'),('    "Web", "Data", "Automation"','#00D9FF'),('  ],','#C9D1D9'),('  mindset: "Build. Learn. Improve."','#C9D1D9'),('};','#58A6FF')]
 for i,(line,c) in enumerate(lines): b+=t(x,y+27*i,line,17,c)
 b+=t(28,h-22,'> Small details. Useful software.',13,'#8BA2B5')
 return svg(w,h,b)
(A/'hero.svg').write_text(hero()); (A/'hero-mobile.svg').write_text(hero(True))
(A/'divider.svg').write_text(svg(1000,12,'<path d="M0 6H1000" stroke="#253A48"/><path d="M0 6H120" stroke="#00FF9C" stroke-width="2"/>'))
(A/'analytics.svg').write_text(svg(1000,160,t(28,40,'PUBLIC GITHUB SNAPSHOT',15,'#00FF9C')+t(28,83,'Waiting for your GitHub username',24)+t(28,124,'No sample numbers. Run scripts/update_stats.py to generate real data.',15,'#8BA2B5')))
font='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
def header(w,mobile=False):
 h=240 if mobile else 220; frames=[]; phrase='Building useful digital experiences.' if not mobile else 'Ideas into useful code.'
 for n in range(len(phrase)+10):
  im=Image.new('RGB',(w,h),'#0D1117'); d=ImageDraw.Draw(im)
  def center(y,s,size,c):
   f=ImageFont.truetype(font,size); d.text(((w-d.textlength(s,font=f))/2,y),s,font=f,fill=c)
  center(28,'HELLO WORLD / HOLA MUNDO',13,'#00FF9C')
  center(64,'Jorge Hernández',32 if mobile else 44,'#F0F6FC')
  center(121,'WEB  /  DATA  /  AUTOMATION',14,'#8BA2B5')
  center(164,phrase[:min(n,len(phrase))]+(' ▌' if n%4<2 else '  '),16 if mobile else 19,'#58A6FF')
  frames.append(im)
 frames[0].save(A/('header-mobile.gif' if mobile else 'header.gif'),save_all=True,append_images=frames[1:],duration=[75]*(len(frames)-1)+[2200],loop=0,optimize=True)
 frames[-1].save(A/('header-mobile-static.png' if mobile else 'header-static.png'))
header(1000); header(560,True)
icons={'html5':'html5-original','css3':'css3-original','javascript':'javascript-original','typescript':'typescript-original','python':'python-original','php':'php-original','react':'react-original','vitejs':'vitejs-original','tailwindcss':'tailwindcss-original','nodejs':'nodejs-original','postgresql':'postgresql-original','supabase':'supabase-original','prisma':'prisma-original','git':'git-original','github':'github-original','vscode':'vscode-original'}
def download(item):
 name,file=item; url=f'https://raw.githubusercontent.com/devicons/devicon/v2.16.0/icons/{name}/{file}.svg'
 with urllib.request.urlopen(url,timeout=30) as r: (A/'icons'/f'{name}.svg').write_bytes(r.read())
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: list(pool.map(download,icons.items()))
with urllib.request.urlopen('https://raw.githubusercontent.com/devicons/devicon/v2.16.0/LICENSE',timeout=30) as r: (A/'icons'/'LICENSE').write_bytes(r.read())
def iconrow(names): return ' '.join(f'<img src="./assets/icons/{n}.svg" width="28" height="28" alt="{n}">' for n in names)
readme='''<!-- Edit text here; visual sources and instructions are in INSTALL.md. -->
<p align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="./assets/header-mobile-static.png">
    <source media="(prefers-reduced-motion: reduce)" srcset="./assets/header-static.png">
    <source media="(max-width: 600px)" srcset="./assets/header-mobile.gif">
    <img src="./assets/header.gif" width="1000" alt="Hola, soy Jorge Hernández. Desarrollo web, datos y automatización.">
  </picture>
</p>

<p align="center"><a href="https://jorghrndz.dev">Explorar mi portafolio ↗</a> · <a href="#featured-projects">Proyectos</a> · <a href="#connect">Contacto</a></p>

<picture>
  <source media="(max-width: 600px)" srcset="./assets/hero-mobile.svg">
  <img src="./assets/hero.svg" width="1000" alt="Jorge Hernández, Full Stack Developer en Durango, México. Enfoque en web, datos y automatización. Retrato ASCII pendiente de fotografía.">
</picture>

## whoami

Soy **Jorge Hernández**, Ingeniero en Sistemas Computacionales. Desarrollo aplicaciones web con React y exploro cómo los datos y la automatización pueden simplificar el trabajo cotidiano.

- **Construyo:** interfaces, aplicaciones y herramientas para problemas reales.
- **Conecto:** frontend, bases de datos y procesos.
- **Aprendo:** desarrollando proyectos, revisando decisiones y cuidando los detalles.

## Tech stack

Herramientas con las que trabajo o que estoy fortaleciendo mediante proyectos; no representan el mismo nivel de dominio.

| Área | Tecnologías |
| :--- | :--- |
'''
rows=[('Languages',['html5','css3','javascript','typescript','python','php'],'HTML5 · CSS3 · JavaScript · TypeScript · Python · PHP · SQL'),('Frontend',['react','vitejs','tailwindcss'],'React · Vite · Tailwind CSS · Responsive design'),('Backend',['nodejs','prisma'],'Node.js · Prisma ORM · JWT'),('Databases',['postgresql','supabase'],'PostgreSQL · Supabase'),('Tools & Workflow',['git','github','vscode'],'Git · GitHub · VS Code · Excel · VBA')]
for name,icons_,labels in rows: readme+=f'| **{name}** | {iconrow(icons_)}<br>{labels} |\n'
readme+='\n<img src="./assets/divider.svg" width="1000" alt="">\n\n## Featured projects\n\n'
projects=[('01 / Personal portfolio','Mi espacio para presentar proyectos, habilidades y formas de contacto.','React · Vite · TypeScript','<a href="https://jorghrndz.dev">Ver sitio ↗</a>'),('02 / Dental clinic manager','Sistema de gestión de citas, pacientes, tratamientos, documentos, usuarios y roles.','React · Tailwind CSS · Prisma · Supabase · JWT','Demo: <code>[DEMO_CLINICA]</code>'),('03 / Social links','Página personal de enlaces con categorías y un fondo espacial animado.','React · Vite · CSS · React Icons','Demo: <code>[DEMO_LINKS]</code>'),('04 / Kokis Bot','Bot de Discord para LOS KOKITOS: comandos de consulta y mensajes de bienvenida.','Node.js · Discord API','Sin demo web; repositorio pendiente.'),('05 / Automation lab','Espacio reservado para documentar herramientas de automatización y seguimiento. Alcance por confirmar.','Excel · VBA','Proyecto por documentar.')]
for i,(name,desc,stack,demo) in enumerate(projects):
 readme+=f'<table>\n<tr><td>\n<h3>{name}</h3>\n<p>{desc}</p>\n<p><sub>{stack}</sub></p>\n<p>{demo} · Repositorio: <code>[REPO_{i+1}]</code></p>\n</td></tr>\n</table>\n\n'
readme+='''## GitHub analytics

<img src="./assets/analytics.svg" width="1000" alt="Resumen de actividad pública de GitHub; pendiente de configurar el usuario.">

<sub>Snapshot local de repositorios públicos, seguidores y gists. Se actualizará al configurar el usuario. Estas cifras no miden habilidad ni incluyen trabajo privado.</sub>

## Connect

Abierto a oportunidades profesionales, colaboraciones y proyectos freelance.

| Canal | Encuéntrame |
| :--- | :--- |
| ↗ Portfolio | [jorghrndz.dev](https://jorghrndz.dev) |
| ⌘ GitHub | `[MI_USUARIO]` |
| ↗ LinkedIn | `[MI_LINKEDIN]` |
| ✉ Email | `[MI_EMAIL]` |

<!-- Reemplaza los marcadores por enlaces reales antes de publicar. -->

<img src="./assets/divider.svg" width="1000" alt="">

<p align="center"><b>Que cada línea acerque una idea a alguien que la necesita.</b><br><sub>Gracias por visitar mi espacio. — Jorge</sub></p>
'''
(P/'README.md').write_text(readme)
print('Visuals, README and icons generated.')
