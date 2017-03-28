from rest_framework import serializers
from survey.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('section_seq', 'section_text', 'page_seq', 'page_header',
                  'sub_page_seq', 'sub_page_header',
                  'question_seq', 'question_text', 'question_type', 'sub_question',
                  'response_seq', 'response_text', 'response_value', 'response_ops', 'response_columns')