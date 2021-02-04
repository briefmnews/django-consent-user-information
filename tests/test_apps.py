import pytest

from consent_user_information.apps import ConsentUserInformationConfig

pytestmark = pytest.mark.django_db


class TestDjangoGarConfig:
    @staticmethod
    def test_apps():
        assert "consent_user_information" in ConsentUserInformationConfig.name
