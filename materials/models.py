from django.db import models

from config import settings

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")

    description = models.TextField(verbose_name="Описание", **NULLABLE)

    preview = models.ImageField(
        upload_to="materials/courses", verbose_name="Превью", **NULLABLE
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель курса",
        **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название", help_text="Укажите название урока"
    )

    description = models.TextField(verbose_name="Описание", **NULLABLE)

    preview = models.ImageField(upload_to="materials/lessons", **NULLABLE)

    url = models.URLField(verbose_name="Ccылка на видео", **NULLABLE)

    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, verbose_name="Курс", **NULLABLE
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель урока",
        **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.course} - {self.user}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
