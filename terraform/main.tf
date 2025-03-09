resource "google_storage_bucket" "data_lake_bucket" {
  name                        = var.bucket_name
  location                    = "US"
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30
    }
  }

  force_destroy = true
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.dataset_id
  project    = var.project
  location   = "US"
}

