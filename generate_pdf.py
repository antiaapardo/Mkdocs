#!/usr/bin/env python
"""
Script para generar PDF de la documentación usando Playwright
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright


async def generate_pdf():
    """Genera PDF a partir de la documentación HTML"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # URL de la página principal de mkdocs
        url = "http://127.0.0.1:8000/"
        
        await page.goto(url)
        await page.wait_for_load_state("networkidle")
        
        # Crear carpeta de descargas si no existe
        pdf_dir = Path("site/pdf")
        pdf_dir.mkdir(exist_ok=True)
        
        # Generar PDF
        pdf_path = pdf_dir / "documentacion.pdf"
        await page.pdf(path=str(pdf_path), format="A4")
        
        print(f"✓ PDF generado: {pdf_path}")
        
        await browser.close()


if __name__ == "__main__":
    asyncio.run(generate_pdf())
