import Aspose.Cells

# Load the JSON file
workbook = Aspose.Cells.Workbook()
workbook.LoadFromJson("json_file.json")

# Convert JSON to PDF
workbook.Save("pdf_file.pdf")

# Get the conversion result of JSON to PDF
pdf_file = open("pdf_file.pdf", "rb")
pdf_content = pdf_file.read()
pdf_file.close()

# Print the PDF content
print(pdf_content)
