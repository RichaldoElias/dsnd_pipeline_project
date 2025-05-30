# Sentimental Analysis

This project aims to analyze customer reviews to predict product recommendations using machine learning techniques. It consolidates knowledge gained in the nanodegree while solving a real-world problem.

# Project Objective

The goal of this notebook is to predict whether a customer recommends a product based on review data. We will use various machine learning techniques to achieve this.

# Expected Outcomes

By the end of this notebook, we aim to have a trained model that can predict product recommendations with high accuracy, precision, and recall.

## Getting Started

To run this project, you need to have python installed on your local notebook, I prefer to use conda as package manager.

## Project Structure
The files in this projects are splitted into different folders and below herewith the actual view:

```
dsnd_pipeline_project/
├── data/
│   └── reviews.csv
├── notebooks/
│   ├── helpers.py
│   └── src.ipynb
├── .gitignore
├── LICENSE.txt
├── README.md
└── requirements.txt
```


- **data/**: csv file containing the dataset.
- **notebooks/**: Jupyter notebooks, documentation and helper code.
- **requirements.txt**: Python dependencies.


### Dependencies

Some example of dependencies below, but refer to the requirements file for full installation
```
conda install conda-forge::scikit-learn
```

### Installation

Step by step explanation of how to get a dev environment running.


## Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/RichaldoElias/dsnd_pipeline_project.git
     cd dsnd_pipeline_project
     ```

2. Create a virtual environment and activate it:
     ```bash
     conda create --name <my-env>
     conda activate <my-env>
     ```

3. Install dependencies:
     ```bash
     conda install --yes --file requirements.txt
     ```


## Usage

1. Run Jupyter notebooks or lab - I prefer labs for having a beautiful interface:
In your terminal
     ```bash
     jupyter lab
     ```
     Open and execute notebooks in the `notebooks/` directory that is called src.ipynb.

## License

[License](LICENSE.txt)
