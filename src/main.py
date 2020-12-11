import logging

from telegram.ext import Updater

import config
from handlers import get_handler, delete_handler, create_handler, start_handler, help_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def main():
    # init updater & dispatcher
    updater = Updater(token=config.TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    # handlers
    dispatcher.add_handler(get_handler)
    dispatcher.add_handler(delete_handler)
    dispatcher.add_handler(create_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
