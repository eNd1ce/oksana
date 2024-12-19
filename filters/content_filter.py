import re

def is_appropriate(message):
    for pattern in forbidden_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            return False
    return True
