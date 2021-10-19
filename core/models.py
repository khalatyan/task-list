from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

def content_file_name(instance, filename):
    return '/'.join(['content', instance.task.title, filename])

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        '''
        Создаёт и сохраняет пользователя
        '''
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''
        Создаёт и сохраняет суперпользователя
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    name = models.CharField(verbose_name='ФИО', max_length=255, blank=True)

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_uidb64(self):
        return urlsafe_base64_encode(force_bytes(self.id))


class Task(models.Model):
    title = models.CharField(max_length=560, verbose_name="Название")
    details = models.TextField(verbose_name='Описание')

    deadline =  models.DateTimeField(verbose_name='Дата завершения')
    executor = models.ForeignKey(User, verbose_name='Исполнитель', related_name='task_executor', on_delete=models.CASCADE)

    def __str__(self):
        return u'%s' % (self.title)
    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'Задачи'


class TaskFile(models.Model):
    file = models.FileField(verbose_name=u'Файл', upload_to=content_file_name)
    task = models.ForeignKey(Task, models.CASCADE, verbose_name="Задача")

    def __str__(self):
        return u'%s' % (self.file)

    class Meta:
        verbose_name = u"файл задач"
        verbose_name_plural = u"Файлы задач"
