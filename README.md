# Streamlit Web App Deployment Guide

### [Diabetes Predictor WebApp ](https://misbah-diabetes-predictor.streamlit.app/)


![image](https://github.com/user-attachments/assets/0df13ac5-bfa5-47fc-86d6-210dc02cd55d)


NOTE : During hosting,Change backward slashes to forward ones in path
Before Deploying on Cloud , remove path and mention only model name like 'trained_model.sav'

**Let python version in which the model was trained be the same as the one in which Spyder script is loaded**
else it will cause a version mismatch when loading the saved .sav model, leading to the InconsistentVersionWarning.

•	Always train and deploy your model in the same environment, 

else  different versions of python in both envireonment will result in different numpy,pandas version etc

## 1. Hosting a Web App on Streamlit
Streamlit makes it easy to create and host interactive web applications using Python. Follow these steps to host your web app:

### Prerequisites:
- Install Python (preferably 3.8+)
- Install Streamlit:
  ```sh
  pip install streamlit
  ```
- Ensure all required libraries (e.g., pandas, scikit-learn) are installed.

### Running Locally:
1. Navigate to your project directory:
   ```sh
   cd path/to/your/project
   ```
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
   Replace `app.py` with your main script file.
3. The app will open in your browser at `http://localhost:8501/`.

## 2. Using Git for Version Control

### Setting Up a Git Repository
1. Initialize a Git repository in your project directory:
   ```sh
   git init
   ```
2. Add a `.gitignore` file to exclude unnecessary files (e.g., `__pycache__/`, `.venv/`).
3. Stage and commit files:
   ```sh
   git add .
   git commit -m "Initial commit"
   ```

### Pushing to GitHub
1. Create a new repository on GitHub.
2. Link the local repository to GitHub:
   ```sh
   git remote add origin https://github.com/your-username/your-repo.git
   ```
3. Push the code:
   ```sh
   git branch -M main
   git push -u origin main
   ```


### Updating Code on GitHub
After making changes:
```sh
  git add .
  git commit -m "Updated features"
  git push origin main
```
![image](https://github.com/user-attachments/assets/f12d9f80-2242-4ab9-bf91-8cd884b9fcaf)

![image](https://github.com/user-attachments/assets/0ff389a6-7556-47be-94ab-ddb0ebf0acf9)


## 3. Deploying the Web App on Streamlit Cloud

open cmd in your repository 

    pip freeze > requirements.txt

this will include the requirements needed for deployment,

not all are required and may cause disturbance so only add (manually create) 

correct veriosns of numpy,pandas,streamlit,scikit learn , check requirements.txt

### Steps to Deploy:
1. Push your code to a public GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click on **New App** and connect your GitHub account.
4. Select your repository and branch (e.g., `main`).
5. Specify the entry-point file (e.g., `app.py`).
6. Click **Deploy**.

🚀

