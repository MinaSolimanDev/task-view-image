from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os, json
from simple.models import Items
import warnings

BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):
    help = "Loading items"

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs=1, type=str)

    def handle(self, *args, **options):
        file_name = options.get('file_name')[0]

        if not os.path.exists(BASE_DIR / str(file_name)):
            raise CommandError(
                'make sure you pass the correct file name and should be stored in the root folder')
        
        with open(BASE_DIR / str(file_name)) as f:
            data = json.load(f)
            items = data['items']
            
            if len(items) == Items.objects.count():
                warnings.warn("No changes detected")
                return
            
            for item in items:
                if not {'id', 'title', 'description', 'imageUrl'} <= item.keys():
                    raise CommandError(
                        'Invalid Structure item, should be contains `id, title, description, imageUrl`')
                store = {
                    "id": item.get('id'),
                    "title": item.get('title'),
                    "description": item.get('description'),
                    "imageUrl": item.get('imageUrl'),
                }
                Items.objects.update_or_create(**store)

                
