from ai.api.model_client.grpc_client import GrpcClient
from ai.api.model_client.http_client import HttpClient
from ai.api.model_client.mock_client import MockClient
from django.apps.config import AppConfig
from django.test import override_settings
from rest_framework.test import APITestCase


class TestAiApp(APITestCase):
    @override_settings(ANSIBLE_AI_MODEL_MESH_API_TYPE='grpc')
    def test_grpc_client(self):
        app_config = AppConfig.create('ai')
        app_config.ready()
        self.assertIsInstance(app_config.model_mesh_client, GrpcClient)

    @override_settings(ANSIBLE_AI_MODEL_MESH_API_TYPE='http')
    def test_http_client(self):
        app_config = AppConfig.create('ai')
        app_config.ready()
        self.assertIsInstance(app_config.model_mesh_client, HttpClient)

    @override_settings(ANSIBLE_AI_MODEL_MESH_API_TYPE='mock')
    def test_mock_client(self):
        app_config = AppConfig.create('ai')
        app_config.ready()
        self.assertIsInstance(app_config.model_mesh_client, MockClient)

    @override_settings(ENABLE_ARI_POSTPROCESS=True)
    def test_enable_ari(self):
        app_config = AppConfig.create('ai')
        app_config.ready()
        self.assertIsNotNone(app_config.get_ari_caller())

    @override_settings(ENABLE_ARI_POSTPROCESS=False)
    def test_disable_ari(self):
        app_config = AppConfig.create('ai')
        app_config.ready()
        self.assertIsNone(app_config.get_ari_caller())