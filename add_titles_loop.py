title_list = [] #пустой список для заголовков

title1 = input("Введите заголовок заметки (или введите стоп для завершения): ") #Создаем функцию ввода
while title1 != "стоп": #Запускаем цикл, что пока title1 не равен "стоп", цикл будет продолжаться и вновь запрашивать заголовки
    title_list.append(title1) #Добавляет введеный заголовок в список
    title1 = input("Введите заголовок заметки (или введите стоп для завершения): ") #Снова выходит функция ввода

print("Заголовки: ") #Выводит строку в консоль
for title1 in title_list: #Этот цикл начинает перебор всех элементов title1 в списке title_list
    print(title1) #Выводит все найденные заголовки