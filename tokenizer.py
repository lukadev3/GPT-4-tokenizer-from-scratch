import unicodedata

# Function returns a dictionary containing pairs of int values
# and the number of their occurrences in the list
def get_stats(ids):
    counts = {}  # Initialize a dictionary to hold counts of pairs
    iterator = 0  # Start iterator at the beginning of the list
    while iterator < len(ids) - 1:  # Loop through the list until the second to last element
        pair1 = (ids[iterator], ids[iterator + 1])  # Create a tuple of the current pair
        count = 1  # Initialize count for the current pair
        # Check for occurrences of the current pair in the list
        for i in range(0, len(ids) - 1):
            pair2 = (ids[i], ids[i + 1])  # Create a tuple for comparison
            if pair1 == pair2 and iterator != i:  # If the pairs match and it's not the same position
                count += 1  # Increment the count
        counts[pair1] = count  # Store the count of the current pair
        iterator += 1  # Move to the next element
    return counts  # Return the dictionary of counts


# Function that replaces two adjacent numbers (pair)
# in the list ids (list of int values) with the number idx
def merge(ids, pair, idx):
    new_ids = []  # Initialize a new list for modified ids
    i = 0  # Start index for iteration
    while i < len(ids):  # Iterate through the ids list
        if i < len(ids) - 1:  # Check if not at the last element
            check = (ids[i], ids[i + 1])  # Create a tuple of the current pair
        else:
            check = None  # If at the last element, set check to None
        if pair == check:  # If the current pair matches the one to merge
            new_ids.append(idx)  # Append the new index to new_ids
            i += 2  # Skip the next element as it's part of the merged pair
        else:
            new_ids.append(ids[i])  # Append the current id to new_ids
            i += 1  # Move to the next element
    return new_ids  # Return the modified list of ids


class Tokenizer():
    def __init__(self) -> None:
        self.merges = {}  # Initialize a dictionary to hold merges (pair -> idx)
        self.patern = ""  # Initialize a pattern for regex (to be defined in subclasses)
        self.special_tokens = {}  # Dictionary for special tokens (str -> int, e.g., |endoftext| -> 10089)
        self.vocab = self.build_vocab()  # Build the initial vocabulary

    # Method to train the tokenizer (to be implemented in subclasses)
    def train(self, text, vocab_size):
        pass

    # Method to decode ids back to text (to be implemented in subclasses)
    def decode(self, ids):
        pass

    # Method to encode text into ids (to be implemented in subclasses)
    def encode(self, text):
        pass

    # Creating vocabulary based on the first 256 characters from the ASCII table.
    # The rest is done through the merge dictionary, which contains information on
    # how pairs were encoded and any special characters not present in this general class.
    def build_vocab(self):
        vocab = {idx: bytes([idx]) for idx in range(256)}  # Create a vocabulary for the first 256 ASCII characters
        for (pair1, pair2), idx in self.merges.items():  # Iterate over each merge in the dictionary
            vocab[idx] = vocab[pair1] + vocab[pair2]  # Combine the byte representations of the pairs
        for special, idx in self.special_tokens.items():  # Handle special tokens
            vocab[idx] = special.encode("utf-8")  # Encode special tokens to bytes
        return vocab  # Return the constructed vocabulary
