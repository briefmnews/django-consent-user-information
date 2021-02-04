import pytest

from consent_user_information.models import ConsentUserInformation
from consent_user_information.utils import create_user_consent_information

pytestmark = pytest.mark.django_db


class TestCreateUserConsentInformation:
    def test_without_user_or_mail(self, request_builder):
        # GIVEN
        request = request_builder.get()
        assert ConsentUserInformation.objects.count() == 0

        # WHEN
        create_user_consent_information(request)

        # THEN
        assert ConsentUserInformation.objects.count() == 1

    def test_with_user_in_request(self, request_builder, user):
        # GIVEN
        request = request_builder.get(user=user)
        assert ConsentUserInformation.objects.count() == 0

        # WHEN
        create_user_consent_information(request)

        # THEN
        assert ConsentUserInformation.objects.count() == 1

    def test_with_user_in_arg(self, request_builder, user):
        # GIVEN
        request = request_builder.get()
        assert ConsentUserInformation.objects.count() == 0

        # WHEN
        create_user_consent_information(request, user)

        # THEN
        assert ConsentUserInformation.objects.count() == 1

    def test_with_mail(self, request_builder, user):
        # GIVEN
        request = request_builder.get()
        assert ConsentUserInformation.objects.count() == 0

        # WHEN
        create_user_consent_information(request, mail=user.email)

        # THEN
        assert ConsentUserInformation.objects.count() == 1
