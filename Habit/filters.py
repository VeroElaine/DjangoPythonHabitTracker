from .models import Habit
import django_filters

class HabitFilter(django_filters.FilterSet):
	class Meta:
		model = Habit
		fields = ["habit","Mon","Tue","Wed","Thu","Fri","Sat","Sun","Time"]