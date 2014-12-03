from django.db import models


class MyBio(models.Model):
    '''
    Main model for my bio
        first_name - my first name
        last_name - my last name
        birth_date = my birth date
        biography - my biography text area
        contacts - my contacts area
        other_contacts - my other contacts
    '''
    first_name = models.CharField(u"Name", max_length=50)
    last_name = models.CharField(u"Last name", max_length=50)
    birth_date = models.DateField(u"Date of birth", blank=True)
    biography = models.TextField(u"Bio", blank=True)
    contacts = models.TextField(u"Contacts", blank=True)
    other_contacts = models.TextField(u"Other contacts", blank=True)

    def __unicode__(self):
        return "Bio data for {0} {1}".format(self.first_name, self.last_name)