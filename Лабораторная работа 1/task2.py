list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2 #находим индекс середины для списка игроков

first_team = list_players[:middle_index] #в первую команду включаем всех до middle_index не включительно
second_team = list_players[middle_index:] #во вторую команду включаем всех от middle_index включительно до конца

print(first_team) #выводим состав первой команды
print(second_team) #выводим состав второй команды
