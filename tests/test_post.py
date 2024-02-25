import pytest
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    responceponse = authorized_client.get("/posts/")
    assert len(responceponse.json()) == len(test_posts)
    assert responceponse.status_code == 200

def test_anunthorized_user_get_all_posts(client):
    responceponse = client.get("/posts/")
    assert responceponse.status_code == 401
    assert responceponse.json() == {"detail": "Not authenticated"}

def test_anunthorized_user_get_one_post(client, test_posts):
    responceponse = client.get(f"/posts/{test_posts[0].id}")
    assert responceponse.status_code == 401
    assert responceponse.json() == {"detail": "Not authenticated"}

def test_get_one_post_not_exist(authorized_client, test_posts):
    responceponse = authorized_client.get(f"/posts/88888")
    assert responceponse.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    responceponse = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**responceponse.json())
    assert responceponse.status_code == 200
    assert post.Post.id == test_posts[0].id
    assert post.Post.title == test_posts[0].title
    assert post.Post.content == test_posts[0].content

@pytest.mark.parametrize("title, content, is_published", [
    ("awesome new title", "awesome new content", True),
    ("favorite pizza", "i love pepperoni", False),
    ("tallest skyscrapers", "wahoo", True),
])
def test_create_post(authorized_client, test_user, test_posts, title, content, is_published):
    responceponce = authorized_client.post(
        "/posts/", json={"title": title, "content": content, "is_published": is_published})

    created_post = schemas.Post(**responceponce.json())
    assert responceponce.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.is_published == is_published
    assert created_post.owner_id == test_user['id']

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    responce = authorized_client.post(
        "/posts/", json={"title": "arbitrary title", "content": "aasdfjasdf"})

    created_post = schemas.Post(**responce.json())
    assert responce.status_code == 201
    assert created_post.title == "arbitrary title"
    assert created_post.content == "aasdfjasdf"
    assert created_post.is_published == True
    assert created_post.owner_id == test_user['id']


def test_unauthorized_user_create_post(client, test_user, test_posts):
    responce = client.post(
        "/posts/", json={"title": "arbitrary title", "content": "aasdfjasdf"})
    assert responce.status_code == 401


def test_unauthorized_user_delete_Post(client, test_user, test_posts):
    responce = client.delete(
        f"/posts/{test_posts[0].id}")
    assert responce.status_code == 401


def test_delete_post_success(authorized_client, test_user, test_posts):
    responce = authorized_client.delete(
        f"/posts/{test_posts[0].id}")

    assert responce.status_code == 204


def test_delete_post_non_exist(authorized_client, test_user, test_posts):
    responce = authorized_client.delete(
        f"/posts/8000000")

    assert responce.status_code == 404


def test_delete_other_user_post(authorized_client, test_user, test_posts):
    responce = authorized_client.delete(
        f"/posts/{test_posts[3].id}")
    assert responce.status_code == 403


def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updatd content",
        "id": test_posts[0].id

    }
    responce = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.Post(**responce.json())
    assert responce.status_code == 200
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']


def test_update_other_user_post(authorized_client, test_user, test_user2, test_posts):
    data = {
        "title": "updated title",
        "content": "updatd content",
        "id": test_posts[3].id

    }
    responce = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert responce.status_code == 403


def test_unauthorized_user_update_post(client, test_user, test_posts):
    responce = client.put(
        f"/posts/{test_posts[0].id}")
    assert responce.status_code == 401


def test_update_post_non_exist(authorized_client, test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updatd content",
        "id": test_posts[3].id

    }
    responce = authorized_client.put(
        f"/posts/8000000", json=data)

    assert responce.status_code == 404












