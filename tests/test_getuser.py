from utils.api_client import APIClient
import pytest
import uuid


@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_getusers_validation(api_client):
    response = api_client.get("public/v2/users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_users(api_client, load_user_data):
    '''
    user_data = {
        "name": "Andriy Pollppiii",
        "email": "khatri_ppii@west.test",
        "gender": "male",
        "status": "active"
    }
    '''
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    user_data["email"] = unique_email
    response = api_client.post("public/v2/users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == "Andriy Pollppiii"
    created_user_id = response.json()['id']
    print(created_user_id)
    responseget = api_client.get(f"public/v2/users/{created_user_id}")
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()['name'] == 'Andriy Pollppiii'


def test_update_users(api_client):
    user_data = {
        "name": "Andriy Poll",
        "email": "khatri_ppuuu@west.test",
        "gender": "male",
        "status": "active"
    }
    response = api_client.put("public/v2/users/7484380", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'Andriy Poll'

def test_delete_users(api_client):
    response = api_client.delete("public/v2/users/7484380")
    assert response.status_code == 404