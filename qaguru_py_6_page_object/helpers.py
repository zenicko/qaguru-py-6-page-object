import os

from selene.core.entity import Element
from selene.core.wait import Command


def resource(file_name: str):
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        os.path.join('resources', file_name))


def upload_resource(path: str) -> Command[Element]:
    def fn(element: Element):
        element.send_keys(resource(path))

    return Command(f'set value by js: {path}', fn)
