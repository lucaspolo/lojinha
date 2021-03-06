import pytest
from django.urls import reverse

from lojinha.django_assertions import dj_assert_contains


def test_status_code(client):
    response = client.get(reverse('root'))
    assert 200 == response.status_code


@pytest.mark.parametrize("content", [
    "Lojinha em construção",
    "2018",
    "pradopolo@gmail.com",
    "nav"
])
def test_home(client, content):
    response = client.get(reverse('root'))
    dj_assert_contains(response, content)
