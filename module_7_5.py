import os
import time

directory = '.'
count_files = 0
for root, dirs, files in os.walk(directory): # Обход каталога
    for file in files:
        filepath = os.path.join(root, file) # Формируем путь к файлу
        count_files += 1 # Счетчик файлов (для наглядности)
        filesize = os.path.getsize(filepath) # Получаем размер файла
        filetime = os.path.getmtime(filepath) # Получаем время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(filepath) # Определяем родительскую директорию
        print(f'Обнаружен файл ({count_files}): {file}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
