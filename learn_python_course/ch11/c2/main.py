def count_vowels(text):
    vowel_count = 0
    uniq_vowel = set()
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for word in text:
        for letter in word:
            if letter.lower() in vowels:
                vowel_count += 1
                uniq_vowel.add(letter)

    return vowel_count, uniq_vowel
