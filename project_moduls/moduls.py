import random
import time


# расписание
def timetable(answer):
    if (answer.lower()).find("распис") != -1:
        exm_timetable = ("ЛЮБИИМЫЙ ПАЙТОН", "УРОКИ ЛИТРБОЛА", "ПАРУ ОТМЕНИЛИ")
        print(random.choice(exm_timetable))


# контактные данные
def information_for_trainer(answer):
    if (answer.lower()).find("тренер") != -1:
        hlp = input('Выберите направление: ')
        if (hlp.lower()).find("любимый") != -1 or (hlp.lower()).find("пайтон") != -1:
            print("ШКАФ ЗЕЛЕНЫЙ \n Улица Пушкина, Дом Колотушкина \n +123456789")
        elif (hlp.lower()).find("литр") != -1 != -1:
            print("ДЯДЯ ВАСЯ \n Улица Колотушкина, Дом Пушкина \n +123456789")

# сумма к оплате
def amount_price(answer):
    if (answer.lower()).find("сумм") != -1 or (answer.lower()).find("оплата") !=-1 :
        print("777 вьетнамских рупий")


# любимый комик
def my_module_1(answer):
    if (answer.lower()).find("комик") != -1:
        clown = input("Назови своего любомого комика из ЧБД (Для выхода из мини игры напиши закончим): ")
        while clown != ('закончим'):
            if (clown.lower()).find("сабуров") != -1 or (clown.lower()).find("нур") != -1:
                print("ОГО! Хороший выбор выходец и Казахстана и лидер проекта.")
            elif (clown.lower()).find("лех") != -1 or (clown.lower()).find("щербак") != -1:
                print("Леха Щербаков. Крутой парень любитель японского автопрома.")
            elif (clown.lower()).find("масаев") != -1 or (clown.lower()).find("тамби") != -1:
                print("Тамби. Комик, который познал само лезвие юмора. Его шутки одни из самых язвительных")
            elif (clown.lower()).find("макар") != -1 or (clown.lower()).find("илья") != -1:
                print("Илюха. Его юмор заключается в том что может внести свою \n лепту в шутку сказав что-то с точки зрения простого человека")
            elif (clown.lower()).find("эмир") != -1 or (clown.lower()).find("кашоков") != -1:
                print("Эмир. Обычный комик.")
            time.sleep(1.3)
            clown = input("Назови своего любомого комика из ЧБД (Для выхожа из мини игры напиши закончим): ")

#цикличность ответчика
def proverka(answer):
   if (answer.lower()).find('распис') == -1  and (answer.lower()).find('сумм') == -1 and (answer.lower()).find('тренер') == -1 and (answer.lower()).find('комик') :
      time.sleep(0.5)
      print('Ввод с ошибкой')
