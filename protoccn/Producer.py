# import PortalWrapper

class Producer(object):
    def __init__(self, name, prefix = ""):
        self.name = name
        self.prefix = prefix
        self.handlers = {}

    # TODO: make prefix a regex for names
    def handle(self, prefix, **options):
        """ TODO

        :param prefix: TODO
        :param options: TODO
        """
        def decorator(f):
            print "setup a function: %s" % (f.__name__)
            self.handlers[prefix] = f
            return f
        return decorator

    def hello(self, message):
        print "hello!"
        pass

    def run(self):
        # Create the portal
        self.client = PortalWrapper.PortalWrapper()
        self.client.listen(self.prefix)

        # Jump into the listening function
        while True:
            request = self.client.receive_raw()
            name = request.name

            # Perform LPM with the handler function and invoke the right request
            target = ""
            for prefix in self.handlers:
                if name.startsWith(prefix) and len(prefix) > target:
                    target = prefix

            # Pass the request to the right method
            response = self.handlers[target](request)

            # Return the response
            self.client.reply(request.name, response)
        pass

    def __str__(self):
        # TODO: return a generic
        return ""

app = Producer(__name__, "/foo/bar")

@app.handle("/baz")
def baz(baz):
    print baz
    pass

# @app.prefix("/car")
# def car(car):
#     print "car!"
#     return car

baz("test") # during the run function, these functions would be invoked based on the name.

# blast off
# app.run()
