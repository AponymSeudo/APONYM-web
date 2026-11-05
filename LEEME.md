# aponym-web — sitio público de APONYM

Sitio estático de una sola página. Sin framework, sin build, sin JavaScript, sin
dependencias y sin terceros: solo HTML, una hoja de estilos y los PNG de marca.

## Cómo verlo

Doble clic en `index.html`. Se abre en el navegador; no necesita servidor.

Para publicarlo después en GitHub Pages, subir esta carpeta tal cual a un repo
`aponym-web` y activar Pages en la raíz.

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` | La landing completa (7 bloques). |
| `estilos.css` | Toda la hoja de estilos, con la paleta del programa. |
| `privacidad.html` | Política mínima: sin cookies, sin analítica, sin formularios. |
| `eula.html` | Condiciones de uso. **Generado**: no editar a mano. |
| `herramientas/eula_html.py` | Regenera `eula.html` desde `../ANONIMIZADOR/docs/EULA.md`. |
| `assets/` | Wordmark claro y oscuro, isotipo, icono y captura real del panel. |
| `robots.txt` | `Disallow: /` hasta que se autorice publicar. |

Regenerar el EULA cuando cambie el del producto:

```
python herramientas\eula_html.py
```

## Decisiones que tomé para esta primera versión

- **Tipografía del sistema**: Georgia para títulos y Segoe UI para texto, igual que el
  panel. Cero descargas, cero licencias y ninguna petición a terceros. Si más adelante
  quieres un serif propio, se auto-hospeda un `.woff2` y se cambia en una línea.
- **Captura real del panel**, recortada para mostrar solo las dos etapas y las acciones.
  No inventé ninguna interfaz.
- **Sin precios** y **sin nombrar a la Clínica** (regla del brief).
- **Contacto**: correo y WhatsApp tomados del EULA. Si no quieres el teléfono público,
  se borra del `index.html` en un minuto.
- **`noindex` + `robots.txt`**: el sitio no se indexa hasta que lo autorices.

## Pendiente antes de publicar

1. **Dominio**: `aponym.cl` estaba libre al 29-10. Registrarlo en NIC y apuntar Pages.
2. **Revisión tuya** de los textos (es lo que va a leer un abogado).
3. **Deuda menor de marca**: la carpeta de mapas sigue en %LOCALAPPDATA%\\Anonimizador;
   es invisible para el usuario y se renombra en una pasada aparte (mueve datos reales).
4. **Autorización escrita** si alguna vez se nombra a la Clínica.
5. **Precio**: hoy no hay sección; si lo quieres, va como «a consultar» o cifra.

