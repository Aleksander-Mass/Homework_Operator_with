import string

class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем названия файлов в атрибут
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем содержимое файла и приводим к нижнему регистру
                    text = file.read().lower()
                    # Избавляемся от пунктуации
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, '')
                    # Разбиваем текст на список слов
                    words = text.split()
                    # Сохраняем слова для данного файла
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            try:
                # Находим индекс первого вхождения слова
                index = words.index(word)  ###  сам индекс
                results[name] = index + 1     ###   index и позиция первого такого слова в списке слов этого файла
            except ValueError:
                # Если слово не найдено в файле
                results[name] = -1
        return results

    def count(self, word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            # Считаем количество вхождений слова в списке
            count = words.count(word)
            counts[name] = count
        return counts

# Пример использования
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
'''
Вывод на консоль:
{'Mother Goose - Monday’s Child.txt': ['monday’s', 'child', 'monday’s', 'child', 'is', 'fair', 'of', 'face', 'tuesday’s', 
'child', 'is', 'full', 'of', 'grace', 'wednesday’s', 'child', 'is', 'full', 'of', 'woe', 'thursday’s', 'child', 'has', 
'far', 'to', 'go', 'friday’s', 'child', 'is', 'loving', 'and', 'giving', 'saturday’s', 'child', 'works', 'hard', 'for', 
'a', 'living', 'and', 'the', 'child', 'that', 'is', 'born', 'on', 'the', 'sabbath', 'day', 'is', 'bonny', 'and', 'blithe', 
'and', 'good', 'and', 'gay', 'mother', 'goose']}
{'Mother Goose - Monday’s Child.txt': 2}
{'Mother Goose - Monday’s Child.txt': 8}
'''