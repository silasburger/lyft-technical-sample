from app import app
from flask import jsonify
import unittest
from cut_string import cut_string

class ApplicationTest(unittest.TestCase):

    

    def setUp(self):
        """Set up our test client"""
        self.client = app.test_client()

    def test_response(self):
        """"""
        response = self.client.post('/test', json={
            "string_to_cut":"iamyourlyftdriver",
            })
        self.assertEqual(response.json["return_string"], "muydv")


    def test_error_response(self):
        """"""
        response = self.client.post('/cupcakes', json={
            "flavor":"shoe laces",
            "size":"smallish",
            "rating":7,
            "image":""
            })
        self.assertEqual(response.json["response"], "shoe laces")
        self.assertEqual(response.json["response"]["rating"], 7.0)


    def test_cut_string_function(self):
        """"""
        response = self.client.post('/cupcakes', json={ })
        self.assertEquals(response.json['response']['flavor'], 'werewer')


    def test_list(self):
        """List cupcakes"""
        response = self.client.get('/cupcakes')
        cupcakes = response.json['cupcakes']
        self.assertEqual(len(cupcakes),1)
        self.assertEqual(cupcakes[0]['flavor'],'testing')

