from py_localtunnel.lt import run_localtunnel


def create_localtunnel(port: int) -> str:
    """
    Create a localtunnel to the specified port.

    Args:
        port (int): The local port to tunnel.

    Returns:
        str: The public URL of the localtunnel.
    """
    lt_tunnel = run_localtunnel(port)
    return lt_tunnel
