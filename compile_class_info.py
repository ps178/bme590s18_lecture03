import glob
import pandas as pd

def main():
   class_data = collect_all_csv_filenames()
   read_csv(class_data)
   write_data(class_data)

def collect_all_csv_filenames():
   dfList = []  #Create empty dict to hold  DataFrames
   for csv_files in glob.glob('*.csv'):  #Collect all the csv files 
      if not csv_files.endswith('mlp6.csv'):  #This is not very modular
         df = pd.read_csv(csv_files, header=None) #Save the csv files into dataframe
         dfList.append(df)
   class_combined = pd.concat(dfList, axis=0)
   colnames = ['Name','Last_Name','NetID','GitHub','Team_Name']
   class_combined.columns = colnames
   class_combined.to_csv('everyone.csv', index=None)
   return class_combined

def read_csv(class_data):
   check_no_spaces(class_data)
   check_camel_case(class_data)

def write_data(class_data):
   for (idx, row) in class_data.iterrows():
      name = row[-3]
      row.to_json(name + '.json')

def check_no_spaces(class_data):
   for (idx, row) in class_data.iterrows():
      if ' ' in row[-1]:
         print('Someone messed up!')

def check_camel_case(class_data):
   counter2 = 0
   for (idx, row) in class_data.iterrows():
      counter = 0
      for i in row[-1]:
         if i.isupper():
            counter = counter+1
      if counter > 1:
        counter2 = counter2+1
   print(counter2)

if __name__ == "__main__":
   main()  












