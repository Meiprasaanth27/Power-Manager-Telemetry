import docker

def run_stress_container(utilization=100, duration=60):
    client = docker.from_env()
    container = client.containers.run(
        'alpine',
        f'sh -c "apk add --no-cache stress && stress --cpu 1 --timeout {duration} --cpu-load {utilization}"',
        detach=True
    )
    return container
