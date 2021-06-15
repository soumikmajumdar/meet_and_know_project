import uuid

def random_uuid():
    return str(uuid.uuid4())[:8].replace("-", " ").lower()
