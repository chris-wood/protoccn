import protoccn
from protoccn.Consumer import *

app = CCNConsumer("Chris")

@app.install_sink("ccnx:/producer/get")
def fetch(fname):
    return fname

app.register("list", "ccnx:/producer/list/")

def main():
    while True:
        cmd = raw_input("> ")
        params = cmd.split(" ")
        if len(params) > 0:
            if params[0] == "list":
                print app.list()
            elif params[0] == "fetch":
                if len(params) > 1:
                    data = fetch(params[1])
                    print data
                else:
                    print "You must provide a file to fetch"
            else:
                print "Unknown command: only 'list' and 'fetch' are supported"

if __name__ == "__main__":
    main()
