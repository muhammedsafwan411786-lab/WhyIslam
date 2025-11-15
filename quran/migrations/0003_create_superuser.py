    from django.db import migrations
    import os

    def create_superuser(apps, schema_editor):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        username = os.environ.get('ADMIN_USER', 'admin')
        password = os.environ.get('ADMIN_PASSWORD', 'adminpass123')
        email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')

        if not User.objects.filter(username=username).exists():
            print(f'Creating superuser: {username}')
            User.objects.create_superuser(username=username, email=email, password=password)
        else:
            print(f'Superuser {username} already exists.')

    class Migration(migrations.Migration):

        dependencies = [
            ('quran', '0002_remove_verse_word_by_word_alter_verse_tafsir_text'),
        ]

        operations = [
            migrations.RunPython(create_superuser),
        ]
    