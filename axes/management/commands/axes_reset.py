from django.core.management.base import BaseCommand

from axes.utils import reset


class Command(BaseCommand):
    help = ("resets any lockouts or failed login records. If called with an "
            "IP, resets only for that IP")

    def add_arguments(self, parser):
        parser.add_argument('ip', nargs='*')

    def handle(self, *args, **kwargs):
        count = 0
        if kwargs and kwargs.get('ip'):
            for ip in kwargs['ip'][1:]:
                count += reset(ip=ip)
        else:
            count = reset()

        if count:
            print('{0} attempts removed.'.format(count))
        else:
            print('No attempts found.')
