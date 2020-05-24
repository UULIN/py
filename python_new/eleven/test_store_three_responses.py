import unittest
from python_new.eleven import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """测试多个survey"""

    def setUp(self):
        """创建一个调查对象和一组答案，供测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['CH', 'EN', 'JP']

    def test_store_single_response(self):
        """测试单个答案被妥善的存储"""
        self.my_survey.store_response(self.respinses[0])
        self.assertIn(self.respinses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善的保管"""

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)