from harness.input_validator import validate_user_request


def test_empty_request():

    valid, message = validate_user_request("")

    assert valid is False
    assert message == "Please enter a study request."


def test_request_too_short():

    valid, message = validate_user_request("study")

    assert valid is False


def test_valid_request():

    valid, message = validate_user_request(
        "I have 4 hours today and need to study Python and DSA."
    )

    assert valid is True
    assert message == ""
