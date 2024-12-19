import aiohttp_jinja2
import jinja2
import src.mrequirements as mrequirements
from _system import *
from aiohttp import web

mrequirements.main()

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATES_PATH))


@aiohttp_jinja2.template('index.html')
async def index(request) -> dict:
    """Serve the client-side application."""

    return {}


def run_new_board(host: str = "127.0.0.1", port: int = 9990) -> None:
    web.run_app(app, port=port, host=host)