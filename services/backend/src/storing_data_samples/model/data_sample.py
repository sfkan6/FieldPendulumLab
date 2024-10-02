import string, random, time


class DataSample:

    def __init__(self, name: str, timestamp: str, description: str, records: list):
        self.name = name
        self.timestamp = timestamp
        self.description = description
        self.records = records

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.name} - {self.timestamp}"

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def get_random_name(size=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(size))

    @classmethod
    def create_now(cls, name, description, records):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        return cls(name, timestamp, description, records)



