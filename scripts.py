from datacenter.models import Schoolkid
from datacenter.models import Subject
from datacenter.models import Lesson
from datacenter.models import Teacher
from datacenter.models import Commendation
from datacenter.models import Chastisement
from datacenter.models import Mark
import random
from django.core.exceptions import ObjectDoesNotExist


def create_commendation(schoolkid, subject):
    lesson = Lesson.objects.filter(
        year_of_study=6, group_letter="А", subject__title__contains=subject).order_by('date').first()
    date = lesson.date
    teacher = lesson.teacher
    subject = lesson.subject
    new_commendation = Commendation.objects.create(text=random.choice(
        commendations), created=date, schoolkid=schoolkid, subject=subject, teacher=teacher)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()


def main():
    schoolboy_name = "Фролов Иван Григорьевич"
    schoolkid = Schoolkid.objects.get(full_name=schoolboy_name)
    subject = "Математика"
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]

    try:
        create_commendation(schoolkid, subject)
        remove_chastisements(schoolkid)
        fix_marks(schoolkid)

    except ObjectDoesNotExist:
        print('Введи корректное имя школьника!')

    except AttributeError:
        print('Введи корректное название предмета!')


if __name__ == "__main__":
    main()
