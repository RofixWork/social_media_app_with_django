from django import template

register = template.Library()


@register.filter
def is_liked_by_user(post, user):
    """
    Checks if a given post is liked by the specified user.
    """
    return post.likes.filter(user=user).exists()
