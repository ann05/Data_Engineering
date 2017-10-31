# Data_Engineering
Insight Data_Engineering code challenge

The code uses the following libraries:
1. Numpy
2. Pandas
3. Sys

For computing the solution, I have taken 2 dictionaries and made a combination of (CMTE_ID,ZIP_CODE) and (CMTE_ID,TRANSACTION_DATE) as the keys. The values associated with these keys are in the form of a list, where the contents are 1. List of all the Transaction_amt, 2. Number of transactions, 3. Total of Transaction amt. The list of transaction amt helps us calculate the median till that record for ZIP_CODE base data and the final median for the TRANSACTION_DT based data.

The code takes the input and output files as a command line argument to write the output into the files and read the input from the file.

calling the program:

python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

python (file with the code) (input_file) (output_file for zip_code) (output_file for transaction_date).
