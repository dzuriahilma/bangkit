# Install Streamlit
!pip install streamlit

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set theme
sns.set(style='dark')

# Set Streamlit page configuration
st.set_page_config(
    page_title="Dashboard Penjualan (E-Commerce)",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Read CSV data from GitHub
alldata_df = pd.read_csv("https://github.com/dzuriahilma/bangkit/blob/main/all_data_marge.csv")

# Streamlit header with an attractive title
st.title('🛍️ Dashboard terkait E-Commerce🛍️')

# Description for context
st.markdown(
    "Halo! Bagaimana Keadaanmu? Selamat datang di Dashboard E-Commerce! Dashboard ini memberikan informasi tentang sebaran negara customer, "
    "Jenis pembayaran yang paling sering digunakan, Persentase customer yang memberikan review 5 dan hubungan / Korelasi antara ongkos kirim serta harga barang."
)

# Creating tabs for subheader
selected_tab = st.sidebar.radio("Pilih Menu", ["Sebaran negara", "Jenis Pembayaran", "Review Customer","Korelasi"])

if selected_tab == "Sebaran Negara":
    st.subheader("Sebaran Negara")

    # Calculate customer distribution in each country worldwide
    count_payment_type_data = alldata_df.groupby("customer_state").order_id.count().sort_values(ascending=False).reset_index()
    count_payment_type_data.head(15)

    # Bar plot to visualize customer distribution in each country worldwide
    bycategory_data = alldata_df.groupby(by=["customer_state"]).order_id.nunique().reset_index()
    bycategory_data.rename(columns={"order_id": "cust_count"}, inplace=True)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(
        y="customer_state",
        x="cust_count",
        hue="customer_state",
        data=bycategory_data.sort_values(by="cust_count", ascending=False),
        palette="pastel", legend=False
    )
    plt.title("Jumlah customer per negara di dunia", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot()

# Tab "Jenis Pembayaran"
elif selected_tab == "Jenis Pembayaran":
    st.subheader("Jenis Pembayaran")

    # Determine the percentage of payment types used
    count_payment_type_data = alldata_df.groupby("payment_type").order_id.count().sort_values(ascending=False).reset_index()

    # Bar plot to visualize the number of users per payment type
    bycategory_data = alldata_df.groupby(by=["payment_type"]).order_id.nunique().reset_index()
    bycategory_data.rename(columns={"order_id": "cust_count"}, inplace=True)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(
        y="cust_count",
        x="payment_type",
        hue="cust_count",
        data=bycategory_data.sort_values(by="cust_count", ascending=False),
        palette="colorblind", legend=False
    )
    plt.title("Jumlah pengguna per jenis pembayaran", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot()

# Tab "Review Customer"
elif selected_tab == "Review Customer":
    st.subheader("Review Customer")

    # Calculate the number of customer review scores
    count_payment_type_data = alldata_df.groupby("review_score").order_id.count().sort_values(ascending=False).reset_index()

    # Pie chart to visualize the proportion of customer review scores
    review_count = alldata_df['review_score'].value_counts()
    colors = sns.color_palette("Accent", len(review_count))
    explode = (0.1, 0, 0, 0, 0, 0)
    
    plt.pie(
        x=review_count,
        labels=review_count.index,
        autopct='%1.1f%%',
        colors=colors,
        explode=explode
    )
    plt.title('Proporsi Review Score Customer')
    st.pyplot()

# Tab "Korelasi"
elif selected_tab == "Korelasi":
    st.subheader("Korelasi")

    # Calculate the correlation between price and shipping cost
    sample_data = {
        'a': alldata_df['price'],
        'b': alldata_df['freight_value']
    }
    data = pd.DataFrame(sample_data)
    data.corr(numeric_only=True)
    
    # Scatter plot between price and shipping cost
    sns.scatterplot(x=alldata_df['price'], y=alldata_df['freight_value'])
    st.pyplot()

st.caption("Copyright by DzuriaHilma")
