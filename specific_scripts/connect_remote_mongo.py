from sshtunnel import SSHTunnelForwarder
import pymongo

MONGO_HOST = "REMOTE HOST IP"
MONGO_DB = "MONGO DB NAME"
MONGO_USER = "USERNAME"
MONGO_PASS = "PASSWORD"

server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=('127.0.0.1', 27017)
)
server.start() # start the ssh tunnel
client = pymongo.MongoClient('127.0.0.1', server.local_bind_port) # server.local_bind_port is assigned local port
db = client[MONGO_DB]
#############################
# Any mongo queries required can be used here
# As per requirement.
#############################
server.stop() # stop the ssh tunnel