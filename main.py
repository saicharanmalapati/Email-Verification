import os
import logging
import sys
from socket import *

# port defines the port used by the api server
port = os.getenv("PORT", "8080")
