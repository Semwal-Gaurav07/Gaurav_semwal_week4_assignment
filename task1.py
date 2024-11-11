def count_file_statistics(input_file, output_file):
    try:
        # Initialize counts
        line_count = 0
        word_count = 0
        char_count = 0

        # Open and read the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
                words = line.split()
                word_count += len(words)
                char_count += len(line)  # Counts all characters including spaces and newlines

        # Write the counts to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"Lines: {line_count}\n")
            file.write(f"Words: {word_count}\n")
            file.write(f"Characters: {char_count}\n")
        
        print(f"Results written to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError:
        print("Error: An I/O error occurred while reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the input and output file paths
input_file = 'input.txt'
output_file = 'output.txt'

# Run the function with the specified files
count_file_statistics(input_file, output_file)

