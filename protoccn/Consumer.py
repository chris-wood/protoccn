# import PortalWrapper
from types import MethodType

class Consumer(object):
    def __init__(self, name, prefix = ""):
        # self.client = PortalWrapper.PortalWrapper()
        self.name = name
        self.handlers = {}
        if (len(prefix) > 0):
            self.prefix = prefix
            # self.client.lisen(prefix)

    def request(self, name):
        # return self.client.get(name)
        return "FETCHED from 'request' %s" % (name)

    def request_with_payload(self, name, payload):
        # return self.client.get(name, payload)
        return "FETCHED FROM THE NETWORK with %s %s" % (name, payload)

    def install_sink(self, target, **options):
        def decorator(f):
            def wrapped_f(*args):
                payload = f(*args)
                return self.request_with_payload(target, payload)
            return wrapped_f
        return decorator

    def register(self, name, target):
        func = lambda: self.request(name)
        setattr(self, name, func)

    def install(self, msg):
        pass

    def __str__(self):
        return ""

app = Consumer(__name__, "/my/name")

# Register a method of name "get_baz" to fetch data with
# the name "/foo/bar/baz"

app.register("get_baz", "/foo/bar/baz")
print(app.get_baz())

# @app.install
@app.install_sink("/foo/bar/car")
def get_car():
    # TODO: prepare the payload of the interest! (the protocol buffer content)
    return "cool stuff to go in the payload"

data = get_car()
print(data)

###
# sample consumer usage..
# ...
# define functions
# ..
# data = consumer.get_data()
