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


    # Establecer la columna indices de las tablas como la clave primaria en el Dataframe
    establecer_index(dataframes)
    print(dataframes)

    # Limpieza y procesamiento de los datos
    eliminar_duplicados(dataframes)
    eliminar_nan(dataframes)
    rellenar_nan(df_ecommerce_customers_dataset,df_ecommerce_order_items_dataset,df_ecommerce_order_payments_dataset,df_ecommerce_orders_dataset,df_ecommerce_products_dataset)
    rellenar_nan_ecommerce_customers_df(df_ecommerce_customers_dataset)
    eliminar_columnas_redundantes_ecommerce_products_dataset(df_ecommerce_products_dataset)


    # Operaciones sobre los DataFrames

    # Obtiene el numero total de clientes unicos en el conjunto de datos
    total_customer_unique_id(df_ecommerce_customers_dataset)
    
    # Calcula el promedio de valor de pago por pedido
    promedio_pago_pedido(df_ecommerce_order_payments_dataset)
    
    # Determina la categoria de producto mas vendida
    categoria_producto_mas_vendido(df_ecommerce_products_dataset)
    
    # Calcula el numero total de pedidos realizados
    total_pedidos_realizados(df_ecommerce_orders_dataset)