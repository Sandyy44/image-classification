# image-classification

## Prerequisites

Before running the project, ensure you have **Python 3.x** installed on your machine.

## 🛠️ Installation & Setup

Follow these steps strictly to ensure the project runs correctly.

### 1. Install Dependencies
This project relies on specific versions of Python libraries. Install them using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 2. Data Placement
To ensure the scripts can locate the dataset, you must move the data folder to the correct location.

* Locate the folder named **`traffic_Data`**.
* Move this folder to the **root directory** of this project (the same level as this README file).

### 3. Split the Dataset
Before training or analysis, the dataset needs to be split (e.g., into training and testing sets).

Run the following command to execute the splitting script:

```bash
python split_data.py
```

---

## 📂 Project Structure

After completing the setup steps above, your project directory should look like this:

```text
├── dataset/               # Final Generated dataset folder
│   ├── train/
│   └── val/
├── traffic_Data/          # [MOVED HERE] The main dataset folder
│   ├── Data/
│   └── TEST/
├── split_data.py          # Script to split the dataset
├── .gitignore
├── labels.csv             # Labels of the main dataset
├── requirements.txt       # List of python dependencies
├── README.md              # This file
└── main.py                # (Your main application file)
```
