output "bucket_name" {
  description = "The name of the created Google Storage bucket."
  value       = google_storage_bucket.data_lake_bucket.name
}

output "bigquery_dataset_id" {
  description = "The ID of the created BigQuery dataset."
  value       = google_bigquery_dataset.dataset.dataset_id
}

