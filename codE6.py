"""
This script is used to merge all text files into just one
text file & also put the current timestamp in it.
"""
import datetime
import glob2

filename = datetime.datetime.now();
all_txt_files = glob2.glob('*.txt') ;

#print (*all_txt_files, sep='\n');


with open(filename.strftime("%a %d %B %Y %I %M")+".txt",'w') as file:
   for text in all_txt_files:
      with open(text,'r') as f:
        file.write(f.read()+'\n');

#filename = datetime.datetime.now()
#
# def create_file():
#     """This function creates an empty file """
#     with open(filename.strftime("%a %d %B %Y %I %M %S %f %p")+".txt",'w') as file:
#         file.write("")
#
# create_file()
