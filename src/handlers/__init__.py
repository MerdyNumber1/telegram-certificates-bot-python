from telegram.ext import CommandHandler
from .get_handler import get_handler
from .create_handler import create_handler
from .delete_handler import delete_handler
from .start_handler import start_handler
from .help_handler import help_handler

get_handler = CommandHandler('get', get_handler)
create_handler = CommandHandler('create', create_handler)
delete_handler = CommandHandler('delete', delete_handler)
start_handler = CommandHandler('start', start_handler)
help_handler = CommandHandler('help', help_handler)
