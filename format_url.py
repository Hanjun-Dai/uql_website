import os
import sys
import csv

folder = sys.argv[1]
with open(os.path.join(folder, 'data.csv'), 'r') as f:
  reader = csv.reader(f)
  header = next(reader)
  for row in reader:
    print(f"  '{row[0]}',")

