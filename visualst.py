# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:37:36 2021

@author: admin
"""

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

uploaded_file= st.file_uploader("File uploader")

if uploaded_file is not None:
    dataframe=pd.read_csv(uploaded_file)
    st.write(dataframe)
    df1=dataframe.copy()
    st.write(df1.columns)
    cor= df1.corr()
    round(cor,3)
    st.write("corr")
  
    #fig,ax=plt.subplots()
    #sns.heatmap(cor,ax=ax,annot=True,cmap="YlGnBu")
    #fig=plt.figure()
    #fig=sns.pairplot(cor)
    #plt.show()
    #st.pyplot(fig)
    
    # f=scatter_matrix(df1,figsize=(12,8))
    # st.pyplot(f)
    
    
    fig2=sns.pairplot(df1)
    st.pyplot(fig2)
    
   
    










    x=st.multiselect("options",df1.columns)


    if x:

        p= st.text("do you want to delete columns")
        a1=st.button("Yes")
        a2=st.button("No")
      
      
        if a1:          
           b=df1.drop(x,axis=1)
           st.write(b)
          
    
    
            
        if a2:
            st.write(df1)
           
      