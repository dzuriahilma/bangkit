import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

sns.set(style='whitegrid')

"""## Data Wrangling

### Gathering Data

####menginput data customer
"""

customer_data = pd.read_csv("/content/customers_dataset.csv")
customer_data.head()
#Mengeluarkan data frame data customer dengan tampilan hanya 5 baris pertama

"""####menginput data order_items

"""

item_order_data = pd.read_csv("/content/order_items_dataset.csv")
item_order_data.head()
#Mengeluarkan data frame data order_item dengan tampilan hanya 5 baris pertama

"""####menginput data order_payments"""

payment_data = pd.read_csv("/content/order_payments_dataset.csv")
payment_data.head()
#Mengeluarkan data frame data pembayaran dengan tampilan hanya 5 baris pertama

"""####menginput data order_review"""

review_data = pd.read_csv("/content/order_reviews_dataset.csv")
review_data.head()
#Mengeluarkan data frame data review dengan tampilan hanya 5 baris pertama

"""####menginput data orders"""

order_data = pd.read_csv("/content/orders_dataset.csv")
order_data.head()
#Mengeluarkan data frame data order dengan tampilan hanya 5 baris pertama

"""####menginput data products"""

produk_data = pd.read_csv("/content/products_dataset.csv")
produk_data.head()
#Mengeluarkan data frame data produk dengan tampilan hanya 5 baris pertama

"""####menginput data namaproduk


"""

namaproduk_data = pd.read_csv("/content/product_category_name_translation.csv")
namaproduk_data.head()

"""### Assessing Data

####Assessing dataframe costumer_data
"""

#Periksa tipe data setiap kolom
customer_data.info()

#Menampilkan statistika deskriptif
customer_data.describe()

#Periksa data duplikat
print("Banyak data duplikat: ", customer_data.duplicated().sum())

"""####Assessing dataframe item_order_data"""

#Periksa tipe data setiap kolom
item_order_data.info()

#Menampilkan statistika deskriptif
item_order_data.describe()

#Periksa data duplikat
print("Banyak data duplikat: ", item_order_data.duplicated().sum())

"""####Assessing dataframe payment_data"""

#Periksa tipe data per kolom
payment_data.info()

#Menampilkan statistika deskriptif
payment_data.describe()

#Periksa data duplikat
print("Banyak data duplikat: ",payment_data.duplicated().sum())

"""####Assessing dataframe review_data"""

#Periksa tipe data per kolom
review_data.info()

#Cek jumlah missing value pada tiap kolom
review_data.isna().sum()

"""> Terdapat 87656 missing values pada `review_comment_title` dan 58247 missing valuae pada `review_comment_message` sehingga perlu ditinjau ulang sebelum dianalisis."""

#Periksa data duplikat
print("Banyak data duplikat: ",review_data.duplicated().sum())

"""####Assessing dataframe order_data"""

#Periksa tipe data per kolom
order_data.info()

#Cek jumlah missing value pada tiap kolom
order_data.isna().sum()

"""Terdapat 160 missing value pada order_approved_at, 1783 pada order_delivered_carrier_date, 2965 pada order_delivered_costumer_date dan 1 pada order_estimated_delivery_date"""

#Periksa data duplikat
print("Banyak data duplikat: ",order_data.duplicated().sum())

"""####Assessing dataframe products"""

#Periksa tipe data per kolom
produk_data.info()

#Cek jumlah missing value pada tiap kolom
produk_data.isna().sum()

"""Terdapat beberapa missing value di beberapa variabel"""

#Periksa data duplikat
print("Banyak data duplikat: ",produk_data.duplicated().sum())

"""####Assessing dataframe namaproduk"""

#Periksa tipe data per kolom
namaproduk_data.info()

#Menampilkan statistika deskriptif
namaproduk_data.describe()

#Periksa data duplikat
print("Banyak data duplikat: ",namaproduk_data.duplicated().sum())

"""### Cleaning Data

####Dataframe customer
"""

#Menghapus data yang tidak digunakan
customer_data.drop(['customer_unique_id','customer_city','customer_zip_code_prefix'], axis=1, inplace=True)
customer_data.head()

"""####Dataframe item_order"""

#Menghapus data yang tidak digunakan
item_order_data.drop(['order_item_id','seller_id','shipping_limit_date'], axis=1, inplace=True)
item_order_data.head()

"""####Dataframe payments"""

#Menghapus data yang tidak digunakan
payment_data.drop(['payment_sequential','payment_installments'], axis=1, inplace=True)
payment_data.head()

"""####Dataframe review"""

#Menghapus data yang tidak digunakan
review_data.drop(['review_id','review_comment_title','review_comment_message','review_creation_date','review_answer_timestamp'], axis=1, inplace=True)
review_data.head()

"""####Dataframe orders"""

#Menghapus data yang tidak digunakan
order_data.drop(order_data.columns.difference(['order_id','customer_id',"order_status"]), axis=1, inplace=True)
order_data.head()

"""####Dataframe products"""

#Menghapus data yang tidak digunakan
produk_data.drop(produk_data.columns.difference(['product_id','product_category_name']), axis=1, inplace=True)
produk_data.head()

"""##Exploratory Data Analysis

###Exploratory orders dan customer
"""

#menggabungkan orders dan customer
customer_order_data = pd.merge(
   left=order_data,
   right=customer_data,
   how="left",
   left_on="customer_id",
   right_on="customer_id"
)
customer_order_data.head()

"""###Exploratory products & prodnames"""

#menggabungkan orders dan customer
order_customer_data = pd.merge(
   left=produk_data,
   right=namaproduk_data,
   how="left",
   left_on="product_category_name",
   right_on="product_category_name"
)
order_customer_data.head()

"""###Exploratory order_items & order_payments"""

#menggabungkan item dan payments
order_payment_data = pd.merge(
   left=item_order_data,
   right=payment_data,
   how="left",
   left_on="order_id",
   right_on="order_id"
)
order_payment_data.head()

"""###Exploratory product_payments & order_review"""

#menggabungkan product_payments dan product_review
selling_data = pd.merge(
   left=order_payment_data,
   right=review_data,
   how="left",
   left_on="order_id",
   right_on="order_id"
)
selling_data.head()

#mengisi missing value
#review_score berupa numerik, jadi diisi dengan mean
selling_data.review_score.mean()
selling_data['review_score'].fillna(value=4.073, inplace=True) #isi dengan mean
selling_data.isna().sum() #re-check

"""###Exploratory customer_orders & selling


"""

#menggabungkan orders_customer dan selling
all_data = pd.merge(
   left=customer_order_data,
   right=selling_data,
   how="left",
   left_on="order_id",
   right_on="order_id"
)
all_data.head()

#menggabungkan products_name dan selling
all_data = pd.merge(
   left=all_data,
   right=order_customer_data,
   how="left",
   left_on="product_id",
   right_on="product_id"
)
all_data.head()

print("Banyak data duplikat: ", all_data.duplicated().sum())

all_data.isna().sum()

all_data.drop_duplicates(inplace=True)
print("Banyak data duplikat: ", all_data.duplicated().sum())

all_data.to_csv("all_data_marge.csv", index=False)

"""## Visualization & Explanatory Analysis

### Pertanyaan 1: Bagaimana sebaran negara customer di seluruh dunia?
"""

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

"""Berdasarkan bar chart yang ditampilkan, dari 27 negara sebaran customer, customer yang paling banyak berasal dari negara SP, sedangan customer paling sedikit dari negara RR

### Pertanyaan 2: Apa jenis pembayaran yang paling banyak digunakan oleh customer?
"""

#Menghitung jumlah pengguna per jenis pembayaran yang digunakan
count_payment_type_data = all_data.groupby("payment_type").order_id.count().sort_values(ascending=False).reset_index()
count_payment_type_data.head(15)

#Diagram batang untuk melihat jumlah pengguna per jenis pembayaran yang digunakan
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

"""Berdasarkan tampilan bar chart tersebut, dapat dilihat bahwa jenis pembayaran yang paling sering digunakan adalah jenis pembayaran credit card

###Pertanyaan 3: Jenis kategori produk apa yang sering dibeli customer?
"""

#Menghitung jumlah pengguna per jenis kategori produk
count_product_category_data = all_data.groupby("product_category_name").order_id.count().sort_values(ascending=False).reset_index()
count_product_category_data.head(10)

#Diagram batang untuk melihat jumlah customer per kategori produk
bycategory_data = all_data.groupby(by=["product_category_name"]).order_id.nunique().reset_index()
bycategory_data.rename(columns={
    "order_id": "cust_count"
}, inplace=True)

plt.figure(figsize=(10, 10))

sns.barplot(
    y="product_category_name",
    x="cust_count",
    hue="product_category_name",
    data=bycategory_data.sort_values(by="cust_count", ascending=False),
    palette="Set1", legend=False
)
plt.title("Jumlah pengguna per kategori produk", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=9)
plt.show()

""">Berdasarkan bar chart tersebut, dapat dilihat bahwa kategori produk yang paling sering dibeli customer adalah cama mesa banho sebesar 10797

###Pertanyaan 4: Berapa persentase customer yang memberikan review rating 5?
"""

#Menghitung jumlah review score customer
count_payment_type_data = all_data.groupby("review_score").order_id.count().sort_values(ascending=False).reset_index()
count_payment_type_data.head(15)

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

"""Berdasarkan pie chart tersebut, persentase customer yang memberikan review score 5 adalah sebanyak 57% dimana persentase tersebut paling banyak dibandingkan review score yang lain

### Pertanyaan 5 : Bagaimana hubungan / korelasi antara harga dan ongkos kirim?
"""

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

"""Berdasarkan output tersebut, dapat dilihat bahwa harga dan ongkos kirim berkorelasi positif yakni sebesar 0,421. Berdasarkan scaterplot juga dapat dilihat bahwa sebaran data membentuk pola berhubungan positif

## Conclusion

- sebaran negara customer dari 27 negara, paling banyak berasal dari negara SP dan paling sedikit berasal dari negara RR
- Tipe pembayaran paling sering digunakan adalah credit_card
- Jenis kategori produk yang paling sering dibeli customer adalah kategori cama_mesa_banho
- Sebanyak 57% customer memberikan review score 5
- Terdapat korelasi positif antara harga dan ongkos kirim
"""
