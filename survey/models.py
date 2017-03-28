from django.db import models


class Question(models.Model):
    # initialise question type constants
    SINGLE_QUESTION_TABLE = 'SingleQuestionTable'
    SINGLE_QUESTION_LIST = 'SingleQuestionList'
    MULTI_CHOICE_QUESTION = 'MultiChoiceQuestion'
    TEXT_QUESTION = 'TextQuestion'

    # initialise yes no constants
    YES = 'Y'
    NO = 'N'

    # tuple of question choices, will make a drop down box.
    QUESTION_TYPE_CHOICES = (
        (SINGLE_QUESTION_TABLE, 'Single Question Table'),
        (SINGLE_QUESTION_LIST, 'Single Question List'),
        (MULTI_CHOICE_QUESTION, 'Multi Choice Question'),
        (TEXT_QUESTION, 'Text Question'),
    )

    YES_NO_CHOICES = (
        (YES, 'Y'),
        (NO, 'N'),
    )

    # model fields
    section_seq = models.IntegerField(default=0)
    section_text = models.CharField(max_length=255)
    page_seq = models.IntegerField(default=0)
    page_header = models.TextField(blank=True)
    sub_page_seq = models.IntegerField(default=0)
    sub_page_header = models.TextField(blank=True)
    question_seq = models.IntegerField(default=0)
    question_text = models.TextField(blank=True)
    question_type = models.CharField(max_length=55, choices=QUESTION_TYPE_CHOICES, default=SINGLE_QUESTION_TABLE)
    sub_question = models.CharField(max_length=1, choices=YES_NO_CHOICES, default=NO)
    response_seq = models.IntegerField(default=0)
    response_text = models.CharField(max_length=255)
    response_value = models.IntegerField(default=0)
    response_ops = models.CharField(max_length=1, choices=YES_NO_CHOICES, default=NO)
    response_columns = models.IntegerField(default=0)

    def __str__(self):
        return self.section_text[:10] + " : " + self.question_text[:10] + " : " + self.response_text[:10]
