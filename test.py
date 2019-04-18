from app import app
from flask import jsonify
import unittest
from cut_string import cut_string

class ApplicationTest(unittest.TestCase):

    

    def setUp(self):
        """Set up our test client"""
        self.client = app.test_client()

    def test_cut_string(self):
        """Unit test the cut_string function"""
        self.assertEqual(cut_string('uiaytbjkc'), 'abc')
        self.assertEqual(cut_string('qw'), '')
        self.assertEqual(cut_string('wecvs'), "c")


    def test_response(self):
        """Integration test of the /test route"""
        response_odd = self.client.post('/test', json={
            "string_to_cut":"iamyourlyftdriver",
            })
        response_even = self.client.post('/test', json={
            "string_to_cut":"zxawub",
            })
        response_empty = self.client.post('/test', json={
            "string_to_cut":"",
            })
        self.assertEqual(response_odd.json["return_string"], "muydv")
        self.assertEqual(response_even.json["return_string"], "ab")
        self.assertEqual(response_empty.json["return_string"], "")


    def test_error_response(self):
        """Test that errors are being handled correctly"""
        response_wrong_key = self.client.post('/test', json={
            "string_to_cu":"iamyourlyftdriver",
            })
        response_not_string = self.client.post('/test', json={
            "string_to_cut":2,
            })
        self.assertEqual(response_wrong_key.json["message"], "\"string_to_cut\" key not provided in body of request")
        self.assertEqual(response_not_string.json["message"], "The value you provided is not a string")

