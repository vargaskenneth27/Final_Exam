import sys, getopt
import pandas as pd


def count_kmers(text, k):
    """
    Counts the number of unique substrings of length k
    that appear as substrings of the given string text

    :param k: Substring length as an integer
    :param text: Given sequence as a string
    :returns the number of unique substrings of length k
    :raises ValueError: if input is invalid
    """
    # Error : null or empty text
    if not text:
        raise ValueError()

    # Error : invalid k
    if len(text) < k or k <= 0:
        raise ValueError()

    # Create an empty set
    kmers = set()

    # Count the number of unique substrings of length k
    for i in range(0, len(text) - k + 1):
        kmers.add(text[i : i + k])

    # Return length as the result
    return len(kmers)


def possible_kmers(text, k):
    """
    Calculates the number of possible Kmers of length k
    that can be contained within the given string text

    :param k: Substring length as an integer
    :param text: Given sequence as a string
    :returns the number of possible Kmers of length k
    :raises ValueError: if k is invalid
    """
    # Error : null or empty text
    if not text:
        raise ValueError()

    # Error : invalid k
    if len(text) < k or k <= 0:
        raise ValueError()

    # Get minimum as described and return
    return min(len(text) - k + 1, pow(4, k))


def linguistic_complexity(text):
    """
    Calculates the linguistic complexity of the given string text

    :returns the linguistic complexity of text
    :param text: Given sequence as a string
    :raises ValueError: if text is null or empty
    """
    # Error : null or empty text
    if not text:
        raise ValueError()

    # Length of the text
    n = len(text)

    # Declare arrays to be used to create a Pandas dataframe
    ks = []
    observed = []
    possible = []

    # For all poossible values of k
    for k in range(1, n + 1):
        # Calculate the number of observed and possible kmers
        ks.append(k)
        observed.append(count_kmers(text, k))
        possible.append(possible_kmers(text, k))

    # Create a Pandas dataframe
    result = {'K': ks, 'Observed': observed, 'Possible': possible}
    df = pd.DataFrame(result, columns=['K', 'Observed', 'Possible'])

    # Output dataframe
    df.to_csv(text + ".csv", index=False)

    # Calculate linguistic complexity
    complexity = df['Observed'].sum() / float(df['Possible'].sum())

    # Return result
    return complexity


def main(argv):
    """
    Main function to read an input file of sequences,
    to calculate linguistic complexities of each sequence and
    to write output per sequence to an output file

    Keyword arguments:
    argv --- Given arguments in the command line
    """
    # Parse input arguments to read I/O file paths and k
    k = 3
    input_path = ''
    output_path = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        print('kmers.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('kmers.py -i <input file> -o <output file>')
        elif opt in ("-i", "--input"):
            input_path = arg
        elif opt in ("-o", "--output"):
            output_path = arg

    # Open input file and check if it's open
    input_file = open(input_path, 'r')
    if input_file.closed:
        print("Failed to open input file")
        sys.exit(3)

    # Open output file and check if it's open
    output_file = open(output_path, 'w')
    if output_file.closed:
        print("Failed to open output file")
        sys.exit(3)

    # Read lines
    lines = input_file.readlines()

    # Process line by line
    for line in lines:
        # Remove any trailing whitespace
        text = line.rstrip()

        # Calculate linguistic complexity
        try:
            # Calculate linguistic complexity
            complexity = linguistic_complexity(text)

            # Print given text and complexity as a new line
            output_file.write(text + " : linguistic complexity = " + str(complexity) + '\n')
        except ValueError:
            print("Invalid input")

    # Close input file
    input_file.close()
    output_file.close()

    # Print finished message
    print("Done")


if __name__ == "__main__":
    main(sys.argv[1:])