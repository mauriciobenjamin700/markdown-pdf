import markdown
from weasyprint import HTML
import os

def markdown_to_pdf(
        md_file_path: str, 
        pdf_file_path: str, 
        css_file_path=None
    ):
    """
    A function to convert a Markdown file to PDF using WeasyPrint.

    - Args:
      - md_file_path:: str: Path to the input Markdown file.
      - pdf_file_path:: str: Path to the output PDF file.
      - css_file_path:: str: Path to the CSS file for styling (optional).

    - 
    """
    # Read the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=[
        'fenced_code',       # Suporte a blocos de código cercados
        'codehilite',        # Destaque de sintaxe (requer pygments)
        'tables',            # Suporte a tabelas
        'toc',              # Tabela de conteúdo (opcional)
        'nl2br',            # Quebra de linha
        'sane_lists',       # Listas seguras
        'attr_list',        # Atributos de lista
        'meta',             # Metadados
        'smarty',           # Aspas inteligentes
        'footnotes',        # Notas de rodapé
        'mdx_math',        # Suporte a matemática (opcional)
    ])
    
    # Criar HTML completo com estilos
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{os.path.basename(md_file_path)}</title>
        <style>
            /* Estilos padrão */
            body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 0 auto; max-width: 800px; padding: 20px; }}
            h1, h2, h3 {{ color: #333; }}
            code {{ background: #f4f4f4; padding: 2px 5px; }}
            pre {{ background: #f8f8f8; padding: 10px; overflow: auto; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            /* CSS personalizado será injetado aqui */
            {open(css_file_path).read() if css_file_path and os.path.exists(css_file_path) else ''}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Gerar PDF
    HTML(string=full_html).write_pdf(pdf_file_path)