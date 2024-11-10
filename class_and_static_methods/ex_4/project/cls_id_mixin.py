class ClsIdMixin:
    id: int = 1

    @classmethod
    def increment_id(cls):
        cls.id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id
