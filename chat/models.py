from django.db import models

class UserChat(models.Model):
    username = models.CharField(max_length=100, unique=True)
    sessions = models.JSONField(default=list)

    def create(username):
        if not UserChat.objects.filter(username=username).exists():
            UserChat.objects.create(username=username, sessions=[])

    def get(username):
        return UserChat.objects.filter(username=username).first()

    def add_session(username, model_name):
        user_chat = UserChat.objects.filter(username=username).first()
        if user_chat:
            user_chat.sessions.append({"model": model_name, "messages": []})
            user_chat.save()

    def add_message(username, model_name, role, content):
        user_chat = UserChat.objects.filter(username=username).first()
        if user_chat:
            for session in user_chat.sessions:
                if session['model'] == model_name:
                    session['messages'].append({"role": role, "content": content})
                    break
            user_chat.save()
