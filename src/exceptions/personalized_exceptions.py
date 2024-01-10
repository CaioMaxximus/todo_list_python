

class Personalized_Exception(Exception):
    pass

class TaskValidationError(Personalized_Exception):
    pass

class TaskRemovalError(Personalized_Exception):
    pass

class TaskCompletionError(Personalized_Exception):
    pass