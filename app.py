from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

import os

connection_string = "DefaultEndpointsProtocol=https;AccountName=regustorageaccount;AccountKey=c42SwkgCVxablacqjxaNLO4x4Hy+fI9xxWHd9Q9669E/wFFoYsVPuOpINdZZlRSETwejrqLphOjT+AStAQTtaA==;Endpo>


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/")
def list_blobs_in_container():

    # Instantiate a BlobServiceClient using a connection string
    from azure.storage.blob import BlobServiceClient

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Instantiate a ContainerClient
    container_client = blob_service_client.get_container_client("testcontainer")

    blobs_list = container_client.list_blobs()

    l = []
    for blob in blobs_list:
        l.append(blob.name)
    return l


app.debug = True

app.run()
