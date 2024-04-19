import allure
import json
from allure_commons.types import AttachmentType


class Helper:

    # берет json и прикрепляет к аллюр отчету
    def attach_response(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)
