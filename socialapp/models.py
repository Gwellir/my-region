from django.db import models
from django.utils.translation import gettext_lazy as _

# from authapp.models import AppUser
# from travelapp.models import Trip
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit

from my_region.constants import CommentPhotoSizes


class Comment(models.Model):
    """
    Модель абстрактного комментария.
    """
    author = models.ForeignKey('authapp.AppUser', verbose_name='Автор', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Текст')
    added_at = models.DateTimeField(verbose_name='Время добавления', db_index=True, auto_now_add=True)
    last_edit = models.DateTimeField(verbose_name='Время изменения', auto_now_add=True)
    is_allowed = models.BooleanField(verbose_name='Прошёл модерацию', db_index=True, default=True)
    is_active = models.BooleanField(verbose_name='Не удалён', db_index=True, default=True)


class TripScore(models.IntegerChoices):
    """
    Перечисление оценок походов.
    """
    TERRIBLE = 1, _('Ужасно')
    BAD = 2, _('Плохо')
    AVERAGE = 3, _('Средне')
    GOOD = 4, _('Хорошо')
    AWESOME = 5, _('Отлично')


class InstructorScore(models.IntegerChoices):
    """
    Перечисление вариантов оценки работы инструктора.
    """
    LIKED = 1, _('Понравился')
    NOT_LIKED = 2, _('Не понравился')


class TripComment(Comment):
    """
    Модель комментария к походу.
    """
    trip = models.ForeignKey('travelapp.Trip', verbose_name='Поход', related_name='comments', on_delete=models.CASCADE)
    # trip specific fields
    score = models.IntegerField(verbose_name='Оценка похода',
                                choices=TripScore.choices)
    instructor_score = models.IntegerField(verbose_name='Оценка инструктора',
                                           choices=InstructorScore.choices,
                                           null=True)
    # difficulty?

    def __str__(self):
        return f'{self.score}* - {self.author}: {self.trip}'


class CommentPhoto(models.Model):
    """
    Модель для хранения пользовательских фотографий похода.
    """
    comment = models.ForeignKey(Comment, verbose_name='Комментарий', related_name='photos', on_delete=models.CASCADE)
    added_at = models.DateTimeField(verbose_name='Добавлено', auto_now_add=True)
    image = ProcessedImageField(upload_to='comment_media',
                                processors=[ResizeToFit(
                                    CommentPhotoSizes.MAX_WIDTH,
                                    CommentPhotoSizes.MAX_HEIGHT,
                                )],
                                format='JPEG',
                                options={'quality': 80},)
    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFit(
                                     CommentPhotoSizes.THUMB_WIDTH,
                                     CommentPhotoSizes.THUMB_HEIGHT,
                                 )],
                                 format='JPEG',
                                 options={'quality': 70},)
