# Jorge Hernández — Neofetch edition

## Diseño

Adaptación propia inspirada en la referencia https://www.gitskins.com/templates/neofetch: retrato ASCII a la izquierda, datos tipo sistema a la derecha, etiquetas azules, líneas de puntos, bloques de información y paneles de proyectos/tecnologías/actividad. No utiliza el código, servicio de exportación ni recursos de pago de GitSkins.

El hero sustituye la cabecera animada y el objeto JavaScript de la versión anterior. Se prioriza la similitud con Neofetch: composición compacta, fondo GitHub Dark, texto monoespaciado, retrato verde y cursor de terminal estático. No hay animaciones en esta edición.

## Instalar

1. Abre tu repositorio público `JorgHdzCas/JorgHdzCas`.
2. Extrae el ZIP y copia el contenido de `github-profile` en la raíz del repositorio. Reemplaza README.md y añade los recursos y scripts nuevos.
3. Las imágenes antiguas pueden permanecer sin afectar el diseño; este README sólo utiliza los nuevos SVG.
4. Haz commit y push. Comprueba el perfil en escritorio y móvil.

No subas el ZIP sin extraer. El archivo README.md debe quedar en la raíz del repositorio.

## Archivos

- README.md: estructura y enlaces clicables reales.
- profile.json: información editable y snapshot público.
- assets/neofetch.svg y neofetch-mobile.svg: tarjetas principales.
- assets/projects*.svg, skills*.svg y activity*.svg: secciones para escritorio y móvil.
- assets/portrait.txt: retrato ASCII derivado de tu avatar público; no contiene una imagen rasterizada.
- scripts/render.py: regenerar tarjetas con Python 3, sin paquetes externos.
- scripts/update.py: consultar GitHub y actualizar datos y tarjetas.
- .github/workflows/profile-stats.yml: actualización manual desde Actions.

## Editar

Los textos del hero y las métricas se generan desde profile.json y scripts/render.py. Los proyectos se editan en profile.json; sus enlaces y descripciones ampliadas, en README.md. El stack está definido en la función skills de scripts/render.py.

Ejecuta desde la raíz para regenerar tras editar:

```bash
python scripts/render.py
```

Para actualizar las cifras y el calendario con datos públicos:

```bash
python scripts/update.py
```

O usa Actions → Refresh Neofetch profile → Run workflow. Necesita permiso de escritura del workflow para guardar cambios; no necesita token personal. No hay una programación automática activada.

El actualizador consulta la API pública de usuario y el calendario público de GitHub. Si el calendario cambia de formato o una consulta falla, se conserva el snapshot anterior y el comando termina con error. La gráfica muestra los niveles de color reales de los últimos 182 días disponibles, no números inventados. Son columnas consecutivas de siete días; no se muestran etiquetas de día de la semana. No se calculan rachas, estrellas totales ni porcentajes de experiencia.

## Datos pendientes

El correo no es público y se omitió del diseño. No se inventaron enlaces a la clínica ni al bot. Automation lab se retiró porque seguía siendo un proyecto sin documentar. El portafolio, la clínica y el bot se describen según la información que proporcionaste; Soy Kokis Links tiene repositorio y demo públicos confirmados en la conversación.

## Compatibilidad

Las imágenes usan SVG estático y texto monoespaciado; no hay JavaScript, foreignObject, iframes ni CSS embebido en el README. Los enlaces están fuera de los SVG porque una imagen insertada en GitHub no conserva enlaces internos interactivos. Cada panel tiene una variante móvil seleccionada con picture. Si un cliente ignora picture, mostrará la imagen de escritorio escalada.

Los SVG tienen su propio fondo y contraste para verse en tema claro u oscuro. Los textos alternativos y los detalles desplegables aportan contenido accesible. El retrato es arte ASCII, por lo que pierde detalle respecto a la foto.

Se verificaron XML, rutas de imágenes y renderizado local de las tarjetas. No se ha publicado ni modificado tu cuenta GitHub. La vista previa incluida representa los paneles locales; el marco y espaciado de GitHub pueden variar.

## Fuentes

- Referencia visual: https://www.gitskins.com/templates/neofetch
- Perfil y fotografía de referencia: https://github.com/JorgHdzCas
- Datos públicos: https://api.github.com/users/JorgHdzCas
- Calendario público: https://github.com/users/JorgHdzCas/contributions
- Reglas del perfil: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme

Todos los SVG de esta edición se generan localmente. No necesitas suscripción a GitSkins.
