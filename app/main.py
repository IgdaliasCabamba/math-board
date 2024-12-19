from _system import *
from server import *

app.router.add_static('/static', STATIC_PATH)
app.router.add_get('/', index)

def run():
    import argparse

    parser=argparse.ArgumentParser(description="ImathLive - A powerful Math wihte board")
 
    parser.add_argument('-ip',
                        '--host',
                        help="Enter the host Bruh",
                        default="127.0.0.1",
                        type=str)
 
    parser.add_argument('-p',
                        '--port',
                        help="Enter the port XD",
                        default=9990,
                        type = int)
    
    args=parser.parse_args()

    sys.exit(run_new_board(args.host, args.port))
    

if __name__ == "__main__":
    run()