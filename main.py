import subprocess

def convert_with_libreoffice(docx_path, output_dir):
    soffice_path = r'C:\Program Files\LibreOffice\program\soffice.exe'

    process = subprocess.Popen([
        soffice_path, '--headless', '--convert-to', 'html', '--outdir', output_dir, docx_path
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("Erro:", stderr.decode())
    else:
        print("Sucesso:", stdout.decode())

# Exemplo de uso
convert_with_libreoffice("Enunciado.docx", "output_folder")
