from kubernetes import client, config
import uuid

# Kubernetes Konfiguration laden
config.load_incluster_config()

def create_worker_pod():

    pod_name = f"worker-{uuid.uuid4().hex[:6]}"

    api = client.CoreV1Api()

    pod = client.V1Pod(
        metadata=client.V1ObjectMeta(
            name=pod_name,
            labels={
                "app": "worker"
            }
        ),
        spec=client.V1PodSpec(
            restart_policy="Never",
            containers=[
                client.V1Container(
                    name="worker",
                    image="python:3.12-slim",
                    command=[
                        "python",
                        "-c",
                        """
import time
print('Worker gestartet')
time.sleep(60)
print('Worker beendet')
"""
                    ]
                )
            ]
        )
    )

    api.create_namespaced_pod(
        namespace="workers",
        body=pod
    )

    return pod_name