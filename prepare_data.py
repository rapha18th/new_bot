# Import invoice2data
from invoice2data import extract_data

# Define the PDF file URL
pdf_url = "https://docdro.id/3822GDQ"

# Extract data from the PDF file
data = extract_data(pdf_url)

# Convert the data to a CSV string
import csv
import io

csv_file = io.StringIO()
csv_writer = csv.writer(csv_file)
csv_writer.writerow(data.keys()) # Write the header row
csv_writer.writerow(data.values()) # Write the data row

# Print the CSV string
print(csv_file.getvalue())
