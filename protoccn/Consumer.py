import Portal
from types import MethodType

class Consumer(object):
    def __init__(self, client, name, prefix):
        self.client = client
        self.name = name
        self.prefix = prefix

    def request(self, name):
        return self.client.get(name)

    def request_with_payload(self, name, payload):
        return self.client.get(name, payload)

    def install_sink(self, target, **options):
        def decorator(f):
            def wrapped_f(*args):
                suffix = f(*args)
                return self.request(target + "/" + suffix)
            return wrapped_f
        return decorator

    def install_rpc(self, target, **options):
        def decorator(f):
            def wrapped_f(*args):
                payload = f(*args)
                return self.request_with_payload(target, payload)
            return wrapped_f
        return decorator

    def register(self, name, target):
        func = lambda: self.request(target)
        setattr(self, name, func)

class TestConsumer(Consumer):
    def __init__(self, name, prefix = ""):
        Consumer.__init__(self, Portal.TestPortal(), name, prefix)
        self.name = name
        self.prefix = prefix

    def __str__(self):
        return self.__class__.__name__

class CCNConsumer(Consumer):
    def __init__(self, name, prefix = ""):
        Consumer.__init__(self, Portal.CCNPortal(), name, prefix)
        self.handlers = {}
        if (len(prefix) > 0):
            self.client.lisen(prefix)

    def __str__(self):
        return self.__class__.__name__
