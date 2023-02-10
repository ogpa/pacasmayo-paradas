import requests
from bs4 import BeautifulSoup
import pandas as pd
import boto3


URL_TO_SCRAPE = "https://www.etsy.com/search/home-and-living"

#response = requests.get(URL_TO_SCRAPE)
# response = requests.get(URL_TO_SCRAPE) #Descomentar para hacer primer request

# resp_content = response.text  # Text property

scrape_filename = "scrape_data.html"

# with open(scrape_filename, "w", encoding="utf-8") as f:  # Descomentar para hacer primer request
#     f.write(resp_content)  # Descomentar para hacer primer request

# Sí se grabó correctamente
doc = BeautifulSoup(
    open(scrape_filename, "r", encoding="utf-8"), "html.parser")

class_product_names = "wt-text-caption v2-listing-card__title wt-text-truncate"

h2_tags = doc.find_all("h2", {"class": class_product_names})
# print(len(h2_tags))
# print(h2_tags)
products_name = []
for p in h2_tags:
    # print(p.text.strip())
    products_name.append(p.text.strip())

# Product name -> h2 class #content > div > div.wt-bg-white.wt-grid__item-md-12.wt-pl-xs-1.wt-pr-xs-0.wt-pr-md-1.wt-pl-lg-0.wt-pr-lg-0.wt-mt-xs-0.wt-overflow-x-hidden.wt-bb-xs-1 > div > div.wt-mt-xs-2.wt-text-black > div.wt-grid.wt-pl-xs-0.wt-pr-xs-0.search-listings-group > div:nth-child(2) > div.wt-bg-white.wt-display-block.wt-pb-xs-2.wt-mt-xs-0 > div > div > div > ul > li:nth-child(1) > div > div > a > div.v2-listing-card__info > div > h2

# h2_tags = doc.find_all("h2")

# print(len(h2_tags))
# Para ver los primero 10 h2 tags

# print(h2_tags[:10])  # Find something you love es el 1er h2_tag
# Para ignorar el "Find something" busco la clase
# class_name_of_h2 = "wt-text-caption v2-listing-card__title wt-text-truncate"
# h2_tags = doc.find_all("h2", {"class": class_name_of_h2})  # name of products
# print(len(h2_tags))
class_product_prices = "wt-text-title-01 lc-price"


class_original_prices = "wt-text-caption search-collage-promotion-price wt-text-slime wt-text-truncate wt-no-wrap"

for p in doc.find_all("p", {"class": class_original_prices}):
    p.decompose()


# p_tags = doc.find_all("p", {"class": class_product_prices})
# print(len(p_tags))
# print(p_tags)
span_class_prices = "currency-value"

span_tags = doc.find_all("span", {"class": span_class_prices})
# print(len(span_tags))
# print(span_tags)
products_price = []
for s in span_tags:
    # print(s.text)
    products_price.append(s.text)


# print(products_name)
# print(products_price)

products_dict = {"name": products_name,
                 "price": products_price}


# print(products_dict)
products_df = pd.DataFrame(products_dict)
# print(products_df)
df_filename = "products.csv"

products_df.to_csv(df_filename, index=False)
S3_RUTA_FOLDER = "bi-telemetria/gps-sin-reportar/csv/"
S3_BUCKET_NAME = "bucket-python-scrape-csv"


s3 = boto3.client("s3")
with open(csv_file_name, "rb") as f:
    s3.upload_fileobj(f, S3_BUCKET_NAME, csv_file_name)


# awsuser
# AwsUser2022

# Crewar tabla:
# create table test(
# name varchar,
# price numeric(10,2)
#   )
# No va a mostrar los datos de 3,800.00 por la coma

# 1. Crear classifier
# 2. Crear crawler s3: add classifier
# 3. Crear connection - aws redshift
# 4. Crear tabla en redshift (en caso la tabla que quiera usar no exista)
# 5. Crear crawler redshift - jdbc
# 6. Crear job
# 7. Edit inbound rules del VPC (está en Properties del Cluster -> security groups).
# "My IP". También habilitar el Publicly accessible
