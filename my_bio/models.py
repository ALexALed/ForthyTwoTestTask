from django.db import models, OperationalError
from sorl.thumbnail import get_thumbnail
from django.core.files.base import ContentFile
from django.db.models.signals import post_init, post_save, post_delete


class MyBio(models.Model):
    first_name = models.CharField(u"Name", max_length=50)
    last_name = models.CharField(u"Last name", max_length=50)
    birth_date = models.DateField(u"Date of birth", blank=True, null=True)
    biography = models.TextField(u"Bio", blank=True, null=True)
    email = models.EmailField(u"email", blank=True, null=True)
    skype = models.CharField(u"Skype", max_length=200, blank=True, null=True)
    jabber = models.EmailField(u"Jabber", blank=True, null=True)
    other_contacts = models.TextField(u"Other contacts", blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.photo and \
                        self.photo.width != 200 and self.photo.height != 200:
            super(MyBio, self).save(*args, **kwargs)
            resized = get_thumbnail(self.photo, "200x200",
                                    crop='center', quality=99)
            self.photo.save(resized.name,
                            ContentFile(resized.read()), save=True)
        super(MyBio, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Bio data for {0} {1}".format(self.first_name, self.last_name)


class HttpRequestSave(models.Model):
    http_request = models.CharField(max_length=300)
    remote_addr = models.IPAddressField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1)

    def __unicode__(self):
        return "Request to {0} at {1}".format(self.remote_addr, self.datetime)


class DataBaseEvents(models.Model):
    signal = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(blank=True, auto_now_add=True)

    def __unicode__(self):
        return "{0}-{1}-{2}".format(self.signal, self.model, self.date)


def signals_init(sender, **kwargs):
    save_signal(sender, 'init')


def signals_save(sender, **kwargs):
    save_signal(sender, 'save')


def signals_delete(sender, **kwargs):
    save_signal(sender, 'delete')


def save_signal(sender, signal):
    if sender.__name__ != 'DataBaseEvents':
        try:
            obj = DataBaseEvents()
            obj.model = sender.__name__
            obj.signal = signal
            obj.save()
        except OperationalError:
            pass


post_init.connect(signals_init, dispatch_uid='ForthyTwoTestTask.my_bio')
post_save.connect(signals_save, dispatch_uid='ForthyTwoTestTask.my_bio')
post_delete.connect(signals_delete, dispatch_uid='ForthyTwoTestTask.my_bio')
