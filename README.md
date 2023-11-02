# Decision Tree Model for Classification from Scratch Using ID3 Algorithm

## Description
This project implements a decision tree model for classification using Python. The decision tree is built from scratch and applied to a sample dataset for predicting whether to play tennis based on weather conditions.

## Dataset Source
The dataset used in this project is sourced from Kaggle and is available at the following link: [Play Tennis Dataset](https://www.kaggle.com/tareqjoy/trainplaytennis). It provides information about various weather conditions and whether to play tennis based on those conditions.

## Getting Started
To get started with the project, follow these steps:
- Clone the repository to your local machine.
- Install the required dependencies using the provided requirements.txt file.
- Run the main script to train the decision tree model and visualize the results.
- Use the provided GUI for predicting new instances based on the trained model.

## Contents
- main.py: Contains the main script for building the decision tree model and evaluating its performance.
- PlayTennis.csv: Sample dataset used for training and testing the model.
- decision_tree.png: Visual representation of the trained decision tree.

## Usage
You can use this project to understand the fundamentals of decision tree classification and how to implement it in Python. Additionally, the provided GUI allows users to input new instances and obtain predictions from the trained model.

## Model Overview
The decision tree model is implemented from scratch using the ID3 algorithm. It recursively splits the dataset based on the information gain at each node. Categorical data is converted to numerical data using the LabelEncoder from the scikit-learn library.

## Code Explanation
The main script (main.py) contains functions for building the decision tree, calculating information gain, and evaluating the model's performance. It also includes a function to visualize the decision tree using the graphviz library.

## GUI Implementation
The GUI allows users to load a pre-trained decision tree model and make predictions on new instances. It simplifies the process of interacting with the model without requiring knowledge of the underlying code.

## Results
The model's performance is evaluated using various metrics such as accuracy, precision, recall, and F1 score. The confusion matrix provides insights into the model's predictive capabilities.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information
For any inquiries or feedback, please contact Vaibhav Pant at pantvaibhav16@gmail.com .

## Future Improvements
- Incorporate more advanced decision tree algorithms for better performance.
- Expand the GUI functionality to support more complex interactions.
- Include additional evaluation metrics and visualizations for a comprehensive analysis of the model's performance.

