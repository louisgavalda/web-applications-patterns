from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Submit an URL."

    def add_arguments(self, parser):
        parser.add_argument("url", nargs="+", type=str)

    def handle(self, *args, **options):
        for url in options["url"]:
            self.stdout.write(self.style.SUCCESS(f"[+] submitted: {url}"))
