from typing import Literal

from .localtunnel import create_localtunnel
from .ngrok_tunnel import create_ngrok_tunnel

TunnelType = Literal["ngrok", "localtunnel"]


def create_tunnel(tunnel_type: TunnelType, port: int) -> str:
    """
    Create a tunnel using the specified tunneling service.

    Args:
        tunnel_type (TunnelType): The type of tunnel to create.
        port (int): The local port to tunnel.

    Returns:
        str: The public URL of the tunnel.

    Raises:
        ValueError: If an invalid tunnel type is specified.
    """
    if tunnel_type == "ngrok":
        return create_ngrok_tunnel(port)
    elif tunnel_type == "localtunnel":
        return create_localtunnel(port)
    else:
        raise ValueError(f"Invalid tunnel type: {tunnel_type}")
