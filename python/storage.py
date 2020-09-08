"""
This script will show how to interract with blob storage
"""


import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def connectStorage():
    """
    This function return connection string from os.env. variables.

    You should set os.env. variable manually
    export AZURE_STORAGE_CONNECTION_STRING="<yourconnectionstring>"
    """
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    return connect_str


def listBlobs(containerName):
    """
    This function list all blob's inside of a container.
    """
    blob_list = container_client.list_blobs()
    result = []
    for blob in blob_list:
        result.append(blob.name)

    return result


def createContainer(containerName):
    """
    This function should create new container in your blob
    """
    pass


def uploadBlob(fileName, containerName):
    """
    This function should upload local file into blob

    You may choose whatever file you want
    """
    pass


def downloadBlob(fileName, containerName):
    """
    This function should download file from blob storage

    Which you already uploaded
    """
    pass


def deleteContainer(containerName):
    """
    This function should delete created container
    """
    pass


if __name__ == "__main__":
    # Here you shoud put your container name
    createContainer("tptContainer")
    print(listBlobs("tptContainer"))
    uploadBlob("filename.txt", "tptContainer")
    downloadBlob("filename.txt", "tptContainer")
    deleteContainer("tptContainer")
