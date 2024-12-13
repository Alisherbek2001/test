import pandas as pd
from .models import Subject, SubSubject, Question, Answer


def import_questions_from_excel(file_path, subject_id, owner):
    data = pd.read_excel(file_path).dropna(how="all")

    subject = Subject.objects.get(id=subject_id)
    for index, row in data.iterrows():
        print(index)
        question_text = row.iloc[0]
        correct_answer = row.iloc[1]
        other_answers = row.iloc[2:-1].tolist()
        sub_subject_name = row.iloc[-1]

        if not sub_subject_name or pd.isna(sub_subject_name):
            continue

        sub_subject = SubSubject.objects.filter(
            name=sub_subject_name, subject=subject
        ).first()
        if not sub_subject:
            continue

        question = Question.objects.create(
            text=question_text, subject=subject, sub_subject=sub_subject, owner=owner
        )

        Answer.objects.create(text=correct_answer, question=question, is_correct=True)

        for answer_text in other_answers:
            Answer.objects.create(text=answer_text, question=question, is_correct=False)

    print("Savollar va javoblar muvaffaqiyatli yuklandi.")
