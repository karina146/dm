def clean_text(text):
    text = text.lower()
    text = text.replace(' ', '')
    for i in text:
        if i in '1234567890-_,.:;!?()’“”…':
            text = text.replace(i,'')
    return text


def analyze_text_statistics(text):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'

    letter_stats = {}
    
    for letter in text:
        if letter in letter_stats:
            letter_stats[letter] += 1
        else:
            letter_stats[letter] = 1
    
    total_letters = len(text)

    sorted_letters = dict(sorted(letter_stats.items()))
    
    # информация о буквах, которых нет в тексте
    missing = []
    for letter in alphabet:
        if letter not in letter_stats:
            missing.append(letter)
    
    # 2. АНАЛИЗ ЧАСТОТЫ ПАР БУКВ (БИГРАММ)

    bigram_stats = {}
    
    for i in range(len(text) - 1):
        bigram = text[i] + text[i+1]
        if bigram in bigram_stats:
            bigram_stats[bigram] += 1
        else:
            bigram_stats[bigram] = 1
    
    total_bigrams = len(text) - 1

    sorted_bigrams = dict(sorted(bigram_stats.items()))
    
    return sorted_letters, sorted_bigrams, total_letters, total_bigrams



if __name__ == "__main__":

    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text = clean_text(text)
    
    letter_list, bigram_list, total_letters, total_bigrams = analyze_text_statistics(text)
    print(letter_list)
    text1 = sorted(letter_list.items(),key=lambda x:x[1], reverse=True) # сортировка по количеству
    print(text1)

    with open('statistic_letter.txt', 'w', encoding='utf-8') as f:
        for letter in letter_list:
            f.write(f'{letter}: {letter_list[letter]}\n')
    with open('statistic_bidrams.txt', 'w', encoding='utf-8') as f:
        for letter in bigram_list:
            f.write(f'{letter}: {bigram_list[letter]}\n')
    
    
