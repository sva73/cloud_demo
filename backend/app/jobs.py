from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException
import uuid


def load_k8s():
    try:
        config.load_incluster_config()
        print("Loaded in-cluster config")

    except ConfigException:
        try:
            config.load_kube_config()
            print("Loaded kubeconfig")

        except ConfigException:
            print("No Kubernetes config available")


def create_worker_job():

    # Kubernetes erst hier laden
    load_k8s()

    job_name = f"worker-job-{uuid.uuid4().hex[:6]}"

    batch_api = client.BatchV1Api()

    job = client.V1Job(
        metadata=client.V1ObjectMeta(
            name=job_name
        ),
        spec=client.V1JobSpec(
            template=client.V1PodTemplateSpec(
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

print("Job gestartet")

for i in range(5):
    print(f"Arbeite Schritt {i}")
    time.sleep(2)

print("Job beendet")
"""
                            ]
                        )
                    ]
                )
            )
        )
    )

    batch_api.create_namespaced_job(
        namespace="workers",
        body=job
    )

    return job_name