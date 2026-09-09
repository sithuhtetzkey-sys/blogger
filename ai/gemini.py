import os
import json
import time

from dotenv import load_dotenv

from google import genai
from google.genai import types


from ai.schema import MOVIE_RECAP_SCHEMA


load_dotenv()


client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)



MODEL = "gemini-3.6-flash"



def generate_movie_recap(
        movie_title,
        movie_year=None,
        extra_context=None
):


    prompt = f"""

You are an Myanmar expert movie recap writer .

Create a high-retention cinematic movie recap in Burmese Language.

Movie:

Title:
{movie_title}

Year:
{movie_year}


Writing style:

- Similar structure to successful YouTube movie recap channels
- Storytelling, not Wikipedia summary
- Strong curiosity hook
- Explain character motivations
- Highlight important turning points
- Explain ending clearly
- Add original analysis
- Keep narration engaging


Important:

The output will be converted into:

1. Blogger article
2. YouTube narration script
3. SEO content


Avoid:

- Copying dialogue
- Long direct quotes
- Scene-by-scene transcript
- Copyrighted screenplay text


Additional information:

{extra_context or "None"}

"""


    for attempt in range(3):

        try:

            response = client.models.generate_content(

                model=MODEL,

                contents=prompt,


                config=types.GenerateContentConfig(

                    temperature=0.8,


                    response_mime_type=
                    "application/json",


                    response_schema=
                    MOVIE_RECAP_SCHEMA

                )

            )


            data=json.loads(
                response.text
            )


            return data



        except Exception as e:


            print(
                f"Gemini error {attempt+1}/3:",
                e
            )


            time.sleep(3)



    raise RuntimeError(
        "Failed generating movie recap"
    )

