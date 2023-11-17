from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField
    email = models.TextField
    phone = models.IntegerField(max_length=10)
    is_favorite = models.BooleanField(True)

    def create_contact(name, email, phone, is_favorite):
        contact = Contact(name=name, email=email, phone=phone, favorite=is_favorite)
        contact.save()
        return contact
    
    def all_contacts():
        all_contacts = Contact.objects.all()
        return all_contacts
    
    def find_contact_by_name(name):
        try:
            find_name = Contact.objects.get(name)
            return find_name
        except:
            return None
        
    def favorite_contacts():
        contacts = Contact.objects.all()
        return contacts
    
    def update_contact_email(name, new_email):
        contact = Contact.object.get(name)
        contact.email = new_email
        contact.save()
        return contact
    
    def delete_contact(name):
        contact = Contact.objects.get(name)
        contact.delete()
        return contact