# - *- coding: utf- 8 - *-
__author__ = 'alexaled'

from django.apps import apps
from django.core.management.base import BaseCommand
import sys


class Command(BaseCommand):

    help = 'This command print all models and count their elements'

    def handle(self, *args, **options):

        result_list = []
        for model in apps.get_models():
            result_list.append('[%s] - %s objects' % (model.__name__,
                                        model._default_manager.count()))
        result_list = '\n'.join(result_list)
        sys.stdout.write(result_list)
        sys.stderr.write("\nerror: " + result_list)

        return result_list
