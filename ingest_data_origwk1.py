import pandas as pd 
import sys
from sqlalchemy import create_engine
from time import time
import argparse
import os





def main(params): 
    user=params.user
    password = params.password
    host=params.host
    port = params.port
    db=params.db
    table_name = params.table_name
    
    #download the csv
    csv_name = "output.csv"
    # os system function can run command line arguments from Python
    os.system(f"wget {url} -O {csv_name}")


    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    #this loads just the column names in the datatbase with n=0   
    datadfiter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    dfiter = next(datadfiter)
    # this changes the two columns to datetime
    dfiter.tpep_pickup_datetime = pd.to_datetime(dfiter.tpep_pickup_datetime)
    dfiter.tpep_dropoff_datetime = pd.to_datetime(dfiter.tpep_dropoff_datetime)

    dfiter.head(n=0).to_sql(name=table_name, con=engine , if_exists='replace')
    datadfiter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    while True:
        t_start = time()
        dfiter = next(datadfiter)
        dfiter.tpep_pickup_datetime = pd.to_datetime(dfiter.tpep_pickup_datetime)
        dfiter.tpep_dropoff_datetime = pd.to_datetime(dfiter.tpep_dropoff_datetime)

        dfiter.to_sql(name=table_name, con=engine , if_exists='append')
        t_end = time()
        print(f"added another chunk it took {t_end - t_start:.2f} seconds" )
        


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='ingest csv file data to postgres db.')
    parser.add_argument('user', help='username for postgres')
    parser.add_argument('password', help='password for postgres')
    parser.add_argument('host', help='host  for postgres')
    parser.add_argument('port', help='port for postgres')
    parser.add_argument('db', help='databasename for postgres')
    parser.add_argument('table_name', help='name of table where we will write the results to')
    parser.add_argument('url', help='url of csv file')

    args = parser.parse_args()
    
    main(args)
