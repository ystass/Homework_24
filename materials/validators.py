from rest_framework.serializers import ValidationError


class UrlValidator:
    """ Проверка ссылок на сторонние ресурсы, кроме youtube.com"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_url = dict(value).get(self.field)
        if tmp_url and "youtube.com" not in tmp_url:
            raise ValidationError('Ссылки могут быть только с youtube')
