from memo___card_layout import (app, layout_card,
    ib_question,
    ib_correct, ib_result, rbtn_1, rbtn_2,rbtn_3,
    rbtn_4,btn_Ok, show_question, show_result)
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle, randint # будем перемешивать ответы в карточке вопроса
from data import questions


card_width, card_height = 600, 500 # начальные размеры окна "карточка"
text_wrong = "Неправильно"
text_correct = "Правильно"

frm_question = "Телефон"
frm_right = "Phone"
frm_wrong1 = "car"
frm_wrong2 = "One milion dollars"
frm_wrong3 = "star"


radio_list=[rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)
answer = radio_list[0]
wrong_answer1,wrong_answer2,wrong_answer3 = radio_list[1],radio_list[2],radio_list[3]
def show_data():
    global radio_list, answer, wrong_answer1,wrong_answer2,wrong_answer3
    shuffle(radio_list)
    answer = radio_list[0]
    wrong_answer1,wrong_answer2,wrong_answer3 = radio_list[1],radio_list[2],radio_list[3]
    ''' показывает на экране нужную информацию '''
    ib_question.setText(frm_question)
    ib_correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def check_result():
    ''' проверка, правильный ли ответ выбран
    если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
    и показывается панель ответов '''
    correct = answer.isChecked()
    if correct:
        ib_result.setText(text_correct)
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked   
        if incorrect:
            ib_result.setText(text_wrong)
            show_result()


def click_OK():
    if btn_Ok.text() != "Наступне питання":
        check_result()
    else:
        next_question()


def next_question():
    global frm_question, frm_right, frm_wrong1,frm_wrong2, frm_wrong3
    rundom_number = randint(1, len(questions))
    frm_question = questions[rundom_number]["question"]
    frm_right = questions[rundom_number]["correct_ans"]
    frm_wrong1 = questions[rundom_number]["wrong_ans1"]
    frm_wrong2 = questions[rundom_number]["wrong_ans2"]
    frm_wrong3 = questions[rundom_number]["wrong_ans3"]
    show_data()
    show_question()
    btn_Ok.setText('Ок')


win_card = QWidget()
win_card.resize(card_width, card_height)


win_card.move(300,300)
win_card.setWindowTitle("Memory card")
#здесь должны быть параметры окна


win_card.setLayout(layout_card)
show_data()
show_question()
btn_Ok.clicked.connect(click_OK)
win_card.show()
app.exec_()
