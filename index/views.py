from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext
from django.http import HttpResponse
from el_pagination.decorators import page_template

# Create your views here.
from .models import Episode, AnimeTitle, Schedule

@page_template('release_item.html')
def posts_home(request, template='index.html', extra_context=None):
    context = {
        'object_list': Episode.objects.all(),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))

def post_detail(request, id=None):
	instance = get_object_or_404(AnimeTitle, id=id)
	i_episode = AnimeTitle.objects.filter(id = id)
	episode = Episode.objects.filter(AnimeTitle__in=i_episode)
	context = {
		"instance": instance,
		"title": instance.title,
		"episode": episode,
	}
	return render(request, 'detail.html', context)

def schedule(request):
	i_monday = Schedule.objects.filter(title = 'Monday')
	monday = AnimeTitle.objects.filter(schedule__in=i_monday)
	i_tuesday = Schedule.objects.filter(title = 'Tuesday')
	tuesday = AnimeTitle.objects.filter(schedule__in=i_tuesday)
	i_wednesday = Schedule.objects.filter(title = 'Wednesday')
	wednesday = AnimeTitle.objects.filter(schedule__in=i_wednesday)
	i_thursday = Schedule.objects.filter(title = 'Thursday')
	thursday = AnimeTitle.objects.filter(schedule__in=i_thursday)
	i_friday = Schedule.objects.filter(title = 'Friday')
	friday = AnimeTitle.objects.filter(schedule__in=i_friday)
	i_saturday = Schedule.objects.filter(title = 'Saturday')
	saturday = AnimeTitle.objects.filter(schedule__in=i_saturday)
	i_sunday = Schedule.objects.filter(title = 'Sunday')
	sunday = AnimeTitle.objects.filter(schedule__in=i_sunday)
	context = {
		"monday":monday,
		"tuesday":tuesday,
		"wednesday":wednesday,
		"thursday":thursday,
		"friday":friday,
		"saturday":saturday,
		"sunday":sunday,
	}
	return render(request, 'schedule.html', context)

def curseason(request):
	i_season = Schedule.objects.filter(title = 'CurrentSeason')
	season = AnimeTitle.objects.filter(schedule__in=i_season)
	context = {
		"season":season,
	}
	return render(request, 'current_season.html', context)

def all_anime(request):
	context = {
        'object_list': AnimeTitle.objects.all().order_by('title'),
    }
	return render(request, 'all_anime.html', context)