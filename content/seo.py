import json
import html


def safe_get(data, key, default=""):

    return data.get(
        key,
        default
    )



def generate_schema(article):


    movie = article.get(
        "movie",
        {}
    )


    title = safe_get(
        article,
        "title",
        movie.get(
            "title",
            "Movie Recap"
        )
    )


    summary = safe_get(
        article,
        "summary"
    )


    if not summary:

        summary = safe_get(
            article.get(
                "blog_output",
                {}
            ),
            "summary",
            "Movie recap and ending explanation."
        )


    schema = {

        "@context":
        "https://schema.org",


        "@type":
        "Article",


        "headline":
        title,


        "description":
        summary,


        "about":

        {

            "@type":
            "Movie",

            "name":
            movie.get(
                "title",
                title
            )

        }

    }


    return f"""
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
</script>
"""