# Semantic Similarity System for TOEFL Synonym Questions

This project implements an intelligent system to answer synonym questions found in tests like the Test of English as a Foreign Language (TOEFL). The system computes the semantic similarity between words to determine which word is the closest synonym of a given word from a list of choices.

## Objective

The goal is to compute the semantic similarity of a word with its potential synonyms using semantic descriptor vectors and cosine similarity. The system identifies the synonym of a given word from a list of choices by selecting the word with the highest semantic similarity.

## Features

- **Cosine Similarity Calculation**: Measures the cosine similarity between two sparse vectors (semantic descriptors).
- **Semantic Descriptor Generation**: Creates semantic descriptor vectors for words based on their co-occurrence in sentences.
- **Semantic Descriptor from Files**: Builds semantic descriptors from multiple text files, treating them as one large corpus.
- **Word Matching**: Chooses the word with the highest semantic similarity to the given word from a list of potential synonyms.
- **Test Evaluation**: Runs a test based on a file containing multiple synonym questions, evaluates the system's guesses, and returns the accuracy of the system's predictions.

## Key Functions

### `cosine_similarity(vec1, vec2)`
- **Description**: Computes the cosine similarity between two sparse vectors (dictionaries).
- **Input**: 
  - `vec1`: First vector as a dictionary.
  - `vec2`: Second vector as a dictionary.
- **Output**: A float representing the cosine similarity between the two vectors.

### `build_semantic_descriptors(sentences)`
- **Description**: Takes a list of sentences and returns a dictionary where each word is mapped to its semantic descriptor vector.
- **Input**:
  - `sentences`: List of lists, where each inner list represents a sentence as a list of words.
- **Output**: A dictionary where each word has a corresponding semantic descriptor vector as a dictionary.

### `build_semantic_descriptors_from_files(filenames)`
- **Description**: Processes multiple files and generates semantic descriptor vectors for all the words appearing in the combined texts.
- **Input**:
  - `filenames`: List of file names to process.
- **Output**: A dictionary of semantic descriptors for words in the files.

### `most_similar_word(word, choices, semantic_descriptors, similarity_fn)`
- **Description**: Given a word and a list of potential synonyms, selects the synonym with the highest semantic similarity.
- **Input**:
  - `word`: The word for which we want to find the synonym.
  - `choices`: A list of possible synonym choices.
  - `semantic_descriptors`: Dictionary containing the semantic descriptors of words.
  - `similarity_fn`: A function (such as `cosine_similarity`) to calculate the similarity between vectors.
- **Output**: The word from `choices` with the highest semantic similarity to `word`.

### `run_similarity_test(filename, semantic_descriptors, similarity_fn)`
- **Description**: Evaluates the system's performance by running it on a file containing synonym questions.
- **Input**:
  - `filename`: File containing synonym questions.
  - `semantic_descriptors`: Dictionary of semantic descriptors.
  - `similarity_fn`: Function to compute similarity between vectors.
- **Output**: A float representing the percentage of correctly guessed synonyms.

## Resources: 
This project was originally developed as part of the **ESC180: Introduction to Programming course** at the University of Toronto

## How to Run
### Clone the repository:

```bash
git clone https://github.com/najmasultani/Python-Projects-General.git

# Navigate to the Semantic Similarity folder
cd Python-Projects-General/Semantic Similarity

# Run the game
python synonyms.py

# Test the system with a synonym test file:
# Assuming you already have your semantic descriptors ready, for example:
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])

# Now, run the similarity test using your test.txt file:
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")
