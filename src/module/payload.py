class Payload:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                setattr(self, key, Payload(**value))
            else:
                setattr(self, key, value)

    def set_attr(self, key, value) -> None:
        if isinstance(key, Payload):
            setattr(self, key, Payload(**value))
        else:
            setattr(self, key, value)
