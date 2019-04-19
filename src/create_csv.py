import os
import csv
import pandas as pd

def append_data(file_path,f_name,l_name):
    try:
        with open(file_path,'a+') as csvfile:
            fieldnames = {'id','first_name','last_name'}
            writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
            #reader
            try:
                df = pd.read_csv(file_path)
                id = len(df)
            except:
                id = 0
                writer.writeheader()
            finally:
                writer.writerow({'id':id,'first_name':f_name,'last_name':l_name})
    except Exception as e:
        print(e)

def main():
    append_data('data.csv','Abhishek','Sahu')

if __name__ == '__main__':
    main()