import protoccn
from protoccn.Consumer import *

app = CCNConsumer("Chris")

@app.install_rpc("lci:/producer/command")
def execute_command(command):
    return command

def main():
    print execute_command("date")

if __name__ == "__main__":
    main()
