# Publicar el sitio — pasos exactos

**Estado: publicado en `https://aponym.cl` el 05-11-2026.** El sitio es estático y no
necesita build. Lo que sigue queda como registro de cómo se armó y cómo se mantiene.

## 0. Datos

| Dato | Valor |
|---|---|
| Dominio | `aponym.cl` (registrado en NIC, DNS en Cloudflare) |
| Repo | `APONYM-web` en la organización `AponymSeudo`, **público** (Pages gratis exige repo público) |
| Cuenta | la de la organización `AponymSeudo` (Damián como owner) |

Ya hecho: `CNAME` con `aponym.cl`, dominio validado en Pages, `Enforce HTTPS` activo,
`noindex` retirado de los cuatro HTML y `robots.txt` en `Allow: /`.

## 1. Crear el repositorio y subir

Desde GitHub: **New repository** → nombre `aponym-web` → **Public** → sin README.

Después, en esta carpeta:

```
git init
git add .
git commit -m "Sitio APONYM v1"
git branch -M main
git remote add origin https://github.com/AponymSeudo/APONYM-web.git
git push -u origin main
```

## 2. Activar GitHub Pages

En el repo: **Settings → Pages**

- Source: **Deploy from a branch**
- Branch: **main** / carpeta **/ (root)**
- Save.

En uno o dos minutos el sitio queda en `https://aponymseudo.github.io/APONYM-web/`.

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
| CNAME | `www` | `aponymseudo.github.io` |

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
- `og.png` está en `assets/` (1200×630) y `og:url`, `og:image` y `twitter:image` apuntan a
  `https://aponym.cl/`. Si el dominio cambia, actualizar esas tres etiquetas.
