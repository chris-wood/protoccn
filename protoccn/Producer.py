class Producer(object):
    def __init__(self, name, prefix = ""):
        self.name = name
        self.prefix = prefix
        self.handlers = {}

    # TODO: make prefix a regex for names
    # TODO: if the producer has a prefix, then don't use the prefix here
    def prefix(self, prefix, **options):
        """A decorator that is used to register a view function for a
        given URL rule.  This does the same thing as :meth:`add_url_rule`
        but is intended for decorator usage::
            @app.route('/')
            def index():
                return 'Hello World'
        For more information refer to :ref:`url-route-registrations`.
        :param rule: the URL rule as string
        :param endpoint: the endpoint for the registered URL rule.  Flask
                         itself assumes the name of the view function as
                         endpoint
        :param options: the options to be forwarded to the underlying
                        :class:`~werkzeug.routing.Rule` object.  A change
                        to Werkzeug is handling of method options.  methods
                        is a list of methods this rule should be limited
                        to (``GET``, ``POST`` etc.).  By default a rule
                        just listens for ``GET`` (and implicitly ``HEAD``).
                        Starting with Flask 0.6, ``OPTIONS`` is implicitly
                        added and handled by the standard request handling.
        """
        def decorator(f):
            #endpoint = options.pop('endpoint', None)
            #self.add_url_rule(rule, endpoint, f, **options)
            print "setup a function: %s" % (f.__name__)
            self.handlers[prefix] = f
            return f
        return decorator

    def hello(self, message):
        print "hello!"
        pass

    def run(self):
        # 1. create the portal(s)
        # 2. jump into the listening function
        pass

    def __str__(self):
        # TODO: return a generic
        return ""

app = Producer(__name__)

@app.prefix("/")
def base(message):
    print message

base("test")   

