import os
import sys
import shutil
import csv


out_folder = sys.argv[1]
img_folder = os.path.join(out_folder, 'png')
if not os.path.isdir(img_folder):
  os.makedirs(img_folder)

with open(os.path.join(out_folder, 'data.csv'), 'r') as f:
  reader = csv.reader(f)
  header = next(reader)
  print(header)
  for row in reader:
    fname = row[0]
    src = os.path.join('val', fname)
    shutil.copyfile(src, os.path.join(img_folder, fname))
