import Portal

class Producer(object):
    def __init__(self, client, name, prefix = ""):
        self.client = client
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
            self.handlers[prefix] = f
            return f
        return decorator

    def run(self):
        # Create the portal
        self.client.listen(self.prefix)

        # Jump into the listening function
        while True:
            request = self.client.receive_raw() # this returns an interest!
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

class TestProducer(Producer):
    def __init__(self, name, prefix = ""):
        Producer.__init__(self, Portal.TestPortal(), name, prefix)

    def __str__(self):
        return self.__class__.__name__

class CCNProducer(Producer):
    def __init__(self, name, prefix = ""):
        Producer.__init__(self, Portal.CCNPortal(), name, prefix)

    def __str__(self):
        return self.__class__.__name__
