import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from app import create_app


def test_home_route():
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    print("✅ Home route works")


def test_calculate_route():
    app = create_app()
    client = app.test_client()
    response = client.post('/calculate',
        json={
            'typed_text': 'hello world',
            'sample_text': 'hello world',
            'time_seconds': 10
        }
    )
    assert response.status_code == 200
    data = response.get_json()
    assert 'wpm' in data
    assert 'accuracy' in data
    assert 'errors' in data
    assert 'level' in data
    print(f"✅ Calculate route works: {data}")


def test_history_route():
    app = create_app()
    client = app.test_client()
    response = client.get('/history')
    assert response.status_code == 200
    print("✅ History route works")


if __name__ == '__main__':
    test_home_route()
    test_calculate_route()
    test_history_route()
    print("\n✅ All route tests passed!")