# TODO  Напишите функцию count_letters
def count_letters(main_str):
    main_dict = {}
    main_low = main_str.lower()
    for symbol in main_low:
        if symbol.isalpha() and symbol.islower():
            if symbol in main_dict:
                main_dict[symbol] += 1
            else:
                main_dict[symbol] = 1
    return main_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(main_dict):
    summ_ = sum(main_dict.values())
    frequencies = {}
    for text, count in main_dict.items():
        frequency = count / summ_
        frequencies[text] = frequency
    return frequencies

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
main_dict = count_letters(main_str)
frequencies = calculate_frequency(main_dict)

for text, freq in frequencies.items():
    print(f"{text}: {freq:.2f}")