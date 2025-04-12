from django.apps import AppConfig

class EmailParserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_parser'
    label = 'email_parser_main'  # ✅ Keep this
