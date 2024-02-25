import pytest
from jose import jwt
from app import schemas
from app.config import settings

# def test_root(client):
#     response = client.get("/")
#     print(response.json())
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello World!"}

def test_create_user(client):
    response = client.post("/users/", 
                           json={"email": "test_user@gmail.com", "password": "test_password123"})
    
    new_user = schemas.UserOut(**response.json())
    assert response.status_code == 201
    assert new_user.email == "test_user@gmail.com"

def test_login_user(client, test_user):
    response = client.post("/login", 
                           data={"username": test_user["email"], "password": test_user["password"]})
    login_responce = schemas.Token(**response.json())
    payload = jwt.decode(login_responce.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert response.status_code == 200
    
@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'test_password123', 403),
    ('test_user@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'test_password123', 422),
    ('test_user@gmail.com', None, 422)
])
def test_incorrect_login_user(client, email, password, status_code):
    response = client.post("/login", 
                           data={"username": email, "password": password})
    print(response.json())
    assert response.status_code == status_code
    # assert response.json() == {"detail": "Invalid Credentials"}
