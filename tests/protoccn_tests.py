from nose.tools import *
import protoccn

from protoccn.Hasher import *
from protoccn.Consumer import *
from protoccn.Producer import *

# def setup():
#     pass
#
# def teardown():
#     pass

def test_consumer_install():
    app = TestConsumer(__name__, "/my/name")

    test_payload = "cool payload"

    # @app.install
    @app.install_sink("/foo/bar/car")
    def get_car():
        return test_payload

    got = get_car()

    hasher = Hasher()
    hash_input = "/foo/bar/car" + test_payload
    expected = hasher.hash(hash_input)

    assert got == expected

def test_consumer_register():
    app = TestConsumer(__name__, "/my/name")

    # Register a method of name "get_baz" to fetch data with
    # the name "/foo/bar/baz"

    app.register("get_baz", "/foo/bar/baz")
    got = app.get_baz()

    hasher = Hasher()
    hash_input = "/foo/bar/baz"
    expected = hasher.hash(hash_input)

    print got
    print expected
    assert got == expected

def test_producer_handle():
    app = TestProducer(__name__, "/foo/bar")

    counter = 0
    print "here"

    @app.handle("/plus_one")
    def plus_one(baz):
        return counter + 1

    got = plus_one("test")
    assert got == (counter + 1)
