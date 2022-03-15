import sys
import re
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import requests
from bs4 import BeautifulSoup
import pickle
from sklearn.compose import make_column_transformer
from PIL import Image
import pytesseract 
from rake_nltk import Rake 
import json

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


class FakeNewsAPI:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()
        self.article = []

    def upload(self,filename):
        text=pytesseract.image_to_string(Image.open(filename))
        return text

    def remove_tags(self,url):
    
        # parse html content
        soup = BeautifulSoup(url, "html.parser")
    
        for data in soup(['style', 'script']):
            # Remove tags
            data.decompose()
    
        # return data by retrieving the tag content
        return ' '.join(soup.stripped_strings)

    def word_drop(self,text):
        text = text.lower()
        text = re.sub('\[.*?\]','',text)
        text = re.sub('\\W'," ",text)
        #text = re.sub('https?://\S+[www\.\S+','',text)
        text = re.sub('<.*?>+','',text)
        #text = re.sub('[%s]' % re.escape(string.punctuation),'',text)
        text = re.sub('\n','',text)
        text = re.sub('\w*\d\w','',text)
        text = text = " ".join(text.split())
        return str(text) 

    # def get_string_article(self,url):
    #     page = requests.get(url)
    #     page_soup = BeautifulSoup(page.content,'html.parser')
    #     headline = page_soup.find_all("div",{"class":"fc-item__header"})
    #     containers = page_soup.find_all("div",{"class":"fc-item__standfirst"})
    #     for head,data in zip(headline,containers):
    #         self.article.append(self.word_drop(head.text) +" "+ self.word_drop(data.text))
    #     return self.article
    
    def keyword_extractor(self,text):
        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(text)
        keywords_extracted = rake_nltk_var.get_ranked_phrases()
        return keywords_extracted    

    def RelatedArticles(self,keywords):
        String = ""
        # for i in keywords:
        #     String += i+' '
        # keywords = String[:-1]
        url = ('https://newsapi.org/v2/everything?'
               'q="'+keywords[0]+'"&'
               'from=2022-03-10&'
               'sortBy=publishedAt&'
               'apiKey=90f109e6441746059c15c51f558f869b')
        response = requests.get(url)
        return response.json()
    
    @staticmethod
    def Stringer(i):
        if i == 1:
            return "True News"
        else:
            return "Fake News"
    
    def textSimilarty(self,text,news):                              #news should be in list format
        news.append(text)
        similarText = {}
        TextNews = []
        vectorizer = CountVectorizer()
        features = vectorizer.fit_transform(news).todense()
        for n,f in zip(news,features):
            similarText[n] = euclidean_distances(features[-1],f) 
        coeff  = list(similarText.values())
        Nnews = list(similarText.keys())
        for _ in range(6):
            minDist = coeff.index(min(coeff))
            TextNews.append(Nnews[minDist])
            coeff.pop(minDist)
            Nnews.pop(minDist)
        return TextNews[1:]
        

    def __main__(self):
        u = pd.read_csv('./data/train.csv')
        u = u.dropna()
        y = u['label']
        X = u['text']
        text = "Ukrainian city of Mariupol 'near to humanitarian catastrophe' after bombardment"
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.1)
        X_train = self.vectorizer.fit_transform(X_train)
        X_test = self.vectorizer.transform(X_test)
        predict_ = self.vectorizer.transform([sys.argv[1]]) 
        self.model.fit(X_train, y_train) 
        y_pred = self.model.predict(predict_)
        # y_rand = self.model.predict(random)
        # print(self.Stringer(y_pred[0]))
        # print(y_rand)

        # fetching the news from newsAPI
        similarNews = []
        relatedNews = self.RelatedArticles(self.keyword_extractor(text))
        for news in relatedNews['articles']:
            similarNews.append(news['title'])
        print(self.Stringer(y_pred))
        for i in self.textSimilarty(text,similarNews):
            print(i+"`")
                

        #saving the model
        # pickle.dump(LR,open("logistic_regression_model",'wb'))
        # print(f'Accuracy is :{self.model.score(X_test,y_test)*100 :4.2f}')


if __name__ == '__main__':
    fakeNews = FakeNewsAPI()
    fakeNews.__main__()
