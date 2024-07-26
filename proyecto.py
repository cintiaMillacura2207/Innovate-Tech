# importación de librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Empieza el programa principal
if __name__ == "__main__":
    
    # Set de datos
    ecommerce_customers_dataset = 'raw_data\\ecommerce_customers_dataset.csv'
    ecommerce_order_items_dataset = 'raw_data\\ecommerce_order_items_dataset.csv'
    ecommerce_order_payments_dataset = 'raw_data\\ecommerce_order_payments_dataset.csv'
    ecommerce_orders_dataset = 'raw_data\\ecommerce_orders_dataset.csv'
    ecommerce_products_dataset = 'raw_data\\ecommerce_products_dataset.csv'

    # Lectura y retorno de dataframes
    df_ecommerce_customers_dataset = lectura_datos_ecommerce_customers_dataset(ecommerce_customers_dataset)
    # print(df_ecommerce_customers_dataset)
    df_ecommerce_order_items_dataset = lectura_datos_ecommerce_order_items_dataset(ecommerce_order_items_dataset)
    # print(df_ecommerce_order_items_dataset)
    df_ecommerce_order_payments_dataset = lectura_datos_ecommerce_order_payments_dataset(ecommerce_order_payments_dataset)
    # print(df_ecommerce_order_payments_dataset)
    df_ecommerce_orders_dataset = lectura_datos_ecommerce_orders_dataset(ecommerce_orders_dataset)
    # print(df_ecommerce_orders_dataset)
    df_ecommerce_products_dataset = lectura_datos_ecommerce_products_dataset(ecommerce_products_dataset)
    # print(df_ecommerce_products_dataset)

    # Exploración de los DataFrames
    exploracion_datos_ecommerce_customers_df(df_ecommerce_customers_dataset)
    exploracion_datos_ecommerce_order_items_df(df_ecommerce_order_items_dataset)
    exploracion_datos_ecommerce_order_payments_df(df_ecommerce_order_payments_dataset)
    exploracion_datos_ecommerce_orders_df(df_ecommerce_orders_dataset)
    exploracion_datos_ecommerce_products_df(df_ecommerce_products_dataset)

    # Se crea una lista con los dataframes 
    dataframes = [df_ecommerce_customers_dataset,df_ecommerce_order_items_dataset,
                 df_ecommerce_order_payments_dataset,df_ecommerce_orders_dataset,
                 df_ecommerce_products_dataset]