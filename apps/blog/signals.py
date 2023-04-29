from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from apps.blog.models import Post
from apps.accounts.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site


@receiver(post_save, sender=Post)
def email_notification(sender, instance, created, **kwargs):
    if created:
        DOMAIN = "localhost:8000"
        email_subject = "Новый пост на News Blog. Будь в курсе актуальных событий"
        posts = Post.objects.filter(is_active=True).order_by("-created_at")[:3]
        message = render_to_string("new_post_email.html", {"posts": posts, "domain": DOMAIN})
        to_emails = User.objects.all().values_list("email", flat=True)
        email = EmailMessage(email_subject, message, to=to_emails)
        email.content_subtype = "html"
        email.send()