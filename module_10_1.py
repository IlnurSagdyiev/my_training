import threading
from time import sleep, perf_counter
from datetime import timedelta


def write_words(word_count: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


started_at = perf_counter()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at = perf_counter()
print(f'Работа потоков {timedelta(seconds=ended_at - started_at)}')

data_to_write_to_file = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]
started_at = perf_counter()
all_threads = []
for arg in data_to_write_to_file:
    thread = threading.Thread(target=write_words, args=arg)
    thread.start()
    all_threads.append(thread)
for thread in all_threads:
    thread.join()
ended_at = perf_counter()
print(f'Работа потоков {timedelta(seconds=ended_at - started_at)}')
