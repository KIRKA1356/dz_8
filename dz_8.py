class Soup:
    def __init__(self, soup, ingridient):
        self.soup = soup
        self.ingridient = ingridient
        self.hot_water = 'просто кипяток!'
    def show_my_soup(self):
        if self.ingridient == 'свекла':
            self.hot_water = self.ingridient
            return f'В супе "{self.soup}" гавный ингридиент - "{self.ingridient}"'
        else:
            return f'Это не {self.soup} - это просто {self.hot_water}'

soup = Soup('Борщ', 'свекла')
print(soup.show_my_soup())

list1= []
class Students:
    def __init__(self, name, group, ocenka):
        self.name = name
        self.group = group
        self.ocenka = ocenka
    def add_in_spisok(self, list):
        self.list = list
        list = []
        list.append(self.name)
        list.append(self.group)
        list.append(self.ocenka)
    def print_students(shape):
        print(shape.list)

t = Students("Павел", "1345", 5)
print(t.print_students())

import random
import statistics


class Name:
    def get_name(self, num):
        class_list = []
        for i in range(num):
            class_list.append(input('Введите имя ученика: '))
        return  class_list

class Group:
    def get_group(self, num):
        group_class_list = []
        count_group = int(input('Сколько будет групп? '))
        for i in range(num):
            group_class_list.append(random.randint(1, count_group))
        return group_class_list

class Progress:
    def get_progress(self, num):
        progress_class_list = []
        count_progress = int(input('Сколько оценок будет введено? '))
        for i in range(num):
            count_class_list = []
            for k in range(count_progress):
                count_class_list.append(random.randint(2,5))
            progress_class_list.append(count_class_list)
        return progress_class_list

def create_total_list(name_list, group_list, progress_list, num):
    total_list = []
    for el in range(num):
        count_total_list = []
        count_total_list.append(name_list[el])
        count_total_list.append(group_list[el])
        count_total_list.append(progress_list[el])
        total_list.append(count_total_list)
    print('Полный список!')
    print('*' * 60)
    for el in range(len(total_list)):
        sred = 0
        count = 0
        print(f'ФИО: {total_list[el][0]}, группа: {total_list[el][1]}, оценки: ', end='')
        for i in total_list[el][2]:
            print(f'{i}', end=' ')
            sred = sred + i
            count += 1
        sred = sred / count
        print(f'Средняя оценка: {sred}', end=' ')
        print()
    return total_list

def bad_progress_list(list):
    print('*' * 60)
    flag = True
    for el in range(len(list)):
        if statistics.mean(list[el][2]) < 3:
            print('Список учеников со средней оценкой ниже 3!')
            sred = 0
            count = 0
            print(f'ФИО: {list[el][0]}, группа: {list[el][1]}, оценки: ', end='')
            for i in list[el][2]:
                print(f'{i}', end=' ')
                sred = sred + i
                count += 1
            sred = sred / count
            print(f'Средняя оценка: {sred}', end=' ')
            print()
            flag = False
    if flag == True:
        print('У всех учеников средний бал больше 3!')





num = int(input('Сколько будет человек в списке? '))
name = Name()
group = Group()
progress = Progress()
name_list = list(sorted(name.get_name(num)))
group_list = group.get_group(num)
progress_list = progress.get_progress(num)
bad_progress_list(create_total_list(name_list, group_list, progress_list, num))