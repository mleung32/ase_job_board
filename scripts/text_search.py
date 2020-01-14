from django.contrib.postgres.search import SearchVector

Posting.objects.update(content_search=SearchVector('class_name','class_desc',
'semester', 'position', 'school', 'instructor', 'percent_time'))