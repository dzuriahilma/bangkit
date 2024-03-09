import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Set tema Streamlit
st.set_page_config(
    page_title="Dashboard Penjualan (E-Commerce)",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Membaca data CSV dari GitHub
alldata_df = pd.read_csv("https://github.com/dzuriahilma/bangkit/blob/main/all_data_marge.csv")

# Header Streamlit dengan judul menarik
st.title('🛍️ Dashboard terkait E-Commerce🛍️')

# Menambahkan deskripsi untuk memberikan konteks
st.markdown(
    "Halo! Bagaimana Keadaanmu? Selamat datang di Dashboard E-Commerce! Dashboard ini memberikan informasi tentang sebaran negara customer, "
    "Jenis pembayaran yang paling sering digunakan, Persentase customer yang memberikan review 5 dan hubungan / Korelasi antara ongkos kirim serta harga barang."
)

# Membuat tab untuk subheader
selected_tab = st.sidebar.radio("Pilih Menu", ["Sebaran negara", "Jenis Pembayaran", "Review Customer","Korelasi"])

if selected_tab == "Sebaran Negara":
    st.subheader("Sebaran Negara")

    #Menghitung jumlah sebaran customer di setiap negara di dunia
    count_payment_type_data = all_data.groupby("customer_state").order_id.count().sort_values(ascending=False).reset_index()
    count_payment_type_data.head(15)

    #Diagram batang untuk melihat jumlah sebaran customer di setiap negara di dunia
    bycategory_data = all_data.groupby(by=["customer_state"]).order_id.nunique().reset_index()
    bycategory_data.rename(columns={
    "order_id": "cust_count"
    }, inplace=True)
    
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
    plt.show()

# Tab "Jenis Pembayaran"
elif selected_tab == "Jenis Pembayaran":
    st.subheader("Jenis Pembayaran")

    #menentukan persentase tipe pembayaran yang digunakan
    count_payment_type_data = all_data.groupby("payment_type").order_id.count().sort_values(ascending=False).reset_index()

    ##Diagram batang untuk melihat jumlah pengguna per jenis pembayaran yang digunakan
    bycategory_data = all_data.groupby(by=["payment_type"]).order_id.nunique().reset_index()
    bycategory_data.rename(columns={
    "order_id": "cust_count"
    }, inplace=True)
    
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
    plt.show()

# Tab "Review Customer"
elif selected_tab == "Review Customer":
    st.subheader("Review Customer")

    #Menghitung jumlah review score customer
    count_payment_type_data = all_data.groupby("review_score").order_id.count().sort_values(ascending=False).reset_index()

    #membuat diagram lingkaran proporsi review score customer
    review_count = all_data['review_score'].value_counts()
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
    plt.show()

# Tab "Korelasi"
elif selected_tab == "Korelasi":
    st.subheader("Korelasi")

    #hitung korelasi antara harga dan ongkos kirim
    sample_data = {
    'a': all_data['price'],
    'b': all_data['freight_value']
    }
    data = pd.DataFrame(sample_data)
    data.corr(numeric_only=True)
    
    #membuat scatter plot antara harga dan ongkos kirim
    sns.scatterplot(x=all_data['price'], y=all_data['freight_value'])
    plt.show()

st.caption("Copyright by DzuriaHilma")
