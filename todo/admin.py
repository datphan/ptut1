from django.contrib import admin
from todo.models import *
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.utils.html import escape
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

import json

class ItemsAdmin(admin.ModelAdmin):
    list_display = ("name", "priority", "difficulty", "progress_", "created", "mark_done", "done")
    search_fields = ["name"]

class ItemsInline(admin.TabularInline):
    model = Items

class DateAdmin(admin.ModelAdmin):
    list_display = ["datetime"]
    inlines = [ItemsInline]

    def response_add(self, request, obj, post_url_continue='../%s/'):
        """ Determines the HttpResponse for the add_view stage.  """
        opts = obj._meta
        pk_value = obj._get_pk_val()

        msg = "Item(s) were added successfully 2."
        # Here, we distinguish between different save types by checking for
        # the presence of keys in request.POST.
        if request.POST.has_key("_continue"):
            self.message_user(request, msg + ' ' + _("You may edit it again below 2."))
            if request.POST.has_key("_popup"):
                post_url_continue += "?_popup=1"
            return HttpResponseRedirect(post_url_continue % pk_value)

        if request.POST.has_key("_popup"):
            return HttpResponse(
              '<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");'
              '</script>' % (escape(pk_value), escape(obj)))
        elif request.POST.has_key("_addanother"):
            self.message_user(request, msg + ' ' + (_("You may add another %s below 4.") %
                                                    force_unicode(opts.verbose_name)))
            return HttpResponseRedirect(request.path)
        else:
            self.message_user(request, msg)

        for item in Items.objects.filter(created=obj):
            if not item.user:
                item.user = request.user
                item.save()

            return HttpResponseRedirect(reverse("admin:todo_item_changelist"))

admin.site.register(Items, ItemsAdmin)
admin.site.register(DateTime, DateAdmin)
admin.site.register(User)