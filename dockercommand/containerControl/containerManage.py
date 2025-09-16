import docker



class BaseDocker:
    """Base class for Docker-related functionality."""
    def __init__(self):
        self.docker_client = docker.from_env()




print("1. image list")
print("2. container list")

selection = input("Enter your choice (1 or 2): ")

if selection == '1':
    images = BaseDocker().docker_client.images.list()
    for image in images:
        print(f"Image ID: {image.id}, Tags: {image.tags[0]}, Image Name: {image.attrs.get('RepoTags')[0]}")
elif selection == '2':
    containers = BaseDocker().docker_client.containers.list(all=True)
    for container in containers:
        print(f"Container ID: {container.id}, Name: {container.name}, Status: {container.status}")