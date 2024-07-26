# importación de librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definición de las funciones que devuelven los dataframes luego de la lectura de archivos .csv
def lectura_datos_ecommerce_customers_dataset(ecommerce_customers_dataset):
    '''
    Esta función realizar la lectura de ecommerce_customers_dataset
    
    Returns:
    - Dataframe correspondientes a ecommerce_customers_dataset
    '''
    ecommerce_customers_df = pd.read_csv(ecommerce_customers_dataset)
    return ecommerce_customers_df


def lectura_datos_ecommerce_order_items_dataset(ecommerce_order_items_dataset):
    '''
    Esta realizar la lectura de ecommerce_order_items_dataset

    Returns:
    - Dataframe correspondientes a ecommerce_order_items_dataset
    '''
    ecommerce_order_items_df = pd.read_csv(ecommerce_order_items_dataset)
    return ecommerce_order_items_df


def lectura_datos_ecommerce_order_payments_dataset(ecommerce_order_payments_dataset):
    '''
    Esta función realizar la lectura de ecommerce_order_payments_dataset

    Returns:
    - Dataframe correspondientes a ecommerce_order_payments_dataset
    '''
    ecommerce_order_payments_df = pd.read_csv(ecommerce_order_payments_dataset)
    return ecommerce_order_payments_df


def lectura_datos_ecommerce_orders_dataset(ecommerce_orders_dataset):
    '''
    Esta función realizar la lectura de ecommerce_orders_dataset

    Returns:
    - Dataframe correspondientes a ecommerce_orders_dataset
    '''
    ecommerce_orders_df = pd.read_csv(ecommerce_orders_dataset)
    return ecommerce_orders_df


def lectura_datos_ecommerce_products_dataset(ecommerce_products_dataset):
    '''
    Esta función realizar la lectura de ecommerce_products_dataset

    Returns:
    - Dataframe correspondientes a ecommerce_products_dataset
    '''
    ecommerce_products_df = pd.read_csv(ecommerce_products_dataset)
    return ecommerce_products_df


# Definición de funciones para la exploración de los dataframes
def exploracion_datos_ecommerce_customers_df(ecommerce_customers_df):
    '''
    Esta función realiza la exploración del dataframe ecommerce_customers_df
    '''
    # Muestra la información del dataframe ecommerce_customers_df
    print("--------------------------------- Info ---------------------------")
    print(ecommerce_customers_df.info)
    # Muestra las primeras diez filas del dataframe ecommerce_customers_df
    print("--------------------------------- Head ---------------------------")
    print(ecommerce_customers_df.head())
    # Muestra las estadisticas descriptivas del dataframe ecommerce_customers_df
    print("--------------------------------- Describe -----------------------")
    print(ecommerce_customers_df.describe())

def exploracion_datos_ecommerce_order_items_df(ecommerce_order_items_df):
    '''
    Esta función realiza la exploración del dataframe ecommerce_order_items_df
    '''
     # Muestra la información del dataframe ecommerce_order_items_df
    print("--------------------------------- Info ---------------------------")
    print(ecommerce_order_items_df.info)
    # Muestra las primeras diez filas del dataframe ecommerce_order_items_df
    print("--------------------------------- Head ---------------------------")
    print(ecommerce_order_items_df.head())
    # Muestra las estadisticas descriptivas del dataframe ecommerce_order_items_df
    print("--------------------------------- Describe -----------------------")
    print(ecommerce_order_items_df.describe())

def exploracion_datos_ecommerce_order_payments_df(ecommerce_order_payments_df):
    '''
    Esta función realiza la exploración del dataframe ecommerce_order_payments_df
    '''
    # Muestra la información del dataframe ecommerce_order_payments_df
    print("--------------------------------- Info ---------------------------")
    print(ecommerce_order_payments_df.info)
    # Muestra las primeras diez filas del dataframe ecommerce_order_payments_df
    print("--------------------------------- Head ---------------------------")
    print(ecommerce_order_payments_df.head())
    # Muestra las estadisticas descriptivas del dataframe ecommerce_order_payments_df
    print("--------------------------------- Describe -----------------------")
    print(ecommerce_order_payments_df.describe())


def exploracion_datos_ecommerce_orders_df(ecommerce_orders_df):
    '''
    Esta función realiza la exploración del dataframe ecommerce_orders_df
    '''
    # Muestra la información del dataframe ecommerce_orders_df
    print("--------------------------------- Info ---------------------------")
    print(ecommerce_orders_df.info)
    # Muestra las primeras diez filas del dataframe ecommerce_orders_df
    print("--------------------------------- Head ---------------------------")
    print(ecommerce_orders_df.head())
    # Muestra las estadisticas descriptivas del dataframe ecommerce_orders_df
    print("--------------------------------- Describe -----------------------")
    print(ecommerce_orders_df.describe())


def exploracion_datos_ecommerce_products_df(ecommerce_products_df):
    '''
    Esta función realiza la exploración del dataframe ecommerce_products_df
    '''
    # Muestra la información del dataframe ecommerce_products_df
    print("--------------------------------- Info ---------------------------")
    print(ecommerce_products_df.info)
        # Muestra las primeras diez filas del dataframe ecommerce_products_df
    print("--------------------------------- Head ---------------------------")
    print(ecommerce_products_df.head())
        # Muestra las estadisticas descriptivas del dataframe ecommerce_products_df
    print("--------------------------------- Describe -----------------------")
    print(ecommerce_products_df.describe())




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

    # Exportar los dataframes en un archivo excel
    exportar_excel(dataframes)

    # Gráficos
    df_ecommerce_products_dataset["product_category_name"].value_counts().plot(kind="bar")
    plt.title("Gráfico de barras de producto")
    plt.savefig("productos_bar.png")

    df_ecommerce_products_dataset["product_category_name"].value_counts().plot(kind="pie")
    plt.title("Gráfico de torta de producto")
    plt.savefig("productos_pie.png")