from rest_framework.exceptions import ValidationError


class YoutubeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if not ('youtube.com' in tmp_value):
            raise ValidationError('Ссылка на сторонний ресурс')