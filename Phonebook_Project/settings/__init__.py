import os

from .base import *
from decouple import config

DJANGO_MODULE_STR = config('SETTINGS')

if DJANGO_MODULE_STR == 'dev':
    from .dev import *
else:
    from .prod import *