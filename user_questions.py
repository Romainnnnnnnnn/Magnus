import user_question_elo
import user_question_couleur

def questions():

    color = user_question_couleur.question_couleur()
    elo = user_question_elo.question_elo()
    return color, elo