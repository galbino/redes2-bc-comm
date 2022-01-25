class AbroadException(Exception):
    pass

class EntityNotFound(AbroadException):
    def __init__(self):
        message = dict(
            [
                ("code", 404),
                ("message", "The requested entity could not be found."),
                ("error_code", "entity_not_found"),
            ]
        )
        super().__init__(message)
