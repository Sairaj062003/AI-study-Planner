from llm import structured_request_parser

from prompts import request_parser_prompt


def parse_user_request(user_request: str):
    """
    Convert a natural-language user request
    into structured UserRequest data.
    """

    messages = request_parser_prompt.invoke({
        "user_request": user_request
    })

    try:

        response = structured_request_parser.invoke(
            messages
        )

        return response

    except Exception as error:

        print(
            "Request parsing failed."
        )

        raise RuntimeError(
            f"Unable to understand the study request: {error}"
        )