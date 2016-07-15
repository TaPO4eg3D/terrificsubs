from django.contrib import admin

# Register your models here.
from .models import AnimeTitle, Episode, Schedule


class TitleAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp', 'updated')
	list_filter = ('timestamp', 'updated', 'release_time')
	search_fields = ('title', 'content')
	class Meta():
		model = AnimeTitle
class EpisodesAdmin(admin.ModelAdmin):
	def get_name(self, obj):
		return obj.AnimeTitle.title
	get_name.admin_order_field  = 'anime_title'  #Allows column order sorting
	get_name.short_description = 'Anime title'  #Renames column head
	list_display = ('title', 'timestamp', 'updated', 'get_name')
	list_filter = ('timestamp', 'updated')
	search_fields = ('title', 'timestamp', 'AnimeTitle__title')

	class Meta():
		model = Episode

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('title',)
	filter_horizontal = ('AnimeTitles',)
	class Meta():
		model = Schedule

admin.site.register(AnimeTitle, TitleAdmin)
admin.site.register(Episode, EpisodesAdmin)
admin.site.register(Schedule, ScheduleAdmin)

