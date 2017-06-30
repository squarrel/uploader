"""Helper functions for the uploads app."""
from django.utils import timezone


def set_path(instance, filename):
    """Create a path-like string out of today's date.
    
    Keyword arguments:
    instance -- used for getting the existing value
    filename -- name of the file
    """
    today = timezone.now().date()
    today_str = str(today).replace('-', '/')
    result = 'media/' + today_str + '/' + filename
    return result
