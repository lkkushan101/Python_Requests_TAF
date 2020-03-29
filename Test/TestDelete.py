from  ReusableRequest import DeleteRequest
from Utility.ReadExcel import readExcel
import unittest

class Get_Test(unittest.TestCase):
    get_req = DeleteRequest
    response = get_req.send_delete_request(readExcel('../Data/data.xlsx','Sheet1','B4'))
    assert response.status_code == 204