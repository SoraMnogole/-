from time import *

from PIL import Image

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QRadioButton, QTextEdit, QVBoxLayout, QWidget)

sleep(1)
app = QApplication([])
win = QWidget()
win.setWindowTitle("Приключения огурца")
win.resize(600,600)

karma = 100
key = 0

start = QPushButton("Начать")
layoutr = QHBoxLayout()
layoutr2 = QHBoxLayout()
v_lay_2 = QHBoxLayout()
v_lay_1 = QHBoxLayout()
v_lay_3 = QHBoxLayout()
v_lay_4 = QHBoxLayout()
main2lay = QVBoxLayout()

layoutr.addWidget(start)
start.resize(150, 50)

main_layuot = QHBoxLayout()
main_layuot.addLayout(layoutr)

win2 = QWidget()
win2.setWindowTitle("Знакомьтесь, великий и потрясающий Огурец!")
win2.resize(900,600)
name = QLineEdit()
name.setPlaceholderText("Как вас зовут?")
ook = QPushButton("Сохранить имя")
noo = QPushButton()
noo.hide()
idontknow = QPushButton()
talk = QLabel("Здравствуй храбрый воин!\n \n \n \nНазови совё имя")
know = QLabel("")
v_lay_1.addWidget(talk)
v_lay_3.addWidget(name)
v_lay_2.addWidget(ook)
v_lay_2.addWidget(noo)
v_lay_4.addWidget(idontknow)
v_lay_4.addWidget(know)

idontknow.hide()

def smena_kartinok():
        win2.show()
        win.hide()

def hideall():
    know.hide()
    noo.hide()
    ook.hide()
    idontknow.show()

def showall():
    idontknow.show()
    noo.show()
    ook.show()
    know.hide()

def cmena_texta():
    ook.setText("Хорошо")
    talk.setText("Прошу прощения, вышла небольшая ошибка. У вас уже есть имя - Огурец.")
    name.hide()
    noo.hide()
    idontknow.hide()
    know.hide()

def net_vabora():
    global karma
    noo.hide()
    karma-=1

def scenaone():
    if ook.text() == "Сохранить имя":
        cmena_texta()
    elif ook.text() == "Хорошо":
        talk.setText("Вы являетесь огурцом, но вы не так просты. Вы являетесь великим героем Огурцеландии!")
        ook.setText("Ясно")
    elif ook.text() == "Ясно":
        talk.setText("Так как вы великий герой, у вас есть не менее великая миссия!\nСпасти принцессу Огурцеландии, Иняшу Огуречнову, её украли злые помидоры.\nВаша миссия спасти великолепную принцессу Иняшу из плена.\nК сожалению, у вас нет выбора и вы не можете отказаться от миссии.")
        ook.setText("Да! Спасём принцессу!")
        noo.setText("Ужас, что за ситуация в стране? ")
        noo.show()
    elif ook.text() == "Да! Спасём принцессу!":
        talk.setText("Идите же, великий герой, к королю Огурцеландии!")
        ook.setText("Хорошо, идём")
        noo.hide()
    elif ook.text() == "Хорошо, идём":
        talk.setText("Король огурцов Тимир:\n Принцессу украли, ступай к помидорам и верни её.")
        ook.setText("Приказ принят")
        noo.show()
        noo.setText("Вас, что не беспокоит кража дочери?")
    elif ook.text() == "Приказ принят":
        global karma
        karma += 1
        talk.setText("Вы отправляетесь в долгое путешествие, да благославит вас Бог огурцов!")
        ook.setText("Во славу богу огурцов!")
        noo.setText("А бог тоже огурец?")
        noo.show()
    elif ook.text() == "Во славу богу огурцов!":
        sleep(0.5)
        talk.setText("Я надеюсь, что вы не подумали что это конец?")
        ook.setText("В какой стороне Помидороландия?")
    elif ook.text() == "В какой стороне Помидороландия?":
        talk.setText("Вы направляетесь в Помидороландию.\n \nВы идёте сковзь леса и горы.\nПо пути в Помидороландию вы встречаете разгромленную повозку.\nВ ней находятся протухшие помидоры. \nВы видите на земле ключ.")
        showall()
        idontknow.setText("Все равно никто не узнает\n(своровать ключ)")
        ook.setText("Пойдёмте дальше")
        noo.setText("Н-да, везде разруха")
    elif ook.text() == "Пойдёмте дальше":
        talk.setText("Пройдя чуть дальше вы видите ворота королевства Помидоров. \nОх, кажется нам тут не рады. Помидоры патрулируют ворота и ожидают вас с недобрыми намерениями.")
        showall()
        noo.setText("Автор разочаровывает.")
        ook.setText("Незаметно пройдём мимо стражи, к королевскому дворцу Помидоров. Лишние драки ни к чему.")
        idontknow.setText("Сразимся с честью!(убить помидоров)")
    elif ook.text() == "Незаметно пройдём мимо стражи, к королевскому дворцу Помидоров. Лишние драки ни к чему." or ook.text() == "Время идти к королю.":
        talk.setText("Вы встречаете короля помидоров в зале для аудиенций")
        showall()
        noo.hide()
        ook.setText("Верните принцессу!")
        idontknow.setText("Мы поговорим на мечах!")
    elif ook.text() == "Где принцесса Иняша?":
        talk.setText('Внезапно появляется древнее-зло-с-ножом.\n                                Готовы ли вы сразиться с ним?')
        showall()
        ook.setText("Я приму битву с честью!")
        noo.setText("Что ещё за древнее зло с ножом? Нельзя было назвать по другому?")
        idontknow.setText("Сбежать")
    elif ook.text() == "Верните принцессу!":
        karma+=10
        talk.setText("Король помидоров:\n Мне жаль, но ее украло древнее-зло-с-ножом!")
        noo.hide()
        idontknow.hide()
        ook.setText("Что?")
    elif ook.text() == "Что?":
        talk.setText("Внезапно появляется древнее-зло-с-ножом.\n                               Готовы ли вы сразиться с ним?")
        showall()
        ook.setText("Я приму битву с честью!")
        noo.setText("Что ещё за древнее зло с ножом? Нельзя было назвать по другому?")
        idontknow.setText("Сбежать")
    elif ook.text() == "Я приму битву с честью!":
        talk.setText("Древнее-зло-с-ножом:\n Что с моими овощами? Я же прoсто хотел поесть... ")
        noo.hide()
        idontknow.hide()
        ook.setText("Атаковать!")
    elif ook.text() == "Атаковать!":
        talk.setText("Древнее-зло-с-ножом не обращает внимания на ваши атаки.\n Вы уже собирались прощаться с жизнью, но прибывает помощь.\n                         Вы слышите чей-то голос:\n                         Не волнуйся, я помогу!")
        ook.setText("Кто это?")
    elif ook.text() == "Кто это?":
        talk.setText("Древнее-зло-с-ножом сражено великим заклинанием.\nВы видите клетку с принцессой огурцов!")
        global key
        if key == 1:
            ook.setText("Открыть клетку")
        else:
            ook.setText("Сломать клетку")
    elif ook.text() == "Открыть клетку":
        if karma < 100 and karma > 50:
            hideall()
            idontknow.hide()
            talk.setText("Вы спасли принцессу и вас чествуют как великого героя!\n Результат: Крайне хороший!")

        elif karma < 50 and karma > 0:
            hideall()
            idontknow.hide()
            talk.setText("Вы спасли принцессу! Поздравляю, вы выполнили свою миссию!\n Результат: Не худший конец из всех.")
        else:
            hideall()
            idontknow.hide()
            talk.setText("Вы спасли принцессу, но по прибытию в королевство вы отправились в темницу, вследствие своих злодеяний!\n Результат: Можно было вести себя лучше!")
    elif ook.text() == "Сломать клетку":
        talk.setText("На клетку было наложено заклинание, принцесса умерла от того что клетку открыли не должным образом.")
        noo.show()
        noo.setText("И весь этот путь ради гибели принцессы?")
        ook.setText("Дальше.")
    elif ook.text() == "Дальше.":
        if karma >= 100:
            hideall()
            idontknow.hide()
            talk.setText("Вы не смогли спасти принцессу. Вас хотят казнить.")
            ook.setText("Продолжить")
        else:
            hideall()
            idontknow.hide()
            talk.setText('Вы не спасли принцессу и вас казнили.\n Результат: Плохой финал')
    elif ook.text() == "Продолжить":
        talk.setText("Кто-то встает на вашу защиту.")
        ook.setText("Ты...")
    elif ook.text() == "Ты...":
        talk.setText("Помидорка Барбара:\n Ваше королевское величество, этот герой не смог спасти принцессу в силу отсутствия ключа. Этот герой сделал все, что было в его силах.\n Если вы его помилуете, то вашему королевству будет сопутствовать удача, иначе оно падет сегодня же.\n\n\n Результат: Это секретная концовка. Я восхищен вами!")

def whatdoyouknow():
    if idontknow.text() == "Все равно никто не узнает\n(своровать ключ)":
        global karma
        global key
        karma-=45
        key+=1
        idontknow.hide()
        know.show()
        know.setText("Теперь вы вор!")
    elif idontknow.text() == "Сразимся с честью!":
        karma-=15
        idontknow.hide()
        know.show()
        know.setText("Враги пали, не устояв перед мощью легендарного героя.")
        ook.setText("Время идти к королю.")
    elif idontknow.text() == "Мы поговорим на мечах!":
        hideall()
        karma-=15
        talk.setText("Вы одерживаете многовенную победу. Осталось найти принцессу.\n\n\n\n\n\nВ зал вбегает помидорка.\n\nПомидорка:\n Нет! Ты обещал мне! Ты не мог умереть! Брат!")
        ook.show()
        ook.setText("Где принцесса Иняша?")
        idontknow.show()
        idontknow.setText("Убить принцессу")
    elif idontknow.text() == "Убить принцессу":
        hideall()
        idontknow.hide()
        if karma > 50:
            talk.setText("Внезапно вас настигает ужасное заклятье. Поздравляю, вы прошли игру!\n Результат:Плохой финал")
        else:
            talk.setText("Внезапно вас настигает ужасное заклятье. Вы чувствуете вес своих грехов и умираете страшной смертью.\n Поздравляю!Вы прошли игру!\n Результат: Плохой финал, может, стоило быть добрее?")
    elif idontknow.text() == "Сбежать":
        hideall()
        idontknow.hide()
        talk.setText("                                  Таинственый голос:\n                          И это тебя зовут героем? Полное разочарование.\n\n\n\n Результат: Вы проиграли, но не волнуйтесь о ваших незавершённых делах позаботились.")



main2lay.addLayout(v_lay_1)
main2lay.addLayout(v_lay_3)
main2lay.addLayout(v_lay_2)
main2lay.addLayout(v_lay_4)
idontknow.clicked.connect(whatdoyouknow)
noo.clicked.connect(net_vabora)
ook.clicked.connect(scenaone)
start.clicked.connect(smena_kartinok)
win2.setLayout(main2lay)
win.setLayout(main_layuot)
win.show()
app.exec_()
