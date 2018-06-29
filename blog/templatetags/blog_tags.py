from django import template
from django.db.models import Count
from ..models import Post
import datetime

register = template.Library()  # it's required that var called register


@register.simple_tag  # it's simple and just return data
def total_posts():
    return Post.published.count()


def small(text):
    return text.lower()


register.filter('small', small)


# or you can write it like this

@register.filter(name='cut')
def cut(value, arg):
    return str(value).replace(arg, '')


@register.simple_tag
def current_time(the_time):
    return datetime.datetime.now().strftime(the_time)


# inclusion tag that return render template + data

@register.inclusion_tag('blog/post/results.html')
def show_results(poll=['first', 'second', 'third']):
    choices = poll
    return {'choices': choices}


@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
