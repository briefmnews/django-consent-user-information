import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import models

logger = logging.getLogger(__name__)


class ConsentUserInformationManager(models.Manager):
    def get_ip_address(self, user):
        try:
            return self.get(user=user).ip
        except (ObjectDoesNotExist, AttributeError):
            logger.info(f"User {user.pk} doesn't have a user consent record")
            return ""

    def get_user_agent(self, user):
        try:
            return self.get(user=user).user_agent
        except (ObjectDoesNotExist, AttributeError):
            logger.info(f"User {user.pk} doesn't have a user consent record")
            return ""
