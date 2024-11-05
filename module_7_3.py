class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def __str__(self):
        return f'{self.file_names}'

    def get_all_words(self):
        symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                for symbol in symbols_to_remove:
                    text = text.replace(symbol, '')
                all_words[file.name] = list(text.lower().split())
        return all_words

    def find(self, word: str):
        word_position = {}
        for key, value in self.get_all_words().items():
            for i in range(len(value)):
                if word.lower() in value[i]:
                    word_position[key] = i + 1
                    break
        return word_position  # функция выводит позицию первого слова, в котором находится искомый набор символов

    def count(self, word: str):
        word_count = {}
        for key, value in self.get_all_words().items():
            count = 0
            for i in range(len(value)):
                if word.lower() in value[i]:
                    count += 1
                word_count[key] = count
        return word_count  # функция выводит количество слов, в которых находится искомый набор символов, а не
        # количество вхождений этого набора символов, т.к. в одном слове может быть несколько вхождений


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
