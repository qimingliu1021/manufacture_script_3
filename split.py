import csv

csv_dir = 'data/manufacture_3rd.csv'
count = 0

with open(csv_dir, "r") as csv_file: 
  reader = csv.reader(csv_file, delimiter=',')
  headers = next(reader)

  with open("data/manufacture_3_1.csv", "w") as csv_file: 
    writer = csv.writer(csv_file)
    writer.writerow(headers)
  with open("data/manufacture_3_2.csv", "w") as csv_file: 
    writer = csv.writer(csv_file)
    writer.writerow(headers)
  with open("data/manufacture_3_3.csv", "w") as csv_file: 
    writer = csv.writer(csv_file)
    writer.writerow(headers)
  with open("data/manufacture_3_4.csv", "w") as csv_file: 
    writer = csv.writer(csv_file)
    writer.writerow(headers)
  with open("data/manufacture_3_5.csv", "w") as csv_file: 
    writer = csv.writer(csv_file)
    writer.writerow(headers)


  for row in reader: 
    count += 1
    if count <= 50: 
      with open("data/manufacture_3_1.csv", "a") as csv_file: 
        writer = csv.writer(csv_file)
        writer.writerow(row)
    if count > 50 and count <= 100: 
      with open("data/manufacture_3_2.csv", "a") as csv_file: 
        writer = csv.writer(csv_file)
        writer.writerow(row)
    if count > 100 and count <= 150: 
      with open("data/manufacture_3_3.csv", "a") as csv_file: 
        writer = csv.writer(csv_file)
        writer.writerow(row)
    if count > 150 and count <= 200:
      with open("data/manufacture_3_4.csv", "a") as csv_file: 
        writer = csv.writer(csv_file)
        writer.writerow(row)
    if count > 200:
      with open("data/manufacture_3_5.csv", "a") as csv_file: 
        writer = csv.writer(csv_file)
        writer.writerow(row)

