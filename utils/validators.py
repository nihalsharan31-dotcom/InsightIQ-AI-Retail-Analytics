from config import MAX_FILE_SIZE_MB


def validate_file(uploaded_file):
    """
    Validate uploaded file.
    Returns:
        (True, "") if valid
        (False, "Reason") if invalid
    """

    if uploaded_file is None:
        return False, "No file selected."

    size_mb = uploaded_file.size / (1024 * 1024)

    if size_mb > MAX_FILE_SIZE_MB:
        return False, f"File exceeds {MAX_FILE_SIZE_MB} MB."

    return True, ""