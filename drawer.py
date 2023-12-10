import os, csv, random, json, logging
from cryptography.fernet import Fernet
from participant import Participant
from paired import Paired
from mailer import Mailer

class Drawer:

    participants = []
    bown = []
    game = []

    def __init__(self) -> None:
        pass

    def read_data(self):
        logging.info("Reading [participants] input file")

        filename = f"{os.getenv('data_path')}/participants.csv"
        if not os.path.isfile(filename):
            raise Exception(f"File not found with name [{filename}], check yours configurations")

        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.participants.append(Participant(row[0], row[1]))
            random.shuffle(self.participants)
        logging.info(f"Done reading [participants] input file, with total of [{len(self.participants)} participants]")
        return self

    def random_participant(self) -> Participant|None:
        random.shuffle(self.bown)
        return self.bown.pop()

    def pairing(self) -> bool:
        self.bown = self.participants.copy()
        self.game = []
        i = 0
        while len(self.bown) > 0:
            secretFriend = self.random_participant()
            if self.participants[i].key == secretFriend.key:
                return False
            self.game.append(Paired(self.participants[i], secretFriend))
            i+=1
        return True

    def draw(self):
        logging.info("Start drawing game")
        while not self.pairing():
            pass
        logging.info("Done drawing game")
        return self

    def save(self):
        logging.info("Start encrypting and save game to file")
        serialized = json.dumps([ paired.to_dict() for paired in self.game ])
        encoded = Fernet(bytes(os.getenv("app_key"), "utf-8")).encrypt(bytes(serialized, "utf-8")).decode("utf-8")
        with open(f"{os.getenv('data_path')}/game.txt", "w") as game_file:
            game_file.write(encoded)
            game_file.close()
        logging.info("Done encrypting and save game to file")
        return self

    def from_exist(self):
        logging.info("Start reading existing game from file")

        filename = f"{os.getenv('data_path')}/game.txt"

        if not os.path.isfile(filename):
            raise Exception(f"File not found with name [{filename}], check yours configurations")

        with open(filename) as game_file:
            contents = game_file.read()
            game = json.loads(Fernet(bytes(os.getenv("app_key"), "utf-8"))
                        .decrypt(bytes(contents, "utf-8")).
                        decode("utf-8"))
            for pairs in game:
                self.game.append(Paired(
                    Participant(pairs["participant"]["name"],pairs["participant"]["email"]),
                    Participant(pairs["secret_friend"]["name"],pairs["secret_friend"]["email"])
                ))
        logging.info("Done reading existing game from file")
        return self

    def send_mails(self):
        logging.info("Start sending mails of drawed game")
        mailer = Mailer()
        for paired in self.game:
            mailer.send_message(paired)
        mailer.close()
        logging.info("Done sending mails of drawed game")

    def resend_one(self, name: str, email:str) -> bool:

        logging.info("Start sending specific participant email")

        for paired in self.game:
            if paired.participant.name == name:
                if email is not None:
                    paired.participant.email = email

                mailer = Mailer()
                mailer.send_message(paired)
                mailer.close()

                logging.info("Done sending specific participant email")
                return True

        logging.info(f"Not found participant with name [{name}]")
        raise Exception(f"Not found participant with name [{name}]")

    def __str__(self) -> str:
        return "\n".join([
            "\nParticipants:\n%s" % "\n".join([str(part) for part in self.participants]),
            "\nGame:\n%s" % "\n".join([str(paired) for paired in self.game]),
        ])
