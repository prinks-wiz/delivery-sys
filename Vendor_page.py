#Vendor page 
import collections.abc
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping
import streamlit as st
from StackQueue import Stacks,ArrayQueue
from gsheetsdb import connect
from datetime import datetime
from gspread_pandas import Spread,Client
from google.oauth2 import service_account
import json
import pandas as pd
from pandas import DataFrame
import User_inputs

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
service_account_info = json.load(open('service_account.json'))
credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes = scope)
client = Client(scope=scope,creds=credentials)
spreadsheetname = "Inventory_data_pub"
spread = Spread(spreadsheetname,client = client)

sh = client.open(spreadsheetname)
worksheet_list = sh.worksheets()

# Functions 
@st.cache()
# Get our worksheet names
def worksheet_names():
    sheet_names = []   
    for sheet in worksheet_list:
        sheet_names.append(sheet.title)  
    return sheet_names

# Get the sheet as dataframe
def load_the_spreadsheet(spreadsheetname):
    worksheet = sh.worksheet(spreadsheetname)
    df = DataFrame(worksheet.get_all_records())
    return df


def update_the_spreadsheet(spreadsheetname,dataframe):
    col = ['Name','phone number','address','email','cart','Time_stamp']
    spread.df_to_sheet(dataframe[col],sheet = spreadsheetname,index = False)
    st.sidebar.info('Request accepted')


what_sheets = worksheet_names()

st.header("Vinayaga Supermarket")

st.title("Received orders")

df = load_the_spreadsheet('CartList')
df.drop_duplicates(subset = 'phone number',keep=True,inplace=True)
order_queue = ArrayQueue()
#Using a queue to enter the existing orders
for i in range(0,df.shape[0]):
    order_queue.enqueue(list(df.iloc[i]))

st.subheader("Current order")
st.write(order_queue.first())
order_complete = st.button("Order delivered")
if order_complete:
    order_queue.dequeue()
    df.drop([0],axis=0,inplace = True)
    update_the_spreadsheet('CartList',df[:-1])

st.write(" ")
st.subheader("Pending orders")
st.write(df[1:])
