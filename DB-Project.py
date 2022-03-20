
import pandas as pd
from pyjstat import pyjstat
from matplotlib import pyplot as plt
import json
import requests
import sqlite3
from sqlite3 import Error
import pprint
print(sqlite3.sqlite_version)

#Had to try. Might one day work just that easy.

test = requests.get(
    'https://pxnet2.stat.fi:443/PXWeb/api/v1/fi/Postinumeroalueittainen_avoin_tieto/2022/paavo_pxt_12f3.px')
test = test.json()

# JSON-query containing the information from the selected Zip-code areas year 2020 published 2022
session = requests.Session()

query = {
"query": [
    {
      "code": "Postinumeroalue",
      "selection": {
        "filter": "item",
        "values": [
          "00130",
          "02380",
          "16710",
          "41930",
          "54800"
        ]
      }
    },
    {
      "code": "Tiedot",
      "selection": {
        "filter": "item",
        "values": [
          "tr_mtu"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}
url = "https://pxnet2.stat.fi:443/PXWeb/api/v1/fi/Postinumeroalueittainen_avoin_tieto/2022/paavo_pxt_12f3.px"



response = session.post(url, json=query)
income22 = json.loads(response.text)

# JSON-query containing the information from the selected Zip-code areas year 2019 published 2021.
session = requests.Session()

query = {
    "query": [
        {
            "code": "Postinumeroalue",
            "selection": {
                "filter": "item",
                "values": [
                    "00130",
                    "02380",
                    "16710",
                    "41930",
                    "54800"
                ]
            }
        },
        {
            "code": "Tiedot",
            "selection": {
                "filter": "item",
                "values": [
                    "tr_mtu"
                ]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}
url = "https://pxnet2.stat.fi:443/PXWeb/api/v1/fi/Postinumeroalueittainen_avoin_tieto/2021/paavo_pxt_12f3.px"

response = session.post(url, json=query)
income21 = json.loads(response.text)

#JSON-query containing the information from the selected Zip-code areas year 2018 published 2020.
session = requests.Session()

query = {
    "query": [
        {
            "code": "Postinumeroalue",
            "selection": {
                "filter": "item",
                "values": [
                    "00130",
                    "02380",
                    "16710",
                    "41930",
                    "54800"
                ]
            }
        },
        {
            "code": "Tiedot",
            "selection": {
                "filter": "item",
                "values": [
                    "tr_mtu"
                ]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}
url = "https://pxnet2.stat.fi:443/PXWeb/api/v1/fi/Postinumeroalueittainen_avoin_tieto/2020/paavo_pxt_12f3.px"

response = session.post(url, json=query)
income20 = json.loads(response.text)

# Needs new query from Paavo-API because of the different URL.
# JSON-query containing the information from the selected Zip-code areas from 2016 published 2019.
session = requests.Session()

query = {

    "query": [
        {
            "code": "Postinumeroalue",
            "selection": {
                "filter": "item",
                "values": [
                    "00130",
                    "02380",
                    "16710",
                    "41930",
                    "54800"
                ]
            }
        },
        {
            "code": "Tiedot",
            "selection": {
                "filter": "item",
                "values": [
                    "Tr_mtu"
                ]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}

url = "https://pxnet2.stat.fi:443/PXWeb/api/v1/fi/Postinumeroalueittainen_avoin_tieto/2019/paavo_5_tr_2019.px"


response = session.post(url, json=query)
income19 = json.loads(response.text)

# JSON-query containing the information from the selected Zip-code areas from 2015 published 2018.
session = requests.Session()

query = {

    "query": [
        {
            "code": "Postinumeroalue",
            "selection": {
                "filter": "item",
                "values": [
                    "00130",
                    "02380",
                    "16710",
                    "41930",
                    "54800"
                ]
            }
        },
        {
            "code": "Tiedot",
            "selection": {
                "filter": "item",
                "values": [
                    "Tr_mtu"
                ]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}


url = "https://pxnet2.stat.fi:443/PXWeb/api/v1/fi/Postinumeroalueittainen_avoin_tieto/2018/paavo_5_tr_2018.px"


response = session.post(url, json=query)
income18 = json.loads(response.text)


def create_connection(incomesdb):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect("incomesdb.db")
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_sql_database(database):

    #Create tables
    sql_create_income22_table = """ CREATE TABLE IF NOT EXISTS income2022 (
                                        zip text PRIMARY KEY,
                                        area text,
                                        income integer 
                                        
                                    ); """

    sql_create_income21_table = """ CREATE TABLE IF NOT EXISTS income2021 (
                                        zip text PRIMARY KEY,
                                        area string,
                                        income text 
                                        
                                    ); """

    sql_create_income20_table = """ CREATE TABLE IF NOT EXISTS income2020 (
                                        zip text PRIMARY KEY,
                                        area text,
                                        income integer
                                        
                                    ); """

    sql_create_income19_table = """ CREATE TABLE IF NOT EXISTS income2019 (
                                        zip text PRIMARY KEY,
                                        area text,
                                        income integer
                                        
                                    ); """

    sql_create_income18_table = """ CREATE TABLE IF NOT EXISTS income2018 (
                                        zip text PRIMARY KEY,
                                        area text ,
                                        income integer
                                        
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:

        create_table(conn, sql_create_income22_table)

        create_table(conn, sql_create_income21_table)

        create_table(conn, sql_create_income20_table)

        create_table(conn, sql_create_income19_table)

        create_table(conn, sql_create_income18_table)
    else:
        print("Error! cannot create the database connection.")


def parser(income, zip_code_count=5):
    """ Function parses JSON-dict
    :param income: Nested dict from JSON-query
    :param zip_code_count number of zip-codes used. Default value: 5
    :return: df_temp which contains parsed names and values for selected year.
    """

    zip_codes = income['dimension']['Postinumeroalue']['category']['index'].keys()
    zip_label = income['dimension']['Postinumeroalue']['category']['label'].values()

    value = income['value']

    #Convert dict_keys and dict_values to string-variables.
    zip_codes = [str(i) for i in zip_codes]
    zip_label = [str(i) for i in zip_label]

    #Iterate through the list and combine information to wanted list.
    df_temp = []
    for i in range(5):
        temp = []
        temp.append(zip_codes[i])
        temp.append(zip_label[i])
        temp.append(value[i])
        df_temp.append(temp)

    return df_temp


def insert_query(database, year, income):

    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    sql_ = "INSERT INTO income%s VALUES (?,?,?)" % year

    for i in range(5):

        # This is the q-mark style:
        cursor.execute(sql_, (income[i][0], income[i][1], income[i][2]))

    conn.commit()


def plotter(dfall):
    value = []  # Empty lists in which the indexes are stored
    #name = []
    zip_codes = []

    years = list(dfall.keys())  # Selecting a dataframe-key (years)
    df = dfall.get(years[0])  # Dataframe for years

    # Loop to iterate over keys and appending them to the zip_codes list
    for l in df:
        zip_codes.append(l[0])

    #While-loop to ask the wanted zip_code area
    while (1):
        i = input(
            "Which zip-code area? Available: 00130, 02380, 16710, 41930 and 54800. Selected: ")

        if i in zip_codes:  # Checks if the input zip-code can be found
            print("OK")
            # Saving the index of wanted zip-code to check where it is stored in the dataframe
            j = zip_codes.index(i)
            break
        else:
            print("not available")

    # Loop to the select the wanted year and append it on the name-list
    for key in dfall:
        x = dfall.get(key)
        x = x[j]
        value.append(x[2])

    name = x[1]

    #Plt-plot to show the income-growth over the years
    plt.plot(years, value)
    plt.title(name)
    plt.xlabel("year")
    plt.ylabel("yearly median income (eur)")
    plt.show()

    #Calculating the average change in selected areas income
    average = (value[-1] / value[0]) * 100

    print("Household median income growth during five years in area %s has been %f percentage" % (
        name, (average - 100)))


def main():
    database = r"..\incomesdb.db"

    #Call to create SQLite-database
    create_sql_database(database)

    #Call to parser and storing the individual JSON-querys to designated variables
    df22 = parser(income22)
    df21 = parser(income21)
    df20 = parser(income20)
    df19 = parser(income19)
    df18 = parser(income18)

    #Denerates the "dfall"-dictionary where years are stored as keys. Inserts wanted information to database and plots the results.
    dfall = {"2018": df18, "2019": df19,
             "2020": df20, "2021": df21, "2022": df22}
    plotter(dfall)
    for i in range(5):
        year = list(dfall.keys())[i]
        income = dfall.get(year)

        insert_query(database, year, income)

    #get_posts() #Helper function to check the tables contents


if __name__ == '__main__':
    main()

#Conclusions and suggestions are provided in ipynb.file