import shutil
import os

def copy_and_remove(original_path, copy_path):
    try:
        shutil.copy2(original_path, copy_path)

        os.remove(original_path)

        print(f"Файл скопирован в {copy_path}, оригинал удален.")
    except FileNotFoundError:
        print("Оригинальный файл не найден.")



copy_and_remove("bebebe", "copy")
