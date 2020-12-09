# x = 'C:\\Users\\KimAlex\\Desktop\\Russian.txt'
x = 'Russian.txt'

def text_analyzer():
    """Данная функция считает количество слов, абзацев, предложений, знаков и пробелов. Вычисляет среднюю длину
    предложения и ТОП-10 слов."""

    def number_of_words(file):
        """Данная функция считает количество цифр и слов в тексте"""

        import re
        f = open(file, 'rt', encoding='utf-8')

        words_n_numbers = 0
        number_of_numbers = 0

        for line in f:
            b = line.split(" ")
            numbers = re.findall(r'\d+', line)
            if len(numbers) > 0:
                number_of_numbers += len(numbers)
            for i in b:
                words_n_numbers += 1

        f.close()

        number_of_words1 = words_n_numbers - number_of_numbers

        print('Words plus numbers:', words_n_numbers)
        print('Number of numbers:', number_of_numbers)
        print('Number of words:', number_of_words1)

    number_of_words(x)

    def number_of_paragraphs(file):
        """Данная функция считает количесто параграфов (абзацев) в тексте"""
        import re

        f = open(file, 'rt', encoding='utf-8')
        number_of_paragraphs1 = 0
        for line in f:
            paragraph = re.findall(r'\n', line)
            if len(paragraph) > 0:
                number_of_paragraphs1 += len(paragraph)
        f.close()

        print('Number of paragraphs:', number_of_paragraphs1)

    number_of_paragraphs(x)

    def number_of_sentences(file):
        """Данная функция считает количество предложений в тексте"""
        import re

        f = open(file, 'rt', encoding='utf-8')
        number_of_sentences1 = 0
        for line in f:
            sentence = re.findall(r'(!+\?+)|(\?+!+)|(!+)|(\?+)|(\.+)', line)
            if len(sentence) > 0:
                number_of_sentences1 += len(sentence)
        f.close()

        print('Number of sentences:', number_of_sentences1)

    number_of_sentences(x)

    def number_of_characters_n_spaces(file):
        """Данная функция считает количество символов и пробелов в тексте"""
        import re

        f = open(file, 'rt', encoding='utf-8')
        number_of_characters = 0
        number_of_spaces = 0
        for line in f:
            character = re.findall(r'.', line)
            space = re.findall(r' ', line)
            if len(character) > 0:
                number_of_characters += len(character)
            if len(space) > 0:
                number_of_spaces += len(space)
        f.close()

        print('Number of characters:', number_of_characters)
        print('Number of spaces:', number_of_spaces)
        print('Number of characters without spaces', f'{number_of_characters - number_of_spaces}')

    number_of_characters_n_spaces(x)

    def intermediate_sentence_length(file):
        """Данная функция считает среднюю длину предложения (в буквах)"""
        import re
        f = open(file, 'rt', encoding='utf-8')

        number_of_sentences1 = 0
        for line in f:
            sentence = re.findall(r'(!+\?+)|(\?+!+)|(!+)|(\?+)|(\.+)', line)
            if len(sentence) > 0:
                number_of_sentences1 += len(sentence)
        f.close()

        f = open(file, 'rt', encoding='utf-8')
        number_of_characters = 0
        number_of_spaces = 0
        for line in f:
            character = re.findall(r'.', line)
            space = re.findall(r' ', line)
            if len(character) > 0:
                number_of_characters += len(character)
            if len(space) > 0:
                number_of_spaces += len(space)
        f.close()

        number_of_letters = number_of_characters - number_of_spaces

        intermediate_sentence_length1 = number_of_letters / number_of_sentences1

        print('Intermediate sentence length(characters):', intermediate_sentence_length1)

    intermediate_sentence_length(x)

    def top_10_words(file):
        """Данная функция выводит Топ-10 слов. Если в тексте есть разные слова, встречающиеся одинаковое количество раз,
        то функция ставит эти слова на одно место."""

        f = open(file, 'rt', encoding='utf-8')
        words = []
        # знаки препинания и спецсимоволы для удаления:
        delete = [',', '!', '?', ':', ';', '.', '\n', 'п»ї', '—', '-', '»']
        for line in f:
            # приводим все заглавные буквы к строчным:
            line = line.lower()
            # заменяем знаки препинания и спецсимволы пробелами:
            for symbol in delete:
                line = line.replace(symbol, ' ')
            # разделяем полученную строку по пробелам и приводим к списку:
            h = line.split(' ')
            # считаем в списке все пробелы и удаляем их, получаем список с избыточной информацией - слова повторяются:
            to_delete = h.count(' ')
            for i in range(to_delete):
                h.remove(' ')
            words.extend(h)
        f.close()

        # Создаем набор слов, которые не нужно учитывать в статистике:
        preps = {'в', 'а', 'и', 'о', 'я', 'у', 'с', 'к', 'да', 'то', 'ж', 'нет', 'да', '', ' ',
                 'не', 'за', 'же', 'на', 'по', 'ну', 'от', 'но', 'вот', 'до', 'ни', 'уж',
                 'из', 'бы', 'что', 'все', 'это', 'если', 'как', 'же'}

        # Удаляем из текста все предлоги и союзы:

        for i in preps:
            to_delete = words.count(i)
            for j in range(to_delete):
                words.remove(i)

        # Создаем словарь, с парами слово-количество повторений:
        words_counter = {}.fromkeys(words, 0)

        for word in words:
            number = words.count(word)
            words_counter[word] += number

        # Сортируем полученный словарь в порядке убывания:
        sorted_words_counter = sorted(words_counter.items(), key=lambda item: item[1], reverse=True)

        # Выводим полученный результат в консоль:
        print()
        print('TOP 10 WORDS!!!')
        print()
        counter = 1
        number = sorted_words_counter[0][1]
        for i in range(len(sorted_words_counter)):

            if counter == 10:
                break

            if sorted_words_counter[i][1] == number:
                print(f'{counter} Place!')
                print(f"Word: '{sorted_words_counter[i][0]}', Times: {sorted_words_counter[i][1]}")

            else:
                print('----------------------')
                print(f'{counter + 1} Place!')
                print(f"Word: '{sorted_words_counter[i][0]}', Times: {sorted_words_counter[i][1]}")
                number = sorted_words_counter[i][1]
                counter += 1

    top_10_words(x)


text_analyzer()

