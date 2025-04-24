# 📦 CSV to BigQuery Data Pipeline (GCP + Kestra + Airflow)

## 📝 Project Summary
This project demonstrates a basic data pipeline setup using Infrastructure as Code with Terraform, Dockerized orchestration tools (Airflow and Kestra), and Google Cloud Platform services. The goal is to extract a CSV file from an external link, store it in Google Cloud Storage (GCS), and then load it into BigQuery.

---

## ⚙️ Tech Stack
- **Infrastructure**: Terraform (for provisioning GCP services)
- **Orchestration & Workflow**:
  - Apache Airflow (Docker) – for downloading CSV file
  - Kestra (Docker) – for loading CSV into BigQuery
- **Data Warehouse**: Google BigQuery
- **Storage**: Google Cloud Storage (GCS)
- **Scripting**: Python
- **Other Tools**: Docker, YAML (for Kestra workflows)

---

## 🔄 Pipeline Overview
1. **Airflow Task**: Downloads a CSV file from a public URL and uploads it to GCS.
   - Script: `csv2gcs.py`

2. **Kestra Flow**: Loads the CSV file from GCS into BigQuery using a YAML-based workflow.
   - Workflow: `load_newsletter_csv.yaml`

3. **Final Destination**: The data ends up in a specified table in Google BigQuery.


## 🚀 How to Run This Project Locally

### 📦 Prerequisites
- Install [Docker](https://www.docker.com/)
- Install [Terraform](https://developer.hashicorp.com/terraform/install)
- A Google Cloud account
- A GCP service account key JSON file

### 🔧 Setup Steps
1. **Clone this repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Set up your GCP credentials**
Place your GCP service account key JSON file in the project directory and set this environment variable:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="your-key-file.json"
```

3. **Provision infrastructure with Terraform**
```bash
cd terraform
terraform init
terraform apply
```

4. **Start Docker containers**
Make sure your `docker-compose.yaml` includes services for Airflow and Kestra, then:
```bash
docker-compose up -d
```

5. **Run the Airflow DAG** to download the CSV file:
- Go to `http://localhost:8080` (Airflow UI)
- Trigger `csv2gcs` DAG manually

6. **Run the Kestra Flow** to load data to BigQuery:
- Go to `http://localhost:8082` (Kestra UI)
- Trigger the `load_newsletter_csv` flow

---

## 🧪 Testing
Basic testing done through manual execution of Airflow DAG and Kestra flow.

---

## 🔮 Future Enhancements
- Automate the pipeline to trigger on new file uploads in GCS.
- Add dbt for data modeling and transformation.
- Build a Looker Studio or Power BI dashboard.
- Include local run instructions with `.env`, `requirements.txt`, and Docker setup.

---

## 🧠 Learnings
- Hands-on setup of Airflow and Kestra in Docker environments.
- Orchestration of data flow from ingestion to BigQuery.
- YAML-based workflow configuration using Kestra.

---

## 📌 Status
✅ Initial version completed  
🔜 Future updates will include automation and visualization components.

---

Feel free to clone the repo and try running it. Suggestions and contributions are welcome!

