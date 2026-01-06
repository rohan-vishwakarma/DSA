class DatabaseConnect:

    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

db1 = DatabaseConnect()

db2 = DatabaseConnect()

print(db1 is db2)