variable "project" {
  description = "The GCP project ID."
  type        = string
  default     = "de-project-batch"
}

variable "region" {
  description = "The GCP region."
  type        = string
  default     = "us-central1"
}

variable "credentials_file" {
  description = "Path to the GCP credentials JSON file."
  type        = string
  default     = "./keys/my_creds.json"
}

variable "bucket_name" {
  description = "The name of the Google Storage bucket. Must be globally unique."
  type        = string
  default     = "bucketforbatch"
}

variable "dataset_id" {
  description = "The BigQuery dataset ID."
  type        = string
  default     = "newsletter"
}

