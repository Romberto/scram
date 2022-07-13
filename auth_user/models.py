from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    POSITIONS = (
        ('DR', 'директор'),
        ('MP', 'менеджер по продажам'),
        ('BG', 'бухгалтер'),
        ('MD', 'менеджер по работе с документами')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=40, choices=POSITIONS)

    class Meta:
        verbose_name = "профайл юзера"
        verbose_name_plural = "профайлы юзеров"

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
