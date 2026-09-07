import markdown


def convert(md):

    return markdown.markdown(
        md,
        extensions=[
            "extra",
            "codehilite",
            "tables"
        ]
    )
