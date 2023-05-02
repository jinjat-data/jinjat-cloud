import modal
from modal import Image, Stub, asgi_app

image = Image.debian_slim().pip_install("boto3")
stub = Stub(mounts=[modal.Mount.from_local_dir("/user/john/.aws", remote_path="/root/")])


@stub.function(image=image)
@asgi_app(label="jinjat")
def fastapi_app():
    return web_app
