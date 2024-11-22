from django.db import models
from django.utils.translation import gettext_lazy as _
from django_quill.fields import QuillField
from django.core import validators

# Create your models here.
class Standard_model(models.Model):
	statut = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
  

class ContactInfo(Standard_model):
    location = models.CharField(_("location"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    phone = models.CharField(_("phone"), max_length=50)
    coordinate = models.CharField(_("coordinate"), max_length=254)

    class Meta:
        verbose_name = _("ContactInfo")
        verbose_name_plural = _("ContactInfos")

    def __str__(self):
        return self.location

class Contact(Standard_model):
    name = models.CharField(_("name"), max_length=254)
    email = models.EmailField(_("email"), max_length=254)
    message = models.TextField(_("message"))
    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name
    

class Project(Standard_model):
    main_image = models.ImageField(_("main image"), upload_to="projects/main_image")
    title = models.CharField(_("title"), max_length=50)
    slogan = models.CharField(_("slogan"), max_length=50)
    description = QuillField(_("description"))
    mini_description = models.TextField(_("mini description"), null=True, blank=True)
    link = models.URLField(_("link"), null=True, blank=True)
    technologies = models.ManyToManyField("Technology", through="TechnologyProject")
    

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title


class Technology(Standard_model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to="technologies/image")
    

    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")

    def __str__(self):
        return self.name



class TechnologyProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    percentage = models.PositiveIntegerField(_("percentage"), validators=[validators.MaxValueValidator(100)])
    

    class Meta:
        verbose_name = _("TechnologyProject")
        verbose_name_plural = _("TechnologyProjects")

    def __str__(self):
        return self.percentage


