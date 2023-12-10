import settings, logging
from cryptography.fernet import Fernet
from participant import Participant
from drawer import Drawer

def main():

    logging.info("Starting application, [app.py]")

    try:
        drawer = Drawer()
        drawer.read_data()\
            .draw()\
            .save()\
            .send_mails()
    except Exception as ex:
        logging.error(ex)

    logging.info("Finished application [app.py]")

if __name__ == '__main__':
    main()
