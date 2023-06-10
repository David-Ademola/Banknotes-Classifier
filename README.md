# Banknotes-Classifier

This repository contains a Python script for performing classification tasks on a banknotes dataset using different machine learning algorithms. Each branch of the repository corresponds to a different classification algorithm, showcasing its implementation and results.

## Dataset

The dataset used for classification is stored in the file `banknotes.csv`. It consists of several features extracted from images of banknotes and a corresponding label indicating whether the banknote is authentic or counterfeit. The features are numerical values representing various properties of the banknotes.

## Dependencies

To run the script, you need to have the following dependencies installed:

- Python (version 3.6 or above)
- scikit-learn (version 0.24 or above)

You can install the required dependencies using pip:
`pip install -r requirements.txt`

## Usage

1. Clone the repository to your local machine: `git clone <repository_url>`

2. Switch to the desired branch corresponding to the classification algorithm you want to use: `git checkout <branch_name>`

The available branches are:

- `knn`: K-Nearest Neighbors algorithm
- `perceptron`: Perceptron algorithm
- `naive-bayes`: Naive Bayes algorithm

3. Run the script: `python classification.py`

The script will load the dataset, split it into training and testing sets, train the selected classification model, make predictions on the testing set, and display the accuracy of the model.

## Results

After running the script, you will see the results printed to the console. The results include the number of correctly and incorrectly classified instances and the accuracy of the model on the testing set.

## License

This project is licensed under the MIT License. You can find the license details in the `LICENSE` file.

## Credits

The banknotes dataset used in this project is a publicly available dataset and can be found [here](https://archive.ics.uci.edu/ml/datasets/banknote+authentication). The dataset was originally donated by Dr. Volker Lohweg of the University of Applied Sciences, Ostwestfalen-Lippe, Germany.








