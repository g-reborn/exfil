import subprocess
import sys
import os

def install_requirements():
    requirements = ['python-telegram-bot']

    print("--- Modül Kurulumu Başlatılıyor ---")
    print("İşlem internet hızınıza bağlı olarak 1-2 dakika sürebilir.\n")

    for module in requirements:
        try:
            print(f"Yükleniyor: {module}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(f"Başarılı: {module} kuruldu.\n")
        except subprocess.CalledProcessError:
            print(f"Hata: {module} yüklenirken bir sorun oluştu.")
        except Exception as e:
            print(f"Beklenmedik Hata: {e}")

    print("-------------------------------------------")
    print("Kurulum tamamlandı. Ana kodu çalıştırabilirsiniz.")
    print("-------------------------------------------\n")

if __name__ == "__main__":
    try:
        install_requirements()
    finally:
        os._exit(0)
