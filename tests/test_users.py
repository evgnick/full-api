import allure

from config.base_test import BaseTest
import pytest


@allure.epic("Administration")
@allure.feature("Users")
class TestUser(BaseTest):

    @pytest.mark.regression
    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        print(self.api_users.get_user_by_id(user.uuid))


