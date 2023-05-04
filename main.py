import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('hotel.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS hotels
             (hotel_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              address TEXT,
              city TEXT,
              state TEXT,
              zip TEXT,
              phone TEXT)''')

conn.commit()
conn.close()


# Connect to the database
conn = sqlite3.connect('hotel.db')
c = conn.cursor()


# Define the Streamlit app
def app():
    st.title('Hotel Management System')

    # Add a form to add a new hotel
    st.subheader('Add a New Hotel')
    name = st.text_input('Name')
    address = st.text_input('Address')
    city = st.text_input('City')
    state = st.text_input('State')
    zip = st.text_input('Zip')
    phone = st.text_input('Phone')
    if st.button('Add'):
        c.execute('INSERT INTO hotels (name, address, city, state, zip, phone) VALUES (?, ?, ?, ?, ?, ?)',
                  (name, address, city, state, zip, phone))
        conn.commit()
        st.success('Hotel added successfully!')

    # Add a form to search for hotels by city
    st.subheader('Search for Hotels by City')
    search_city = st.text_input('City')
    if st.button('Search'):
        hotels = pd.read_sql_query(f'SELECT * FROM hotels WHERE city = "{search_city}"', conn)
        st.write(hotels)


# Run the Streamlit app
app()
streamlit run app.py
