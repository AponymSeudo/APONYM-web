# Publicar el sitio — pasos exactos

Todo el sitio ya está armado y es estático: **no necesita build**. Falta subirlo, activar
GitHub Pages y apuntar el dominio.

## 0. Datos que hay que fijar

| Dato | Valor |
|---|---|
| Dominio | `aponym.cl` (confirmar: hoy no tiene registros DNS) |
| Repo | `aponym-web` en GitHub, **público** (Pages gratis exige repo público) |
| Cuenta | la misma de `Dvmyvn-hash` |

Cuando el dominio esté confirmado, ejecutar desde esta carpeta:

```
echo aponym.cl > CNAME
```

Y recién al publicar, quitar el `noindex`:

- En `index.html`, `privacidad.html`, `eula.html` y `404.html`: borrar la línea
  `<meta name="robots" content="noindex, nofollow">`.
- En `robots.txt`: cambiar `Disallow: /` por `Allow: /`.

## 1. Crear el repositorio y subir

Desde GitHub: **New repository** → nombre `aponym-web` → **Public** → sin README.

Después, en esta carpeta:

```
git init
git add .
git commit -m "Sitio APONYM v1"
git branch -M main
git remote add origin https://github.com/Dvmyvn-hash/aponym-web.git
git push -u origin main
```

## 2. Activar GitHub Pages

En el repo: **Settings → Pages**

- Source: **Deploy from a branch**
- Branch: **main** / carpeta **/ (root)**
- Save.

En uno o dos minutos el sitio queda en `https://dvmyvn-hash.github.io/aponym-web/`.

## 3. Apuntar el dominio

### En GitHub
**Settings → Pages → Custom domain**: escribir el dominio y guardar. El archivo `CNAME`
se crea solo (si ya existe, lo respeta).

### En el DNS del dominio
Si el dominio se administra en NIC.cl, hay que delegarlo a un proveedor de DNS (NIC no
hospeda zona). Con Cloudflare (gratis) o el DNS del registrador:

| Tipo | Nombre | Valor |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |
| CNAME | `www` | `dvmyvn-hash.github.io` |

### En NIC.cl
Cambiar los **nameservers** del dominio a los del proveedor de DNS elegido (por ejemplo,
los dos que entregue Cloudflare). La propagación puede tardar hasta 24 h, normalmente
menos de una hora.

## 4. HTTPS

Cuando GitHub muestre el dominio como válido, activar **Enforce HTTPS** en
**Settings → Pages**. El certificado lo emite GitHub.

## 5. Verificar

```
nslookup aponym.cl
curl -I https://aponym.cl
```

Debe responder `200` y `strict-transport-security`. Probar también:

- `https://www.aponym.cl` (redirige al dominio sin www)
- `https://aponym.cl/eula.html` y `https://aponym.cl/privacidad.html`
- `https://aponym.cl/404.html` forzando una ruta inexistente
- Que no haya peticiones a terceros: abrir DevTools → Network y recargar.

## 6. Después de publicar

- **Revisar el copy** con calma (Hugo lo puede mejorar cuando recupere el PC).
- Si se agrega una sección nueva, mantener la regla: sin scripts, sin fuentes externas,
  sin cookies.
- Cuando cambie el EULA del producto: `python herramientas\eula_html.py` y volver a subir.
- `og.png` ya está en `assets/`; si cambia el dominio, actualizar la URL absoluta en los
  metadatos `og:url` y `og:image` (hoy son relativos).
