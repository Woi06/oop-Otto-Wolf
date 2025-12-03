def prefix_message(message, prefix="INFO"):
    return f"[{prefix}] {message}"

def timestamp_message(message):
    from datetime import datetime
    return f"[{datetime.now().isoformat()}] {message}"
