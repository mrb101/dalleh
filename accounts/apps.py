from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    """
        Set the ready function to Register the Singals.
        set AccountsConfig as default_app_config in __init__
    """
    def ready(self):
        import accounts.signals
