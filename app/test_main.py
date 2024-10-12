import pytest
import datetime
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "test_year,test_month,test_day,expected_answer",
    [
        pytest.param(2022, 2, 2, ["duck"],
                     id="The product expired 02.02.2022 is \'duck\'"),
        pytest.param(2024, 10, 12, ["chicken", "duck", "salmon"],
                     id="The products expired 06.02.2022 are "
                        "\'duck\' and \'chicken\'")
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime: mock.MagicMock,
                           test_year: int,
                           test_month: int,
                           test_day: int,
                           expected_answer: list) -> None:
    mocked_datetime.date.today.return_value = (
        datetime.date(test_year, test_month, test_day))
    mocked_datetime.date.side_effect = datetime.date
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    assert (dict.fromkeys(expected_answer)
            == dict.fromkeys(outdated_products(products)))
