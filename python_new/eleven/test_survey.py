import unittest
from python_new.eleven import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """测试survey"""
    def test_store_single_response(self):
        """测试单个答案被妥善的存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('CH')
        self.assertIn("CH", my_survey.responses)


class TestAnonymousSurvey(unittest.TestCase):
    """测试多个survey"""
    def test_store_single_response(self):
        """测试单个答案被妥善的存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_responses = ['CH', 'EN', 'JP']
        for response in my_responses:
            my_survey.store_response(response)
        for response in my_responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
