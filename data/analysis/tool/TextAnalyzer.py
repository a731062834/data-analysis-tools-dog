#encoding:utf8
import jieba
import re

class TextAnalyzer:
    regex_alpha = "[a-zA-Z]+"
    regex_num = "[0-9]+"

    def __init__(self):
        self.tokenizer = jieba.Tokenizer()

    def get_tokenized_words(self, input_text):
        tokenized_words = self.tokenizer.tokenize(input_text)

        valid_words = []
        for word in tokenized_words:
            if len(word) < 2:
                continue
            if re.match(self.regex_num, word):
                continue
            if re.match(self.regex_alpha, word):
                continue
            valid_words.append(word)
        return valid_words

    def get_sentences(self, input_text):
        return re.split("。|！|？", input_text)
