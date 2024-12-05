import pandas as pd
from .models import Question, Answer, Subject


def import_questions_from_excel(file_path, subject_id):
    data = pd.read_excel(file_path)

    subject = Subject.objects.get(id=subject_id)

    for index, row in data.iterrows():
        question_text = row.iloc[0]

        correct_answer = row.iloc[1]
        other_answers = row.iloc[2:].tolist()

        question = Question.objects.create(text=question_text, subject=subject)

        Answer.objects.create(text=correct_answer, question=question, is_correct=True)

        for answer_text in other_answers:
            Answer.objects.create(text=answer_text, question=question, is_correct=False)

    print("Savollar va javoblar muvaffaqiyatli yuklandi.")
