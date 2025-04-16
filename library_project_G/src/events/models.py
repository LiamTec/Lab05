from django.db import models
from django.utils.text import slugify
from django.conf import settings  # para usar AUTH_USER_MODEL


class Event(models.Model):
    """Library event like book club, reading, etc."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_participants = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def is_full(self):
        return self.registrations.count() >= self.max_participants


class Participant(models.Model):
    """Person registering for events"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Registration(models.Model):
    """Event registration"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'participant')

    def __str__(self):
        return f"{self.participant} -> {self.event}"


class Attendance(models.Model):
    """Attendance report"""
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.registration} - {'Attended' if self.attended else 'Missed'}"
