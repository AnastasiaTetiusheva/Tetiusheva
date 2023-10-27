users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dictionary_1 = dict([("Общее количество", 0), ("Уникальные посещения", 0)])
dictionary_1["Общее количество"] = len(users)
dictionary_1["Уникальные посещения"] = len(set(users))

print(dictionary_1)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
