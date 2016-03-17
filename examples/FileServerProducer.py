import os

import protoccn
from protoccn.Hasher import *
from protoccn.Producer import *

app = CCNProducer("Producer", "ccnx:/producer")

@app.handle("/get")
def serve_file(fname, payload):
    with open(fname, "r") as fh:
        return fh.read()

@app.handle("/list")
def list_files(fname, payload):
    return str(os.listdir("."))

if __name__ == "__main__":
    app.run()
