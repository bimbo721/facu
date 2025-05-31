import rarfile
import itertools
import os
import shutil
import tempfile

RAR_PATH = r"C:\Users\joaco\Desktop\bloodcarpeta\Blood.rar"
rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"  # Cambiar si es necesario

# Generar variantes de "blood" con distintas mayúsculas
def generate_base_words(word="blood"):
    chars = list(word.lower())
    for bits in itertools.product(*[(c.lower(), c.upper()) for c in chars]):
        yield ''.join(bits)

# Generar sufijos numéricos (hasta 5 dígitos)
def generate_suffixes(max_digits=5):
    for length in range(0, max_digits + 1):  # Incluye sin sufijo
        for digits in itertools.product("0123456789", repeat=length):
            yield ''.join(digits)

# Combinación de base + sufijo
def generate_passwords():
    for base in generate_base_words():
        for suffix in generate_suffixes():
            yield base + suffix

# Probar todas las contraseñas generadas
for password in generate_passwords():
    print(f"🔐 Probando: {password}")

    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            with rarfile.RarFile(RAR_PATH) as rf:
                rf.extractall(path=tmpdir, pwd=password.encode('utf-8'))

            extracted_files = os.listdir(tmpdir)
            total_size = sum(os.path.getsize(os.path.join(tmpdir, f)) for f in extracted_files)

            if extracted_files and total_size > 0:
                print(f"\n✅ ¡Contraseña encontrada!: {password}")
                print(f"📁 Archivos extraídos en: {tmpdir}")
                input("Presioná Enter para copiar los archivos antes de que se borren...")
                shutil.copytree(tmpdir, os.path.join(os.getcwd(), "archivos_extraidos"))
                print("📦 Archivos copiados a ./archivos_extraidos")
                break

        except rarfile.RarWrongPassword:
            continue
        except rarfile.BadRarFile:
            print("❌ Archivo RAR corrupto.")
            break
        except Exception as e:
            print(f"⚠️ Error inesperado con '{password}': {e}")
            break