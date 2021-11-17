import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from server.assets.schemas import user

@pytest.mark.usefixtures('global_settings')
class TestAPI:
    settings: dict
    client: TestClient
    url: str
    
    @classmethod
    def setup(cls):
        cls.settings = cls.settings
        cls.client = cls.settings.get('client')
    
    def setup_method(self, method):
        method_name = method.__name__.split('_')[-1]
        self.url = f'/api/{method_name}'
    
    def test_create_users(self):
        data = user.CreateUser(
            user_id="test_id",
            password="jlaksjdfoi1234kxzlv",
            nickname="test_test",
            name="test name",
            email="test@gamil.com",
            phone="010-215-2182"
        )
        res = self.client.post(
            self.url,
            json=data.dict()
        )
        assert res.status_code == 200
        
    def test_get_users(self):
        res = self.client.get(
            self.url,
            params=dict(id=1)
        )
        
        assert res.status_code == 200
    
    def test_update_users(self):
        data = user.UpdateUser(
            user_id="updated_test_id",
            password="lkjywe12xbv",
            nickname="update_test",
            name="update test name",
            email="update_test@gamil.com",
            phone="010-2345-8554"
        )
        res = self.client.put(
            self.url,
            params=dict(id=2),
            json=data.dict()
        )

    def test_delete_users(self):
        res = self.client.delete(
            self.url,
            params=dict(id=1)
        )
        assert res.status_code == 200