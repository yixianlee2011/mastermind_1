
from webtest import TestApp
import main

def test_functional():
    app = TestApp(main.bottle)
    assert app.get('/api/verify_service_m').status == '200 OK'