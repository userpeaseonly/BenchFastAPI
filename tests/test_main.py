from fastapi.testclient import TestClient
from io import BytesIO
from main import app

client = TestClient(app)

def test_upload_file():
    file_content = b"This is a test file content."
    file_name = "test_file.txt"
    in_memory_file = BytesIO(file_content)

    response = client.post(
        "/upload/",
        files={"file": (file_name, in_memory_file, "text/plain")},
    )

    assert response.status_code == 200
    assert response.json() == {"filename": file_name}