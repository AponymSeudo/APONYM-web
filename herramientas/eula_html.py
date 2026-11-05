#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera eula.html a partir de docs/EULA.md del repo del producto.

Uso:  python herramientas\\eula_html.py
No editar eula.html a mano: se regenera.
"""
import html
import re
import sys
from pathlib import Path

RAIZ_SITIO = Path(__file__).resolve().parent.parent
EULA_MD = RAIZ_SITIO.parent / "ANONIMIZADOR" / "docs" / "EULA.md"
SALIDA = RAIZ_SITIO / "eula.html"

PLANTILLA = """<!DOCTYPE html>
<html lang="es-CL">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>Condiciones de uso — APONYM</title>
  <meta name="description" content="Condiciones de uso de APONYM.">
  <link rel="icon" href="assets/icono.png" sizes="256x256">
  <link rel="stylesheet" href="estilos.css">
  <style>
    .legal {{ max-width: 760px; padding-top: 72px; padding-bottom: 96px; }}
    .legal h1 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(32px, 4.2vw, 48px); margin: 0 0 8px; }}
    .legal h2 {{ font-family: var(--serif); font-weight: 400; font-size: 24px; margin: 40px 0 8px; }}
    .legal p, .legal li {{ color: var(--tinta-suave); }}
    .legal__sub {{ color: var(--muted); font-size: 14px; margin-bottom: 30px; }}
    .volver {{ display: inline-block; margin-top: 40px; font-size: 14px; color: var(--muted); }}
  </style>
</head>
<body>
  <header class="cabecera">
    <div class="contenedor cabecera__fila">
      <a class="marca" href="index.html" aria-label="APONYM, volver al inicio">
        <img src="assets/logo-header.png" alt="APONYM" width="170" height="47">
      </a>
    </div>
  </header>
  <main class="contenedor legal">
{contenido}
    <a class="volver" href="index.html">← Volver al inicio</a>
  </main>
  <footer class="pie">
    <div class="contenedor pie__fila">
      <img src="assets/logo-claro.png" alt="APONYM" width="140" height="39">
      <nav class="pie__nav" aria-label="Legal">
        <a href="privacidad.html">Privacidad</a>
        <a href="eula.html">Condiciones de uso</a>
        <a href="mailto:dpintovillaseca@gmail.com">Contacto</a>
      </nav>
      <p class="pie__legal">© 2026 APONYM · Hecho en Chile</p>
    </div>
  </footer>
</body>
</html>
"""


def _limpia(texto: str) -> str:
    texto = html.escape(texto.strip(), quote=False)
    texto = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", texto)
    return texto


def convertir(md: str) -> str:
    lineas = md.splitlines()
    salida: list[str] = []
    buffer: list[str] = []

    def cerrar_parrafo():
        if buffer:
            salida.append("<p>" + _limpia(" ".join(buffer)) + "</p>")
            buffer.clear()

    for linea in lineas:
        limpia = linea.strip()
        if not limpia:
            cerrar_parrafo()
            continue
        if limpia.startswith("# "):
            cerrar_parrafo()
            salida.append("<h1>" + _limpia(limpia[2:]) + "</h1>")
            continue
        if limpia.startswith("## "):
            cerrar_parrafo()
            salida.append("<h2>" + _limpia(limpia[3:]) + "</h2>")
            continue
        if limpia.startswith("**") and limpia.endswith("**") and len(limpia) < 90:
            cerrar_parrafo()
            salida.append('<p class="legal__sub">' + _limpia(limpia) + "</p>")
            continue
        if re.fullmatch(r"-{3,}", limpia):
            cerrar_parrafo()
            continue
        if limpia.startswith("- "):
            cerrar_parrafo()
            salida.append("<li>" + _limpia(limpia[2:]) + "</li>")
            continue
        buffer.append(limpia)

    cerrar_parrafo()
    return "\n".join("      " + linea for linea in salida)


def main() -> int:
    if not EULA_MD.is_file():
        print(f"[ERROR] No encuentro {EULA_MD}")
        return 1
    contenido = convertir(EULA_MD.read_text(encoding="utf-8"))
    SALIDA.write_text(PLANTILLA.format(contenido=contenido), encoding="utf-8", newline="\n")
    print(f"[OK] {SALIDA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
