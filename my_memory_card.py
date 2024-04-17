from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import shuffle
from random import randint
class Question():
        def __init__(self, quest, right, wrong1, wrong2, wrong3):
                self.quest= quest
                self.right=right
                self.wrong1= wrong1
                self.wrong2= wrong2
                self.wrong3= wrong3
questions_list = [Question('Как переводится слово "дерево"?', 'tree', 'three', 'willow', 'derevo'),
                Question("Как переводится слово 'яблоко'?", 'apple', 'pineapple','tomato','apply'),
                Question('Как переводится слово "кот"?', 'cat','dog', 'catch', 'poodle'),
                Question("Как переводится слово 'хлеб'?", 'bread', 'xleb','bred','hleb'),
                Question("какой жанр у 'Ромео и Джульеты'?", 'трагедия', 'драмма','не знаю','комедия'),
                Question("сколько лет пирамамиде Хеопса?", '5000', '1000','10000','80000'),
                Question("Как умер Никола Тесла?", 'болезнь', 'старость','от удара током','от смеха'),
                Question("В какой стране есть Ейфелевая башня?", 'Франция', 'Италия','Узбекистан','Австралия'),
                Question("Какой национальности не существует?", 'Смурфы', 'Алеуты','Чулымцы','Энцы'),
                Question("Как называют жительницу болгарии?", 'Болгарка', 'Болгария','Болгарянка','Дрель')]       
                

app=QApplication([])

RadioGroupBox= QGroupBox('Варианты ответов')

main_win=QWidget()

main_win.setWindowTitle('memory card')

question=QLabel('Какой национальности не существует')

varianti=QLabel('Варианты ответов')

btn_OK=QPushButton('ответить')

answer_1=QRadioButton('Энцы')
answer_2=QRadioButton('Смурфы')
answer_3=QRadioButton('Чулымцы')
answer_4=QRadioButton('Алеуты')

RadioGroup=QButtonGroup()
RadioGroup.addButton(answer_1)
RadioGroup.addButton(answer_2)
RadioGroup.addButton(answer_3)
RadioGroup.addButton(answer_4)


layout_quest1= QHBoxLayout()
layout_quest2= QVBoxLayout()
layout_quest3= QVBoxLayout()

layout_quest2.addWidget(answer_1)
layout_quest2.addWidget(answer_2)
layout_quest3.addWidget(answer_3)
layout_quest3.addWidget(answer_4)
layout_quest1.addLayout(layout_quest2)
layout_quest1.addLayout(layout_quest3)
RadioGroupBox.setLayout(layout_quest1)

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()


RadioGroupBox.setLayout(layout_line1)

AnsGroupBox = QGroupBox("Результаты")
lb_Result = QLabel("Верно/Неверно")
lb_Correct = QLabel("Правильный ответ")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)

layout_line1.addWidget(question, alignment=Qt.AlignCenter)
layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(RadioGroupBox)
layout_line3.addWidget(btn_OK,stretch=3)
RadioGroupBox.hide()
layout_card= QVBoxLayout()

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

def show_result():
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('следующий вопрос')
def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('ответить')
        RadioGroup.setExclusive(False)
        answer_1.setChecked(False)
        answer_2.setChecked(False)
        answer_3.setChecked(False)
        answer_4.setChecked(False)
        RadioGroup.setExclusive(True)

answers=[answer_1, answer_2, answer_3, answer_4]
def ask(q):
        shuffle(answers)
        answers[0].setText(q.right)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        question.setText(q.quest)
        lb_Correct.setText(q.right)
        show_question()
def show_correct(res):
        lb_Result.setText(res)
        show_result()
def check_answer():
        if answers[0].isChecked():
                show_correct('верно')
                main_win.score +=1
        else:
                if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                        show_correct('неверно')
        print(f'сстатистика\n всего вопросов:{main_win.total}\nправильных ответов:{main_win.score}')
        print(f'рейтинг:{main_win.score/main_win.total*100}%')

def next_question():
        main_win.total +=1
        print(f'сстатистика\n всего вопросов:{main_win.total}\nправильных ответов:{main_win.score}')
        current_question =randint(0, len(questions_list)-1)
        q= questions_list[current_question]
        ask(q)
def click_ok():
        if btn_OK.text()=='ответить':
                check_answer()
        else:
                next_question()



main_win.total=0
main_win.score=0
next_question()
btn_OK.clicked.connect(click_ok)
main_win.setLayout(layout_card)
main_win.show()
app.exec()
