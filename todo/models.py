from django.db import models
from django.core.urlresolvers import reverse

class DateTime(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return unicode(self.datetime.strftime("%b %d, %Y, %I:%M %p"))
    
class User(models.Model) :
    name = models.CharField(max_length=60)
    def __unicode__(self):
        return unicode(self.name)

class Items(models.Model):
    name = models.CharField(max_length=60)
    created = models.ForeignKey(DateTime)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True)
    progress = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.name)

    def mark_done(self):
        return "<a href='%s'>Done</a>" % reverse("todo.views.mark_done", args=[self.pk])
    mark_done.allow_tags = True

    def progress_(self):
        return "<div style='width: 100px; border: 1px solid #ccc;'>" + \
          "<div style='height: 4px; width: %dpx; background: #555; '></div></div>" % self.progress
    progress_.allow_tags = True

