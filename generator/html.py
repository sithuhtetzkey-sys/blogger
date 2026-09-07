from config import BLOG_ID



def list_posts(service):

    result=service.posts().list(
        blogId=BLOG_ID
    ).execute()


    return result.get(
        "items",
        []
    )




def create_post(
        service,
        title,
        html,
        labels=[],
        draft=True
):


    body={

        "title":title,

        "content":html,

        "labels":labels

    }


    return service.posts().insert(

        blogId=BLOG_ID,

        body=body,

        isDraft=draft

    ).execute()




def update_post(
        service,
        post_id,
        title,
        html
):


    return service.posts().update(

        blogId=BLOG_ID,

        postId=post_id,

        body={

            "title":title,

            "content":html

        }

    ).execute()




def publish(
        service,
        post_id
):

    return service.posts().publish(

        blogId=BLOG_ID,

        postId=post_id

    ).execute()



def delete_post(
        service,
        post_id
):

    return service.posts().delete(

        blogId=BLOG_ID,

        postId=post_id

    ).execute()
