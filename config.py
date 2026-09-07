import os
from dotenv import load_dotenv

import truststore
truststore.inject_into_ssl()
load_dotenv()


BLOG_ID=os.getenv(
    "BLOG_ID"
)

SCOPES=[
    "https://www.googleapis.com/auth/blogger"
]
