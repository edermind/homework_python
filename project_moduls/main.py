import moduls

if __name__ == '__main__':
    answer = input('АВТООТВЕТЧИК ГОТОВ К ВАШИМ ВОПРОСАМ(ВЫКЛЮЧИТЬ - off): ')
    while answer != 'off':
        moduls.timetable(answer)
        moduls.information_for_trainer(answer)
        moduls.amount_price(answer)
        moduls.proverka(answer)
        moduls.my_module_1(answer)
        answer = input('АВТООТВЕТЧИК ГОТОВ К ВАШИМ ВОПРОСАМ(ВЫКЛЮЧИТЬ - off): ')
    print ('ОТВЕТЧИК ЗАВЕРШАЕТ РАБОТУ.')