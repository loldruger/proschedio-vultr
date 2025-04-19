# filepath: /home/ubuntu/project/proschedio-vultr/src/proschedio_vultr/handlers/__init__.py
# Export handlers for use by the plugin
from ._base_handler import ResourceHandlerInterface
from .instance_handler import ServerInstanceHandler

__all__ = [
    "ResourceHandlerInterface",
    "ServerInstanceHandler",
]
