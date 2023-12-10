import settings, logging
from drawer import Drawer

def main():
    logging.info("Starting application, [resend.py]")

    try:
        drawer = Drawer()
        drawer.from_exist().send_mails()
    except Exception as ex:
        logging.error(ex)

    logging.info("Finished application [resend.py]")

if __name__ == '__main__':
    main()
