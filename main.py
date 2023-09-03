import streamlit as st
import pandas as pd
import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()

# Create empty dataframes for each table
customer_table = pd.DataFrame(columns=['First Name', 'Last Name', 'Gender', 'Phone Number'])
booking_table = pd.DataFrame(columns=['Booking ID', 'Booking Type', 'Booking Date'])
reservation_table = pd.DataFrame(columns=['Reservation ID', 'Check In Date', 'Check Out Date', 'No. of Days'])
room_table = pd.DataFrame(columns=['Room No', 'Room Type', 'No. of Occupants', 'Room Price'])
address_table = pd.DataFrame(columns=['Street', 'City', 'State', 'Country'])
invoice_table = pd.DataFrame(columns=['Invoice Number', 'Booking ID'])
line_table = pd.DataFrame(columns=['Service ID', 'Service Quantity'])
services_table = pd.DataFrame(columns=['Type', 'Cost'])
transactions_table = pd.DataFrame(columns=['Transaction Number', 'Payment Method', 'Payment Date', 'Invoice Number'])
satisfaction_table = pd.DataFrame(columns=['Satisfaction ID', 'Satisfaction Level'])

# Define sidebar menu
menu = ['Customer', 'Booking', 'Reservation', 'Room', 'Address', 'Invoice', 'Line', 'Services', 'Transactions',
        'Satisfaction']
choice = st.sidebar.selectbox("Select a table", menu)

# Display table based on user choice
if choice == "Customer":
    st.subheader("Customer")
    st.write("Add a Customer")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    phone_number = st.text_input("Phone Number")
    if st.button("Submit"):
        customer_table.loc[len(customer_table)] = [first_name, last_name, gender, phone_number]
        st.success("Customer has been added successfully.")
    st.write("View Customers")
    st.write(customer_table)

elif choice == "Booking":
    st.subheader("Booking")
    st.write("Add a Booking")
    booking_id = st.text_input("Booking ID")
    booking_type = st.selectbox("Booking Type", ["Single", "Double", "Suite"])
    booking_date = st.date_input("Booking Date")
    if st.button("Submit"):
        booking_table.loc[len(booking_table)] = [booking_id, booking_type, booking_date]
        st.success("Booking has been added successfully.")
    st.write("View Bookings")
    st.write(booking_table)

elif choice == "Reservation":
    st.subheader("Reservation")
    st.write("Add a Reservation")
    reservation_id = st.text_input("Reservation ID")
    check_in_date = st.date_input("Check In Date")
    check_out_date = st.date_input("Check Out Date")
    no_of_days = st.text_input("Number of Days")
    if st.button("Submit"):
        reservation_table.loc[len(reservation_table)] = [reservation_id, check_in_date, check_out_date, no_of_days]
        st.success("Reservation has been added successfully.")
    st.write("View Reservations")
    st.write(reservation_table)

elif choice == "Room":
    st.subheader("Room")
    st.write("Add a Room")
    room_No = st.text_input("Room No")
    room_type = st.selectbox("Room Type", ["Single", "Double", "Triple"])
    no_of_occupants = st.text_input("No. of Occupants")
    room_price = st.text_input("Room Price")
    if st.button("Submit"):
        room_table.loc[len(room_table)] = [room_No, room_type, no_of_occupants, room_price]
        st.success("Room has been added successfully.")
    st.write("View Rooms")
    st.write(room_table)

elif choice == "Address":
    st.subheader("Address")
    st.write("Add a Address")
    Street = st.text_input("Street")
    City = st.text_input("City")
    State = st.text_input("State")
    Country = st.text_input("Country")
    if st.button("Submit"):
        address_table.loc[len(address_table)] = [Street, City, State, Country]
        st.success("Address has been added successfully.")
    st.write("View Address")
    st.write(address_table)

elif choice == "Invoice":
    st.subheader("Invoice")
    st.write("Add an Invoice")
    invoice_number = st.text_input("Invoice Number")
    booking_id = st.selectbox("Booking ID", booking_table['Booking ID'].tolist())
    if st.button("Submit"):
        invoice_table.loc[len(invoice_table)] = [invoice_number, booking_id]
        st.success("Invoice has been added successfully.")
    st.write("View Invoices")
    st.write(invoice_table)

elif choice == "Line":
    st.subheader("Line")
    st.write("Add a Line")
    service_id = st.text_input("Service ID")
    service_quantity = st.text_input("Service Quantity")
    if st.button("Submit"):
        line_table.loc[len(line_table)] = [service_id, service_quantity]
        st.success("Line has been added successfully.")
    st.write("View Lines")
    st.write(line_table)

elif choice == "Add Service":
    st.subheader("Add a Service")
    service_type = st.text_input("Service Type")
    service_cost = st.number_input("Service Cost")
    if st.button("Submit"):
        services_table.loc[len(services_table)] = [service_type, service_cost]
        st.success("Service has been added successfully.")
    st.subheader("View Services")
    st.write(services_table)

elif choice == "Transactions":
    st.subheader("Transactions")
    st.write("Add a Transaction")
    transaction_number = st.text_input("Transaction Number")
    payment_method = st.selectbox("Payment Method", ["Credit Card", "Debit Card", "Cash"])
    payment_date = st.date_input("Payment Date")
    invoice_number = st.selectbox("Invoice Number", invoice_table['Invoice Number'].tolist())
    if st.button("Submit"):
        transactions_table.loc[len(transactions_table)] = [transaction_number, payment_method, payment_date,
                                                           invoice_number]
        st.success("Transaction has been added successfully.")
    st.write("View Transactions")
    st.write(transactions_table)

elif choice == "Satisfaction":
    st.subheader("Satisfaction")
    st.write("Add a Satisfaction")
    satisfaction_id = st.text_input("Satisfaction ID")
    satisfaction_level = st.slider("Satisfaction Level", min_value=1, max_value=10, step=1)
    if st.button("Submit"):
        satisfaction_table.loc[len(satisfaction_table)] = [satisfaction_id, satisfaction_level]
        st.success("Satisfaction has been added successfully.")
    st.write("View Satisfaction")
    st.write(satisfaction_table)


