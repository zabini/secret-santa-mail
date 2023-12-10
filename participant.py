import hashlib

class Participant:

    def __init__(self, name: str, email: str) -> None:
        self.key = hashlib.sha1(f"{name}.{email}".encode('utf-8')).hexdigest()
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"Key: {self.key} | Name: {self.name.ljust(20)} | Email: {self.email}"

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
        }
