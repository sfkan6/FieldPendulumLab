import json, time


class Record:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def create_by_json(cls, data_json):
        data = json.loads(data_json)
        return cls(**data)



class AngleRecord(Record):

    def __init__(self, angle: int|float, timestamp: int|float):
        self.angle = angle
        self.timestamp = timestamp

    @classmethod
    def create_now(cls, angle, n=6) -> Record:
        timestamp = round(time.time(), n)
        return cls(angle, timestamp)

    @classmethod
    def create_now_relative_to_start_time(cls, angle, start_time, n=6):
        timestamp = round(time.time() - start_time, n)
        return cls(angle, timestamp)


