from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model

User = get_user_model()


class LanguageModel(models.Model):
    class Levels(models.TextChoices):
        BAS = 'BAS', _('Basic')
        ADV = 'ADV', _('Advanced')
        PRO = 'PRO', _('Professional')
        BIL = 'BIL', _('Bilingual')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="languages")
    level = models.CharField(verbose_name=_("Level"), max_length=50, choices=Levels.choices, default=Levels.BAS)
    name = models.CharField(max_length=200, unique=True, verbose_name=_("Name"))

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')
        ordering = ['-name']

    def __str__(self):
        return f"{self.name}-{self.get_level_display()}"


class SkillModel(models.Model):
    class Types(models.TextChoices):
        HARD = 'HARD', _('Hard skills')
        SOFT = 'SOFT', _('Soft skills')

    class Levels(models.TextChoices):
        B = 'B', _('Beginner')
        S = 'S', _('Skilled')
        A = 'A', _('Advanced')
        E = 'E', _('Expert')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="skills")
    type = models.CharField(verbose_name=_("Type"), max_length=50, choices=Types.choices, default=Types.SOFT)
    level = models.CharField(verbose_name=_("Level"), max_length=50, choices=Levels.choices, default=Levels.S)
    name = models.CharField(max_length=200, unique=True, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"), max_length=2000, blank=True, )

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')
        ordering = ['-name']

    def __str__(self):
        return f"{self.name}"


class EducationModel(models.Model):
    class Levels(models.TextChoices):
        PE = 'PE', _('Primary education')
        LSE = 'LSE', _('Lower secondary education')
        USE = 'USE', _('Upper secondary education')
        PS = 'PS', _('Postsecondary non - tertiary education')
        SCT = 'SCT', _('Short - cycle tertiary education')
        BL = 'BL', _('Bachelor’s or equivalent level')
        ML = 'ML', _('Master’s or equivalent level')
        DL = 'DL', _('Doctor or equivalent level')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="educations")
    name = models.CharField(verbose_name=_("Name"), max_length=200)
    level = models.CharField(verbose_name=_("Level"), max_length=50, choices=Levels.choices, default=Levels.USE)
    institution = models.CharField(verbose_name=_("Institution"), max_length=150)
    level = models.CharField(verbose_name=_("Level"), max_length=50, choices=Levels.choices, default=Levels.USE)
    description = models.TextField(verbose_name=_("Description"), max_length=100, blank=True, )
    start_date = models.DateField(verbose_name=_("Start Date"), blank=True)
    end_date = models.DateField(verbose_name=_("End Date"), blank=True)

    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.name}-{self.get_level_display()}"


class CourseModel(models.Model):
    class Levels(models.TextChoices):
        PE = 'PE', _('Primary education')
        LSE = 'LSE', _('Lower secondary education')
        USE = 'USE', _('Upper secondary education')
        PS = 'PS', _('Postsecondary non - tertiary education')
        SCT = 'SCT', _('Short - cycle tertiary education')
        BL = 'BL', _('Bachelor’s or equivalent level')
        ML = 'ML', _('Master’s or equivalent level')
        DL = 'DL', _('Doctor or equivalent level')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="courses")
    name = models.CharField(verbose_name=_("Name"), max_length=200)
    institution = models.CharField(verbose_name=_("Institution"), max_length=150)
    level = models.CharField(verbose_name=_("Level"), max_length=50, choices=Levels.choices, default=Levels.USE)
    description = models.TextField(verbose_name=_("Description"), max_length=100, blank=True, )
    start_date = models.DateField(verbose_name=_("Start Date"), blank=True)
    end_date = models.DateField(verbose_name=_("End Date"), blank=True)

    def __str__(self):
        return f"{self.name}-{self.get_level_display()}"

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ['-start_date']


class ExperienceModel(models.Model):
    class Types(models.TextChoices):
        NONE = None, _('Unknown')
        SALAR = 'SALAR', _('Salaried')
        CHIEF = 'CHIEF', _('Founder/chief')
        FREEL = 'FREEL', _('Freelance/chief')
        INTER = 'INTER', _('Internship')
        OTHER = 'OTHER', _('other')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="experiences")
    type = models.CharField(verbose_name=_("Type"), max_length=10, choices=Types.choices, default=Types.INTER)
    position = models.CharField(verbose_name=_("Position"), max_length=200)
    company = models.CharField(max_length=200, verbose_name=_("Company"))
    context = models.TextField(max_length=1000, blank=True, verbose_name=_("Context"))
    summary = models.TextField(max_length=3000, blank=True, verbose_name=_("Summary"))
    start_date = models.DateField(verbose_name=_("Start Date"), blank=True)
    end_date = models.DateField(verbose_name=_("End Date"), blank=True)

    def __str__(self):
        return f"{self.position}-{self.company}"

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experiences')
        ordering = ['-start_date']


class StatementModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="statements")
    text = models.TextField(verbose_name=_("Personal statement"))

    class Meta:
        verbose_name = _('Personal statement')
        verbose_name_plural = _('Personal statements')

    def __str__(self):
        return self.text


class LetterModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="letters")
    text = models.TextField(verbose_name=_("Motivation letter"))

    class Meta:
        verbose_name = _('Motivation letter')
        verbose_name_plural = _('Motivation letters')

    def __str__(self):
        return self.text


class CertificationModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                             related_name="certifications")
    title = models.CharField(verbose_name=_("Title"), max_length=50)
    authority = models.CharField(verbose_name=_("Authority"), max_length=125)
    description = models.TextField(verbose_name=_("Description"), max_length=125, blank=True)
    date = models.DateField(verbose_name=_("Date obtained"), null=True, blank=True)

    class Meta:
        verbose_name = _('Certification')
        verbose_name_plural = _('Certifications')
        ordering = ['-date']

    def __str__(self):
        return f"{self.title}-{self.authority}"


class InterestModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="interests")
    name = models.CharField(verbose_name=_("Name"), max_length=50)

    class Meta:
        verbose_name = _('Interest')
        verbose_name_plural = _('Interests')
        ordering = ['name']

    def __str__(self):
        return f"{self.name}-{self.user}"


class PersonModel(models.Model):
    class Genders(models.TextChoices):
        M = 'F', _('Male')
        F = 'M', _('Female')

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=255)
    gender = models.CharField(verbose_name=_("Gender"), max_length=10, choices=Genders.choices, default=Genders.M)
    phone = models.CharField(verbose_name=_("Phone"), max_length=20, blank=True)
    email = models.EmailField(verbose_name=_("Email"), blank=True)
    website = models.URLField(verbose_name=_("Website"), max_length=300, blank=True, null=True)
    linkedin = models.URLField(verbose_name=_("Linkedin"), blank=True)
    address = models.CharField(verbose_name=_("Address"), max_length=255, blank=True)
    image = models.ImageField(verbose_name=_("Image"), blank=True, null=True, upload_to='images')
    image_thumbnail = ImageSpecField(source='avatar',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',
                                     options={'quality': 60})

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ResumeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="interests")
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    person = models.ForeignKey(PersonModel, verbose_name=_("Personal info"))
    statement = models.ForeignKey(StatementModel, verbose_name=_("Personal statement"))
    experiences = models.ManyToManyField(ExperienceModel, verbose_name=_("Experiences"))
    certifications = models.ManyToManyField(CertificationModel, verbose_name=_("Certifications"))
    educations = models.ManyToManyField(EducationModel, verbose_name=_("Education"))
    courses = models.ManyToManyField(CourseModel, verbose_name=_("Courses"))
    skills = models.ManyToManyField(SkillModel, verbose_name=_("Skills"))
    interests = models.ManyToManyField(InterestModel, verbose_name=_("Interests"))

    class Meta:
        verbose_name = _('Resume')
        verbose_name_plural = _('Resumes')
        ordering = ['name']

    def __str__(self):
        return f"{self.name}-{self.user}"
