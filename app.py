"""
Gemini Movie Recap Blogger Automation

Pipeline:

Movie title
    |
Gemini Flash
    |
Movie Recap JSON
    |
HTML Renderer
    |
Blogger API
    |
Draft / Publish

"""


import os
import json
import argparse
from datetime import datetime


from dotenv import load_dotenv


from ai.gemini import generate_movie_recap


from blogger.client import blogger


from blogger.posts import (
    create_post,
    publish
)


from content.renderer import render



load_dotenv()



OUTPUT_DIR="output/recaps"



os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)



# ---------------------------------
# Save generated article
# ---------------------------------


def save_backup(data):


    filename=datetime.now().strftime(
        "%Y%m%d_%H%M%S.json"
    )


    path=os.path.join(
        OUTPUT_DIR,
        filename
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(

            data,

            f,

            indent=4,

            ensure_ascii=False

        )


    return path




# ---------------------------------
# Generate article
# ---------------------------------


def generate(
        movie,
        year=None,
        context=None
):


    print(
        "\n🎬 Generating movie recap..."
    )


    article=generate_movie_recap(

        movie_title=movie,

        movie_year=year,

        extra_context=context

    )


    print(
        "✓ Gemini generation completed"
    )


    return article





# ---------------------------------
# Blogger publishing
# ---------------------------------


def publish_blog(

        article,

        draft=True

):


    print(
        "\n📝 Preparing Blogger HTML..."
    )


    html=render(

        article,
        image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuAaFoBHE4wG7f_lCVqR_P7U1gVxVySQmSrSY_YtF7BA&s=10"
    )


    service=blogger()



    print(
        "Uploading to Blogger..."
    )



    post=create_post(

        service,


        article["title"],


        html,


        labels=
        article.get(
            "labels",
            [
                "Movie Recap"
            ]
        ),


        draft=draft

    )



    print(
        "\n✓ Blogger created"
    )


    print(
        "URL:",
        post.get("url")
    )



    return post





# ---------------------------------
# Main pipeline
# ---------------------------------


def run(args):


    article=generate(

        args.movie,

        args.year,

        args.context

    )



    backup=save_backup(
        article
    )


    print(
        "Backup:",
        backup
    )



    if args.no_publish:


        print(
            "\nPreview mode only"
        )

        return



    post=publish_blog(

        article,


        draft=
        not args.publish

    )



    if args.publish:


        print(
            "\nPublishing..."
        )


        publish(

            blogger(),

            post["id"]

        )


        print(
            "✓ Published"
        )





# ---------------------------------
# CLI
# ---------------------------------


if __name__=="__main__":



    parser=argparse.ArgumentParser(

        description=
        "Gemini Movie Recap Blogger AI"

    )



    parser.add_argument(

        "movie",

        help=
        "Movie title"

    )


    parser.add_argument(

        "--year",

        help=
        "Movie release year"

    )


    parser.add_argument(

        "--context",

        help=
        "Extra instructions"

    )


    parser.add_argument(

        "--publish",

        action="store_true",

        help=
        "Publish immediately"

    )


    parser.add_argument(

        "--no-publish",

        action="store_true",

        help=
        "Only generate content"

    )



    args=parser.parse_args()



    run(args)
