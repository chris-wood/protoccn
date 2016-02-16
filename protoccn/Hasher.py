import hashlib

class Hasher(object):
    def __init__(self):
        pass

    def hash(self, msg):
        h = hashlib.new("sha256")
        h.update(msg)
        return h.hexdigest()
