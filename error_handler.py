from models import WorkflowError


def create_workflow_error(
    error_type: str,
    message: str,
    recoverable: bool
):
    """
    Create a structured workflow error.
    """

    return WorkflowError(
        error_type=error_type,
        message=message,
        recoverable=recoverable
    )