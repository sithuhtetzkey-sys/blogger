from .seo import generate_schema



def add_image(
        image_url,
        alt_text="Featured image"
):

    if not image_url:
        return ""


    return f"""

<figure>

<img 
src="{image_url}"
alt="{alt_text}"
style="
width:100%;
height:auto;
border-radius:12px;
"
/>

</figure>

"""



def render(
        article,
        image_url=None
):


    title = article.get(
        "title",
        "Movie Recap"
    )


    # Image block
    image_html = add_image(

        image_url,

        title

    )


    content = ""


    # Movie recap schema

    if "recap_structure" in article:


        recap = article.get(
            "recap_structure",
            {}
        )


        intro = recap.get(
            "introduction",
            {}
        )


        content += f"""

<h2>
Introduction
</h2>

<p>
{intro}
</p>

"""


        for section in [
            "act_1_setup",
            "act_2_conflict",
            "act_3_climax"
        ]:


            items = recap.get(
                section,
                []
            )


            content += f"""

<h2>
{section.replace("_"," ").title()}
</h2>

"""


            if isinstance(items, list):

                for item in items:

                    content += f"""

<div>

<p>
{item}
</p>

</div>

"""

            else:

                content += str(items)



    else:

        content = article.get(
            "content_html",
            article.get(
                "content",
                ""
            )
        )



    html=f"""

{generate_schema(article)}


<article>


<h1>
{title}
</h1>


{image_html}


<div class="movie-recap">

{content}

</div>


</article>

"""


    return html