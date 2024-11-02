def custom_write(file_name: str, strings: list):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, val in enumerate(strings, start=1):
            byte_number = file.tell()
            file.write(f'{val}\n')
            strings_positions[(line_number, byte_number)] = val
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
