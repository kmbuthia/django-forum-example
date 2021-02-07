from django_cron import CronJobBase, Schedule
from django.contrib.auth.models import User
from boards.models import Board, Topic, Post
from django.utils import timezone

class InitDataCron(CronJobBase):
    RUN_EVERY_MINS = 30 # Every 30min
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'webforumproject.boards.init_data_cron'

    def do(self):
        # Clear users
        User.objects.filter(is_staff=False)

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


