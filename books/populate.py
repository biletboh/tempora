import json

from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware

from books.models import Book

def get_aware_datetime(date_str):
    ret = parse_datetime(date_str)
    if not is_aware(ret):
        ret = make_aware(ret)
    return ret


# posts = json.load(open('posts.json'))
# data = posts[2]['data']

def populate_books(data):
    for p in data:
        if (p['post_content']).strip() != '':
            date = get_aware_datetime(p['post_date'])
            if not Book.objects.filter(title=p['post_title']).exists():
                b = Book.objects.create(
                        pub_date=date, title=p['post_title'],
                        description=p['post_content'], slug=p['ID'])
                print(b)
