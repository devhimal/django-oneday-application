import datetime
from django.utils import timezone
from poll.models import Question, Choice

# Delete existing data
Question.objects.all().delete()
Choice.objects.all().delete()

# Create a question
q1 = Question(question_text="What's new in Python 3.13?", pub_date=timezone.now())
q1.save()

# Add choices to the question
q1.choice_set.create(choice_text='Improved GIL', votes=0)
q1.choice_set.create(choice_text='New JIT compiler', votes=0)
q1.choice_set.create(choice_text='Better error messages', votes=0)

# Create another question
q2 = Question(question_text="What is your favorite web framework?", pub_date=timezone.now() - datetime.timedelta(days=5))
q2.save()

# Add choices to the question
q2.choice_set.create(choice_text='Django', votes=0)
q2.choice_set.create(choice_text='Flask', votes=0)
q2.choice_set.create(choice_text='FastAPI', votes=0)
q2.choice_set.create(choice_text='Ruby on Rails', votes=0)

print("Sample data created successfully!")
