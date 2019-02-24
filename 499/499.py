# problem number 0499
import sys
import re
for line in sys.stdin:
    frequency_of_letter = {};
    max_frequency = 0
    max_frequency_letters_upper = ""
    max_frequency_letters_lower = ""
    line = line.strip().replace(" ", "")
    for letter in line:
        if letter in frequency_of_letter:
            frequency_of_letter[letter] += 1
        else:
            if (letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                continue
            else:
                frequency_of_letter[letter] = 1
    if not frequency_of_letter:
        continue
    max_frequency = max(sorted(frequency_of_letter.values()))
    for letter in frequency_of_letter:
        if frequency_of_letter[letter] == max_frequency:
            if letter.isupper():
                max_frequency_letters_upper = max_frequency_letters_upper + letter
            else:
                max_frequency_letters_lower = max_frequency_letters_lower + letter

    print ("%s %s" %("".join(sorted(max_frequency_letters_upper) + sorted(max_frequency_letters_lower)), max_frequency))
