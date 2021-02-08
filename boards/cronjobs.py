from django.contrib.auth.models import User
from boards.models import Board, Topic, Post
from django.utils import timezone

def init_data_cron():
    try:
        # Clear users
        User.objects.filter(is_staff=False).delete()

        admin_users = User.objects.filter(is_staff=True)
        # print(admin_users[0])

        # Clear posts, topics and boards
        Post.objects.all().delete()
        Topic.objects.all().delete()
        Board.objects.all().delete()

        django_board = Board.objects.create(name='Django', description='Discussion on Django stuff')
        python_board = Board.objects.create(name='Python', description='Discussion on Python stuff')
        random_board = Board.objects.create(name='Random', description='Discussion on random stuff')

        for i in range(6):
            subject = 'Topic #{}'.format(i)
            topic = Topic.objects.create(subject=subject, board=django_board, started_by=admin_users[0])
            for i in range(51):
                Post.objects.create(message = 'Test message {}'.format(i), topic=topic,
                    updated_at=timezone.now(), created_by=admin_users[0])

            topic = Topic.objects.create(subject=subject, board=python_board, started_by=admin_users[0])
            for i in range(51):
                Post.objects.create(message = 'Test message {}'.format(i), topic=topic,
                    updated_at=timezone.now(), created_by=admin_users[0])

            topic = Topic.objects.create(subject=subject, board=random_board, started_by=admin_users[0])
            for i in range(51):
                Post.objects.create(message = 'Test message {}'.format(i), topic=topic,
                    updated_at=timezone.now(), created_by=admin_users[0])
        
        print('init_data_cron ran successfully!')
    except Exception as err:
        print(err)
        print('\n\n')
        print(err.with_traceback())



