
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
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

'''
{'Walt Whitman - O Captain! My Captain!.txt': ['o', 'captain', 'my', 'captain', 'o', 'captain', 'my', 'captain', 'our', 
'fearful', 'trip', 'is', 'done', 'the', 'ship', 'has', 'weather’d', 'every', 'rack', 'the', 'prize', 'we', 'sought', 
'is', 'won', 'the', 'port', 'is', 'near', 'the', 'bells', 'i', 'hear', 'the', 'people', 'all', 'exulting', 'while', 
'follow', 'eyes', 'the', 'steady', 'keel', 'the', 'vessel', 'grim', 'and', 'daring', 'but', 'o', 'heart', 'heart', 
'heart', 'o', 'the', 'bleeding', 'drops', 'of', 'red', 'where', 'on', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 
'cold', 'and', 'dead', 'o', 'captain', 'my', 'captain', 'rise', 'up', 'and', 'hear', 'the', 'bells', 'rise', 'up', '—', 
'for', 'you', 'the', 'flag', 'is', 'flung', '—', 'for', 'you', 'the', 'bugle', 'trills', 'for', 'you', 'bouquets', 'and', 
'ribbon’d', 'wreaths', '—', 'for', 'you', 'the', 'shores', 'acrowding', 'for', 'you', 'they', 'call', 'the', 'swaying', 'mass', 
'their', 'eager', 'faces', 'turning', 'here', 'captain', 'dear', 'father', 'this', 'arm', 'beneath', 'your', 'head', 'it', 
'is', 'some', 'dream', 'that', 'on', 'the', 'deck', 'you’ve', 'fallen', 'cold', 'and', 'dead', 'my', 'captain', 'does', 
'not', 'answer', 'his', 'lips', 'are', 'pale', 'and', 'still', 'my', 'father', 'does', 'not', 'feel', 'my', 'arm', 'he', 
'has', 'no', 'pulse', 'nor', 'will', 'the', 'ship', 'is', 'anchor’d', 'safe', 'and', 'sound', 'its', 'voyage', 'closed', 
'and', 'done', 'from', 'fearful', 'trip', 'the', 'victor', 'ship', 'comes', 'in', 'with', 'object', 'won', 'exult', 'o', 
'shores', 'and', 'ring', 'o', 'bells', 'but', 'i', 'with', 'mournful', 'tread', 'walk', 'the', 'deck', 'my', 'captain', 
'lies', 'fallen', 'cold', 'and', 'dead', 'walt', 'whitman'], 'Rudyard Kipling - If.txt': ['if', 'if', 'you', 'can', 'keep', 
'your', 'head', 'when', 'all', 'about', 'you', 'are', 'losing', 'theirs', 'and', 'blaming', 'it', 'on', 'you', 'if', 'you', 
'can', 'trust', 'yourself', 'when', 'all', 'men', 'doubt', 'you', 'but', 'make', 'allowance', 'for', 'their', 'doubting', 'too', 
'if', 'you', 'can', 'wait', 'and', 'not', 'be', 'tired', 'by', 'waiting', 'or', 'being', 'lied', 'about', 'don’t', 'deal', 'in', 
'lies', 'or', 'being', 'hated', 'don’t', 'give', 'way', 'to', 'hating', 'and', 'yet', 'don’t', 'look', 'too', 'good', 'nor', 
'talk', 'too', 'wise', 'if', 'you', 'can', 'dream', '—', 'and', 'not', 'make', 'dreams', 'your', 'master', 'if', 'you', 'can', 
'think', '—', 'and', 'not', 'make', 'thoughts', 'your', 'aim', 'if', 'you', 'can', 'meet', 'with', 'triumph', 'and', 'disaster', 
'and', 'treat', 'those', 'two', 'impostors', 'just', 'the', 'same', 'if', 'you', 'can', 'bear', 'to', 'hear', 'the', 'truth', 
'you’ve', 'spoken', 'twisted', 'by', 'knaves', 'to', 'make', 'a', 'trap', 'for', 'fools', 'or', 'watch', 'the', 'things', 
'you', 'gave', 'your', 'life', 'to', 'broken', 'and', 'stoop', 'and', 'build', '’em', 'up', 'with', 'worn-out', 'tools', 'if', 
'you', 'can', 'make', 'one', 'heap', 'of', 'all', 'your', 'winnings', 'and', 'risk', 'it', 'on', 'one', 'turn', 'of', 
'pitch-and-toss', 'and', 'lose', 'and', 'start', 'again', 'at', 'your', 'beginnings', 'and', 'never', 'breathe', 'a', 'word', 
'about', 'your', 'loss', 'if', 'you', 'can', 'force', 'your', 'heart', 'and', 'nerve', 'and', 'sinew', 'to', 'serve', 'your', 
'turn', 'long', 'after', 'they', 'are', 'gone', 'and', 'so', 'hold', 'on', 'when', 'there', 'is', 'nothing', 'in', 'you', 
'except', 'the', 'will', 'which', 'says', 'to', 'them', '‘hold', 'on’', 'if', 'you', 'can', 'talk', 'with', 'crowds', 'and', 
'keep', 'your', 'virtue', 'or', 'walk', 'with', 'kings', '—', 'nor', 'lose', 'the', 'common', 'touch', 'if', 'neither', 'foes', 
'nor', 'loving', 'friends', 'can', 'hurt', 'you', 'if', 'all', 'men', 'count', 'with', 'you', 'but', 'none', 'too', 'much', 'if', 
'you', 'can', 'fill', 'the', 'unforgiving', 'minute', 'with', 'sixty', 'seconds’', 'worth', 'of', 'distance', 'run', 'yours', 
'is', 'the', 'earth', 'and', 'everything', 'that’s', 'in', 'it', 'and', '—', 'which', 'is', 'more', '—', 'you’ll', 'be', 'a', 
'man', 'my', 'son', 'rudyard', 'kipling'], 'Mother Goose - Monday’s Child.txt': ['monday’s', 'child', 'monday’s', 'child', 
'is', 'fair', 'of', 'face', 'tuesday’s', 'child', 'is', 'full', 'of', 'grace', 'wednesday’s', 'child', 'is', 'full', 'of', 
'woe', 'thursday’s', 'child', 'has', 'far', 'to', 'go', 'friday’s', 'child', 'is', 'loving', 'and', 'giving', 'saturday’s', 
'child', 'works', 'hard', 'for', 'a', 'living', 'and', 'the', 'child', 'that', 'is', 'born', 'on', 'the', 'sabbath', 'day', 
'is', 'bonny', 'and', 'blithe', 'and', 'good', 'and', 'gay', 'mother', 'goose']}
{'Walt Whitman - O Captain! My Captain!.txt': 14, 'Rudyard Kipling - If.txt': 109, 'Mother Goose - Monday’s Child.txt': 41}
{'Walt Whitman - O Captain! My Captain!.txt': 18, 'Rudyard Kipling - If.txt': 7, 'Mother Goose - Monday’s Child.txt': 2}
'''