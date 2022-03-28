from django import template
register = template.Library()





from django.contrib.auth import get_user_model
user_model = get_user_model()

@register.filter
def author_details(post_author):
  if not isinstance(post_author, user_model):
    return ""
  if post_author.first_name and post_author.last_name:
    name = f"{post_author.first_name} {post_auther.last_name}"
  else:
    name = f"{post_author.username}"
  
  return name