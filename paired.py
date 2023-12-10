from participant import Participant

class Paired:
    def __init__(self, participant: Participant, secret_friend: Participant) -> None:
        self.participant = participant
        self.secret_friend = secret_friend

    def __str__(self) -> str:
        return f"{self.participant.name.ljust(20)} {self.secret_friend.name}"

    def to_dict(self):
        return {
            "participant": self.participant.to_dict(),
            "secret_friend": self.secret_friend.to_dict(),
        }
