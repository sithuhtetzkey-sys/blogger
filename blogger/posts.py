from googleapiclient.discovery import build

from .auth import authenticate


def blogger():

    return build(
        "blogger",
        "v3",
        credentials=authenticate()
    )
