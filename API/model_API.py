
import re
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import requests
from bs4 import BeautifulSoup
import pickle
from sklearn.compose import make_column_transformer
from PIL import Image
import pytesseract 
import os
# import nltk, spacy 
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

    def get_string_article(self,url):
        page = requests.get(url)
        page_soup = BeautifulSoup(page.content,'html.parser')
        headline = page_soup.find_all("div",{"class":"fc-item__header"})
        containers = page_soup.find_all("div",{"class":"fc-item__standfirst"})
        for head,data in zip(headline,containers):
            self.article.append(self.word_drop(head.text) +" "+ self.word_drop(data.text))
        return self.article
    
    def RelatedArticles(keywords):
        url = ('https://newsapi.org/v2/everything?'
               'q='+keywords+'&'
               'from=2022-01-11&'
               'sortBy=popularity&'
               'apiKey=90f109e6441746059c15c51f558f869b')
        response = requests.get(url)
        return response.json()

    # def Cleaner():
    #     nlp = spacy.load("en_core_sci_lg")
    #     text = """spaCy is an open-source software library for advanced natural language processing, 
    #             written in the programming languages Python and Cython. The library is published under the MIT license
    #             and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
    #     doc = nlp(text)
    #     print(doc.ents)
    
    def __main__(self):
        u = pd.read_csv('../data/train.csv')
        u = u.dropna()
        y = u['label']
        X = u['text']
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.1)

        X_train = self.vectorizer.fit_transform(X_train)
        X_test = self.vectorizer.transform(X_test)
        predict_ = pd.DataFrame(self.get_string_article("https://www.theguardian.com/international"))
        predict_ = self.vectorizer.transform(predict_[0]) 
        random = self.vectorizer.transform(["Don Halcomb, a farmer in Adairville, Ky. is expecting his profit to vanish this year, largely because of the confluence of falling crop prices and rising costs for seeds and other materials. The price of an bag of seed corn rose to $300 from $80 in the last decade, as the companies that produced them consolidated, he said. And with the recent decline in commodity prices, Mr. Halcomb said he expects to lose $100 an acre this year. “We’re producing our crops at a loss now, just like the oil guys are pumping oil at a loss,” Mr. Halcomb, who grows corn, soybeans, wheat and barley on his   family farm, said by telephone on Wednesday. “You can’t cut your costs fast enough. ” It is a common plight of farmers across the United States, with the global agriculture industry in a wrenching downturn. Because farmers have produced too much corn, wheat and soybeans, they have been forced to slash prices to sell their crops. They have also reduced spending on seeds, pesticides and fertilizer, which has eaten into sales at agribusiness giants, including Monsanto and DuPont. In response, these companies have sought   deals to cut costs and weather the industry’s storm. Four major agribusiness mergers have been announced in the last year. The latest is Bayer AG’s $56 billion takeover of Monsanto  —   the largest acquisition of 2016  —   announced on Wednesday. Every merger creates the possibility of higher costs for farmers. Mr. Halcomb buys seeds with traits licensed to Monsanto of St. Louis and seeds from DuPont, which has a deal pending to merge with Dow Chemical. His fertilizers are made of potassium compounds and phosphate produced by Agrium of Calgary, Alberta, which on Monday agreed to combine with the fertilizer producer Potash Corporation of Saskatchewan. He uses pesticides made by Syngenta of Switzerland, which agreed in February to a takeover by the China National Chemical Corporation. “It’s just like any other industry that consolidates,” Mr. Halcomb said. “They tell the regulators they’re   and then they tell their customers they have to increase pricing after the deal’s done. ” The companies say they are merging to diversify and increase growth and research capabilities, but these deals, given their size and scope, have already caught the attention of lawmakers and regulators in Washington. There is no guarantee that they will all receive regulatory approval, and some companies may have to sell assets to allay antitrust concerns. Dow’s merger with DuPont is under Justice Department review. The market seemed to anticipate hurdles for the Monsanto deal on Wednesday. Shares of the company closed about 20 percent lower than the $128 per share cash offer from Bayer, which is based in Leverkusen, Germany. Shares of each company gained less than 1 percent after the deal was announced. Adding the assumption of about $10 billion of Monsanto debt, Bayer’s total $66 billion pact is the largest   deal, according to data compiled by Thomson Reuters, ahead of InBev’s $60. 4 billion offer for another St.   company,   in June 2008. Senator Charles E. Grassley, Republican of Iowa and chairman of the Judiciary Committee, scheduled a hearing next week to discuss the possible effect of these   mergers on farming. Iowa produced more corn last year than any other state, according to the National Corn Growers Association. “It seems to be catching fire and happening so fast with so many,” Senator Grassley said in a phone interview. “When you have less competition, prices go up. ” European competition regulators also said publicly, before a   deal was even signed, that they would look at how it could affect prices and the availability of seed products, as well as research. Liam Condon, who leads Bayer’s   division, said in an interview that the company did an “extensive analysis” with regard to antitrust before approaching Monsanto in May. Mr. Condon said that he does not believe there is much overlap between their portfolios, because Bayer’s focus is largely on crop protection, while Monsanto’s is on seeds and traits. He said the companies assume they may need to sell off some assets to appease regulators. Monsanto, which is famous for its production of genetically modified seeds, rejected several offers from Bayer as too low. Wednesday’s deal represented a 44 percent premium to Monsanto’s stock price on May 9, the day before Bayer’s interest in a deal surfaced. To assuage Monsanto’s concerns, Bayer threw in a $2 billion breakup fee if the deal fell apart on antitrust grounds. The strategic goal of the deal, according to Bill Selesky, an analyst at Argus Research, is to create a    experience for farmers, making Bayer the world’s largest supplier of seeds and farm chemicals. By improving the product for farmers, the combined company could ultimately raise prices, Mr. Selesky said in an interview. Senator Grassley said that he had spoken with a few farmers who believed the deals were necessary so large agribusinesses could continue to absorb the costs of researching and developing products and getting government approval for them. Bayer and Monsanto said they planned to cut about $1. 2 billion worth of costs as part of the deal, helping to improve efficiency. But Jim Benham of Versailles, Ind. the president of the Indiana Farmers Union, was not so optimistic. He blamed the rising costs of inputs  —   seeds, fertilizer and the like  —   for eating away at farmers’ profit margins, and warned that consolidation will make it worse. Costs have already risen by double digits over the last four to five years, and the proposed   merger could accelerate that. “The merger is going to hurt the farmer,” said Mr. Benham, who grows corn, soybeans and sometimes wheat on his   farm. “The more consolidation we have on our inputs, the worse it gets. ” Mr. Condon of Bayer said that the company would not raise prices without providing more value to farmers. “This is a highly competitive industry, and just increasing prices without having any additional advantage or benefit for growers won’t go anywhere,” he said. “It’s up to us to show what we’re offering will help farmers improve their return on investment. ” Some farmers said the consolidation could even enable prices to fall. Christine Hamilton manages a farm of more than 12, 000 acres in Kimball, S. D. growing crops like corn and operating a ranch. She said that if the deal can pass the antitrust screening, then maybe it could actually help farmers. “I understand how companies need to get bigger in order to be competitive,” she said. “As we are in a low part of the cycle, anything that might have a chance of reducing our input prices would be great. ”"])

        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(predict_)
        y_rand = self.model.predict(random)
        print(y_pred)
        print(y_rand)
        #saving the model
        # pickle.dump(LR,open("logistic_regression_model",'wb'))
        print(f'Accuracy is :{self.model.score(X_test,y_test)*100 :4.2f}')


if __name__ == '__main__':
    fakeNews = FakeNewsAPI()
    fakeNews.__main__()
    