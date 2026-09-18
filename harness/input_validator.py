MIN_REQUEST_LENGTH = 10
MAX_REQUEST_LENGTH = 1000


def validate_user_request(user_request : str):

    if not user_request:
        return False, "Please enter a study request."

    if len(user_request) < MIN_REQUEST_LENGTH:
        return False, "Your request is too short. Please describe what you want to study"
    if len(user_request) > MAX_REQUEST_LENGTH:
        return False, "Your request is too long. Please keep it under 1000 characters."
    return True , ""

