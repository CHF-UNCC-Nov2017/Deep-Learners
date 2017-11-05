import pandas as pd
from sklearn.linear_model import LinearRegression


class LR:
      def __init__(self):
         self.df = pd.read_csv('data.csv',header=None)
         print self.df
         self.y = [1,0,1,0]

      def fit(self):
          self.reg = LinearRegression()
          self.reg.fit(self.df,self.y)
     
      def predict(self,ll):
          return self.reg.predict(ll)


         
