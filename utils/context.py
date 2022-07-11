import os

# This file contains global variables
context ={
    "videos":dict(),
    "audio":dict(),
    "clips":dict(),
    "concat":list()
}

CLEAR = "cls" if "nt" in os.name else "clear"