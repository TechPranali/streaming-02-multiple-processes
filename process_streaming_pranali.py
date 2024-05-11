import csv
import time
import random

def stream_data_from_csv(csv_filename):
    """Stream data from a CSV file."""
    with open(csv_filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            yield row
            # Generate one record every 1-3 seconds
            time.sleep(1 + (2 * random.random()))


def write_data_to_output(data, output_filename):
    """Write data to the output file."""
    with open(output_filename, 'a') as output_file:
        for item in data:
            output_file.write(str(item) + '\n')


def main():
    csv_filename = 'people_info.csv'  # Path to your CSV file
    output_filename = 'streamed_data.txt'

    # Stream data from CSV file
    data_stream = stream_data_from_csv(csv_filename)

    # Write streamed data to output file
    write_data_to_output(data_stream, output_filename)


if __name__ == "__main__":
    main()
