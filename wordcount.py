import sys
import csv
import string
from functools import reduce
import time
import os

def mapper(text):
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    
    # Split the text into words
    words = text.split()
    
    # Emit each word with a count of 1
    return [(word, 1) for word in words]

def reducer(word_counts, word_count):
    word, counts = word_count
    
    # Sum the counts for each word
    if word in word_counts:
        word_counts[word] += counts
    else:
        word_counts[word] = counts
    
    return word_counts

# Check if the input file name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the input file name as a command-line argument.")
    sys.exit(1)

input_file = sys.argv[1]

# Read text from file with explicit encoding
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Start measuring the time
start_time = time.time()

# Map step: split the text into words and emit each word with a count of 1
mapped_data = mapper(text)

# Reduce step: combine the counts for each word
word_counts = reduce(reducer, mapped_data, {})

# End measuring the time
end_time = time.time()

# Calculate the processing time
processing_time = end_time - start_time

# Format the processing time to two decimal places
processing_time_formatted = "{:.2f}".format(processing_time)

# Get the current iteration number
iteration = 1
while os.path.exists(f"output-{iteration}.csv"):
    iteration += 1

# Construct the output file name with the iteration number
output_file = f"output-{iteration}.csv"

# Write the word counts to a CSV file with proper encoding and error handling
with open(output_file, 'w', newline='', encoding='utf-8', errors='replace') as file:
    writer = csv.writer(file)
    writer.writerow(['Word', 'Count'])
    writer.writerows(word_counts.items())

# Print the processing time and the output file name
print("Processing time:", processing_time_formatted, "seconds")
print("Word counts saved to:", output_file)