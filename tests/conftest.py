import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django_user_agents.middleware import UserAgentMiddleware

from .factories import ConsentUserInformationFactory, UserFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def user_information():
    return ConsentUserInformationFactory()


@pytest.fixture
def request_builder():
    """Create a request object"""
    return RequestBuilder()


class RequestBuilder(object):
    @staticmethod
    def get(path="/", user=None):
        rf = RequestFactory()
        request = rf.get(path)
        request.user = user or AnonymousUser()

        SessionMiddleware().process_request(request)
        UserAgentMiddleware().process_request(request)

        request.session.save()

        return request
