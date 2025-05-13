import pandas as pd
import streamlit as st

crypto = st.text_input("Put a crypto abreviation:")
currency = st.text_input("Put a currency abreviation:")
threshold_value = st.number_input("Put a threshold value:",
                          min_value = 0 , max_value=999999999)

import requests
import json

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '293d98a6-6458-42e4-b609-6c5ffed19c24',
}

if crypto and currency and threshold_value: 
    response = requests.get(f"https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={crypto}&convert={currency}"
                        , headers=headers)
    
    if response.status_code in [200,201]:
        print("Success")
        print(json.dumps(response.json(),indent=4))
    else:
        print(f"Error {response.status_code} with error: {response.text}")
    
    price = response.json()["data"][crypto][0]["quote"][currency]['price']
else:
    st.info("Check the fields and fill them all.")


if st.button("Notify me"):
    st.write(f"The current price of {crypto} is {price} {currency}. We will notify you when the price reaches {threshold_value} {currency}.")