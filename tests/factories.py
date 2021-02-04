import factory

from django.contrib.auth import get_user_model

from consent_user_information.models import ConsentUserInformation


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: "noel{0}@flantier.com".format(n))


class ConsentUserInformationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ConsentUserInformation

    user = factory.SubFactory(UserFactory)
    ip = "127.0.0.1"
    device = "PC"
    os = "Linux"
    user_agent = "Hello"
