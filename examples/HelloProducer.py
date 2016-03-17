import subprocess

import protoccn
from protoccn.Producer import *

app = CCNProducer("Producer", "ccnx:/producer")

@app.handle("/command")
def execute_command(suffix, cmd):
    out = subprocess.check_output([cmd])
    print "Ran %s: %s" % (cmd, out)
    return out

if __name__ == "__main__":
    app.run()
