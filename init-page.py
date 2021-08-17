# initializes a manual page
import pathlib
import os
def run_manual(manual: str, db: bool):
    try:
        if db == True:
            print("checking for man...")
        if pathlib.Path("/usr/bin/man").exists():
            if db == True:
                print("CWD=" + os.getcwd())
            os.system("/usr/bin/man " + manual)
    except KeyboardInterrupt:
        print("cancelling manpage operation.")


run_manual("./man/hello.1", False) # set to true for DEBUG logs