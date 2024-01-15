import json
from django.http import HttpRequest
from django.http.response import JsonResponse
import logging

logger = logging.getLogger(__name__)



class Response():
    def __init__(self, request, testMode=False):
        request = {}
        self.request = request
        self.attachPager = False
        self.data = {}
        self.test_mode = testMode
        self.pager = request
        self.pager_dict = {
        }

    def set_pager(self, sort_field="id", total_records=0, filtered_records=10,records_per_page=10,sort_order="DESC"):
        self.attachPager = True
        self.pager_dict.update({
            "sortBy": sort_field,
            "totalRecords": total_records,
            "recordsPerPage": records_per_page,
            "sortOrder": sort_order
        })

    def createResponse(self, message, payload, status_code=200):
        self.data["status"] = status_code
        self.data["message"] = message
        self.data["payload"] = payload if status_code == 200 else {}
        self.data["pager"] = self.pager_dict if self.attachPager else {}

        if int(status_code) != 200:
            logger.error(f"HTTP Response:{status_code}: Request Error | {message}")
        else:
            logger.info(f"HTTP Response:{status_code}: {message}")
        
        response = JsonResponse(self.data, safe=False, status=status_code)
        return response