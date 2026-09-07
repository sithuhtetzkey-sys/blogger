from googleapiclient.discovery import build

import truststore
truststore.inject_into_ssl()
from .auth import authenticate


def blogger():

    return build(
        "blogger",
        "v3",
        credentials=authenticate()
    )
