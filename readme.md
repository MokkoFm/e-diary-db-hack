# db-hack

Скрипт для внесения изменения в базу данных ["Электронного дневника"](https://github.com/MokkoFm/e-diary).  
Для начала работы нужно скачать файл `scripts.py`, сохранить его рядом с файлом manage.py.  
После этого в консоли перейти в папку, где лежит файл `manage.py`, подключить базу данных.  

## Как запустить shell, что сделать сначала  
1. `python manage.py shell`  
2. Импортировать необходимые модули и библиотеки:
```
from datacenter.models import Schoolkid
from datacenter.models import Subject
from datacenter.models import Lesson
from datacenter.models import Teacher
from datacenter.models import Commendation
from datacenter.models import Chastisement
from datacenter.models import Mark
import random
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
```

## 1. Исправить оценки, убрать жалобы, добавить похвалу от учителя  

В функции main() есть переменные:  
`schoolboy_name` - ФИО школьника, кому нужно исправить оценки.  
`subject` - Предмет, к уроку которого нужно добавить похвалу.  
`commendations` - Примеры хвалебных слов от учителей, можно добавить свои варианты  
`schoolkid` - Получить доступ к объекту, чье ФИО лежит в переменной `schoolboy_name`  

1. Необходимо скопировать все переменные из функции main() с их значениеями в shell:  
```
def main():
    schoolboy_name = "Фролов Иван Григорьевич"
    schoolkid = get_object_or_404(Schoolkid, full_name=schoolboy_name)
    subject = "Математика"
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        ...
    ]
```

2. Скопировать одну за другой функции `create_commendation`, `remove_chastisements`, `fix_marks` в shell в таком формате:  
```
def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()
```

3. Теперь можно запускать функции, поочередно написав в shell:  
`main()` - подключаем переменные  
`create_commendation(schoolkid, subject)` - создать похвалу  
`remove_chastisements(schoolkid)` - удалить замечания  
`fix_marks(schoolkid)` - исправить все двойки и тройки на пятерки  

## 2. Помочь друзьям

1. Написать в файле `scripts.py` новые значения для переменных `schoolboy_name`, `subject`.  
2. Снова скопировать переменные `schoolboy_name`, `subject`, `schoolkid` в shell:  
```
def main():
    schoolboy_name = "Фролов Иван Григорьевич"
    schoolkid = get_object_or_404(Schoolkid, full_name=schoolboy_name)
    subject = "Математика"
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        ...
    ]
```
3. Запустить необходимые функции.   

## 3. Ошибки ввода

1. В случае неверного ввода ФИО школьника программа сообщит об ошибке `Введи корректное имя школьника!`  
Необходимо проверить значение переменной `schoolboy_name`. После этого вновь скопировав код, как в пункте 1. 
2. В случае ошибки ввода названия предмета программа сообщит об ошибке `Введи корректное название предмета!`  
Необходимо проверить значение переменной `subject`. После этого вновь скопировать код, как в пункте 1. 