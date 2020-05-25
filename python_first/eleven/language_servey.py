from python_first.eleven import AnonymousSurvey

"""定义一个问题， 并创建一个表示调查的AnonymousSurvey"""

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("input 'q' to quit")

while True:
    response = input("please input :")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)
# 显示调查结果
print("\nThank you to everyone who participated in the survey")
my_survey.show_results()