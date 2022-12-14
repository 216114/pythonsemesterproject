def create_q():
    create_q.questions = []
    create_q.variants_of_answer = []
    create_q.correct_answers = []
    how_much_question = int(input("How much question you want create?: "))
    for i in range(1,how_much_question+1):
        q = input(f"Type Your {i} question: ")
        create_q.questions.append(q)
        for j in range(1,5):
            variant = input(f"Your {j} Variant of answer: ")
            create_q.variants_of_answer.append(variant)
        true_answer = int(input(f"And which of variants True?(type number of variant): "))
        create_q.correct_answers.append(true_answer)

def choise_btw_gm():
    gm_choise = int(input("You want play with custom questions or Our version? (type 1 for custom, type 2 to Our version): ")) #gm - GameMode
    if gm_choise == 1:
        create_q()
        main_game(1)
    if gm_choise == 2:
        main_game(2)

def main_game(gm):
    if gm == 1:
        bank = 10
        print('\nInstructions:\nFor each question, select the correct answer by choosing 1, 2, 3 or 4.')
        for w in range(len(create_q.questions)):
            print(f"Question: {create_q.questions[w]}")
            for e in range(w*4, w*4+4):
                print(f"Variant:{create_q.variants_of_answer[e]}")
            player_choise = int(input())
            if player_choise == create_q.correct_answers[w]:
                print(f"Correct. You won {bank**w}")
            else:
                print("Seems its not correct answer. Sorry. But you lose Game")
                exit()
        print("WOAH YOU ARE A MONSTER. YOU ANSWERED CORRECTLY TO ALL QUESTION")
    elif gm == 2:
        bank = 10
        questions = ['Какое растение существует на самом деле?', 'Что за место, попав в которое, человек делает селфи на кухне, которую не может себе позволить?', 'Что проводит боксер, наносящий удар противнику снизу?', 'К кому первому обратились за помощью дед и бабка, не справившись с репкой?', 'Ответ 2', 'Заранее Извиняюсь За Опоздание', 'Но Когда я начал это делать не смотря на другие похожие проекты, у меня столько прикольных и эффективных идей было (Спасибо большое)', 'Я устал писать', 'Серьезно', 'все']
        variants_of_answer = ['Чилийский', 'Индийский', 'Русский', 'Британский', 'Рим', 'Лондон', 'Валлмарт', 'Икеа', 'Свинг', 'Хук', 'Апперкот', 'Джеб', 'К Жучке', 'К дочке', 'К внучке', 'К Ахмету', '2', '2', '2', '2', 'прошу', 'меня', 'простить', 'Пожалуста (Это ответ)', 'Это правильный ответ', 'Прикол', 'Прекол', 'Мем', 'ответ', 'лол', 'лол', 'лол', 'Тру Ансвер', 'не тру', 'не тру', 'не тру', 'Ответ', '.', '.', '.']
        correct_answers = [2, 4, 3, 3, 2, 4, 1, 1, 1, 1]
        print('\nInstructions:\nFor each question, select the correct answer by choosing 1, 2, 3 or 4.')
        for w in range(len(questions)):
            print(f"Question: {questions[w]}")
            for e in range(w*4, w*4+4):
                print(f"Variant:{variants_of_answer[e]}")
            player_choise = int(input())
            if player_choise == correct_answers[w]:
                print(f"Correct. You won {bank**w}")
            else:
                print("Seems its not correct answer. Sorry. But you lose Game")
                exit()
        print("WOAH YOU ARE A GENIUS. YOU ANSWERED CORRECTLY TO ALL QUESTIONS")

choise_btw_gm()
