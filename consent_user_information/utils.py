import logging

from django.contrib.auth import get_user_model

from ipware import get_client_ip

from .models import ConsentUserInformation

logger = logging.getLogger(__name__)


def create_user_consent_information(request, user=None, email=None):
    """To create an user consent information"""
    if not hasattr(request, "user_agent"):
        raise ValueError("UserAgentMiddleware from django_user_agents is mandatory")

    data = {
        "device": request.user_agent.device.family,
        "browser": request.user_agent.browser.family,
        "os": request.user_agent.os.family,
        "user_agent": request.user_agent,
    }

    if request.user_agent.browser.version_string:
        data["browser"] += " " + request.user_agent.browser.version_string

    if request.user_agent.os.version_string:
        data["os"] += " " + request.user_agent.os.version_string

    client_ip, is_routable = get_client_ip(request)

    if client_ip is None:
        logger.warning("Unable to get the ip")
    else:
        data["ip"] = client_ip

    if user:
        user = user
    elif email:
        user = get_user_model().objects.get(email=email)
    else:
        if request.user.is_authenticated:
            user = request.user

    ConsentUserInformation.objects.update_or_create(user=user, defaults=data)
