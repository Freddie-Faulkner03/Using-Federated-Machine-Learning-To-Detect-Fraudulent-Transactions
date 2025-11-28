# Using Federated Machine Learning to Detect Fraudulent Transactions
## Project Overview
This project explores how Federated Machine Learning (FML) can be applied to detect fraudulent financial transactions without compromising user privacy. Traditional machine-learning approaches require collecting all data in a centralized repository, which raises privacy, security, and regulatory concerns—especially in the financial sector.
Federated Learning solves this by training models directly on decentralized data sources (such as multiple banks or institutions) while only sharing model parameters, not raw data. <br><br>This project demonstrates how federated techniques can be used to:<br>
• Identify fraudulent transactions efficiently.<br>
• Preserve data privacy across participating clients.<br>
• Improve model robustness by learning from diverse, distributed datasets.<br>
• Reduce the risk of data breaches and regulatory violations.<br>
<br>The notebooks and scripts included in this project walk through data preprocessing, model design, federated training workflows, and evaluation of the fraud-detection model’s performance in a distributed setting.
## Technologies Used
• Python 3 – Core programming language for all modeling components.<br>
• TensorFlow / TensorFlow Federated (TFF) – Frameworks for building and training federated machine-learning models.<br>
• Scikit-learn – Used for preprocessing, feature engineering, and baseline machine-learning models.<br>
• NumPy & Pandas – For numerical operations, data cleaning, transformation, and dataset handling.<br>
• Matplotlib / Seaborn – For visualizing data distributions, model metrics, and training behavior.<br>
• Jupyter Notebook – Interactive environment for experimentation, analysis, and documentation.<br>
