from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    def custom_uplad_to(instance, filename):
        if Profile.objects:
            old_instance = Profile.objects.get(pk=instance.pk)
            old_instance.avatar.delete()
        return 'profiles/' + filename

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to=custom_uplad_to, null=True, blank=True
    )
    occupation = models.CharField(
        verbose_name="Ocupación", max_length=25,
        null=True, blank=True
    )
    institution = models.CharField(
        verbose_name="Institución", max_length=25,
        null=True, blank=True
    )
    bio = models.CharField(
        verbose_name="Biografía", max_length=300,
        null=True, blank=True)
    approved = models.BooleanField(
        verbose_name="Aprobado", null=False, default=False 
    )


@receiver(post_save, sender=User)
def ensure_profile_creation(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
