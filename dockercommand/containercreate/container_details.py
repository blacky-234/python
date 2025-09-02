import docker


class BaseDocker:
    """Base class for Docker-related functionality."""
    def __init__(self):
        self.client = docker.from_env()


class DockerContainer(BaseDocker):
    """Represents a single Docker container."""
    def __init__(self, container_id):
        super().__init__()
        self.container_id = container_id
        self.container = self._get_container()
        self.details = self._get_details()

    def _get_container(self):
        try:
            return self.client.containers.get(self.container_id)
        except docker.errors.NotFound:
            return None

    def _get_details(self):
        if not self.container:
            return {"error": "Container not found"}
        try:
            return {
                "id": self.container.id,
                "name": self.container.name,
                "status": self.container.status,
                "image": self.container.image.tags,
                "created": self.container.attrs.get('Created'),
                "ports": self.container.ports,
                "container_ip": self.container.attrs['NetworkSettings']['IPAddress'],
            }
        except Exception as e:
            return {"error": str(e)}

    def get_details(self):
        return self.details


class DockerManager(BaseDocker):
    """Manages multiple Docker containers."""
    def __init__(self):
        super().__init__()

    def list_all_containers(self):
        return [DockerContainer(container.id) for container in self.client.containers.list(all=True)]

    def list_running_containers(self):
        return [DockerContainer(container.id) for container in self.client.containers.list()]


def main():
    manager = DockerManager()
    containers = manager.list_all_containers()

    for container in containers:
        print(container.get_details(), end="\n\n")
        print("==========================Next Container===========================")


if __name__ == "__main__":
    main()
