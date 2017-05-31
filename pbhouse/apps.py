from django.apps import AppConfig


class PbhouseConfig(AppConfig):
    name = 'pbhouse'

    def ready(self):
        import pbhouse.signals

