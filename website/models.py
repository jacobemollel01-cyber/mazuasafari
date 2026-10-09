from django.db import models


class SafariInquiry(models.Model):

    full_name = models.CharField(max_length=150)

    email = models.EmailField()

    country = models.CharField(max_length=100, blank=True)

    phone = models.CharField(max_length=50, blank=True)

    travellers = models.PositiveIntegerField()

    days = models.PositiveIntegerField(blank=True, null=True)

    arrival = models.DateField(blank=True, null=True)

    departure = models.DateField(blank=True, null=True)

    destination = models.CharField(max_length=100, blank=True)

    accommodation = models.CharField(max_length=100, blank=True)

    budget = models.CharField(max_length=150, blank=True)

    requests = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
    
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    country = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    travellers = models.PositiveIntegerField(blank=True, null=True)
    days = models.PositiveIntegerField(blank=True, null=True)
    arrival = models.DateField(blank=True, null=True)
    departure = models.DateField(blank=True, null=True)

    destination = models.CharField(max_length=100, blank=True)
    accommodation = models.CharField(max_length=100, blank=True)
    budget = models.CharField(max_length=150, blank=True)
    requests = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"