import sys, settings, logging, getopt
from drawer import Drawer

def read_params():
    # Options
    options = "hn:e:"
    # Long options
    long_options = ["help", "name=", "email="]
    arguments, values = getopt.getopt(sys.argv[1:], options, long_options)
    name: str = None
    email: str = None
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print("Display Help")
            sys.exit()
        if currentArgument in ("-n", "--name"):
            name = currentValue
        elif currentArgument in ("-e", "--email"):
            email = currentValue
    return name, email

def main():

    logging.info("Starting application [resend_one.py]")

    name, email = read_params()

    if name is None:
        print("Participant name need to be present to resent mail")
        logging.error("Participant name need to be present to resent mail")
        sys.exit(1)

    try:
        drawer = Drawer()
        drawer.from_exist().resend_one(name, email)
    except Exception as ex:
        logging.error(ex)

    logging.info("Finished application [resend_one.py]")

if __name__ == '__main__':
    main()
