"""Test case that reponse to incorrect https request"""
def test_index_ok(client):
    """Making GET request to / and stored the response
    assert the status to 200 if the resquest is ok"""
    response = client.get('/')
    assert response.status_code == 200
