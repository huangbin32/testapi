#coding=utf-8
import json
from public import mytest
from ddt import ddt, data, unpack
from loguru import logger
from public.send_request import SendRequest
from public.data_info import get_test_case_data, data_info, write_res
# import json

@ddt
class Other(mytest.MyTokenTest):
    """其他需要验证token的接口"""

    @data(*get_test_case_data(data_info, 'other'))
    def test_api(self, data):
        logger.info(data)
        method = data['method']
        url = self.url + data['url']
        logger.info(url)
        send_data = data['send_data']
        assert_info = data['assert_info']
        rownum = data['rownum']
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url,header=self.headers)
        logger.info(r)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])