from pyngrok import ngrok


def create_ngrok_tunnel(port: int) -> str:
    """
    Create an ngrok tunnel to the specified port.

    Args:
        port (int): The local port to tunnel.

    Returns:
        str: The public URL of the ngrok tunnel.
    """
    tunnel = ngrok.connect(port)
    return tunnel.public_url
