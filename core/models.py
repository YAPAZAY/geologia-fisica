from ckeditor.fields import RichTextField
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class SiteData(models.Model):

    def custom_uplad_to(instance, filename):
        try:
            if SiteData.objects:
                old_instance = SiteData.objects.get(
                    site_name=instance.site_name)
                old_instance.cover_image.delete()
        except ObjectDoesNotExist:
            pass
        return 'site/cover_image/' + filename

    def favicon_custom_uplad_to(instance, filename):
        try:
            if SiteData.objects:
                old_instance = SiteData.objects.get(
                    site_name=instance.site_name)
                old_instance.favicon.delete()
        except ObjectDoesNotExist:
            pass
        return 'site/favicon/' + filename

    site_name = models.CharField(
        verbose_name="Nombre del sitio", max_length=50, null=False)
    site_description = models.CharField(
        verbose_name="Descripción del sitio", max_length=500, null=False)
    cover_image = models.ImageField(
        upload_to=custom_uplad_to, verbose_name="Foto de portada del sitio",
        null=True, blank=True
    )
    favicon = models.ImageField(
        upload_to=favicon_custom_uplad_to, verbose_name="favicon del sitio",
        null=True, blank=True
    )
    site_home = RichTextField(
        verbose_name="Texto de bienvenida", null=True, blank=True)
    google_tag = models.CharField(
        verbose_name="Site Tag Google", max_length=500, null=True, blank=True)
    facebook_pixel = models.CharField(
        verbose_name="Pixel de Facebook", max_length=500,
        null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Información del Sitio'
        verbose_name_plural = 'Información del Sitio'
        ordering = ['updated_at']


class ContentManagmentSystem(models.Model):
    def custom_uplad_to(instance, filename):
        try:
            if ContentManagmentSystem.objects:
                old_instance = ContentManagmentSystem.objects.get(
                    slug=instance.slug)
                old_instance.avatar.delete()
        except ObjectDoesNotExist:
            pass
        return 'site/cms/' + filename

    slug = models.SlugField(max_length=250, primary_key=True)
    title = models.CharField(verbose_name="Título", max_length=200)
    main_picture = models.ImageField(
        upload_to=custom_uplad_to, verbose_name="Foto de portada"
    )
    content = RichTextField(
        verbose_name="Contenido", null=False
    )
    created_at = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'pagina estática'
        verbose_name_plural = 'paginas estáticas'
        ordering = ['title']

    def __str__(self):
        return self.title
