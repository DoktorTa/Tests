class StatusCodeResponseReservation:  # Поля в этой хуйне надо бы захуевертить на дискрипторах, если будет время.
    SUCCESS = 'success'
    ERROR = 'error'
    CRITICAL = 'critical'  # Не оч круто рассказывать всему интернету, что у вас, что-то наебнулось.

class StatusCodeResponseStatus:
    FOUND = 'found'
    NOT_FOUND = 'not_found'
    ERROR = 'error'
