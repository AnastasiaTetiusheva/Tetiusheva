# TODO Напишите функцию find_common_participants
def find_common_participants(participants_1, participants_2, razdelitel = ","):

    participants_1 = participants_1.split(razdelitel)
    participants_2 = participants_2.split(razdelitel)

    common_participants = list(set(participants_1).intersection(participants_2))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
razdelitel_ = "|"



# TODO Провеьте работу функции с разделителем отличным от запятой

common = find_common_participants(participants_first_group, participants_second_group, razdelitel_)
print("Общие участники:", common)