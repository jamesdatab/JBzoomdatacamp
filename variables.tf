

variable "credentials" {
    description = "My credentials"
    default = "E:\\dataengzoomcamp\\week1mine\\terraformkey\\datacampproj-1197601b2746.json"
}

variable "project" {
    description = "Project"
    default = "datacampproj"
}


variable "location" {
    description = "Project_location"
    default = "US"
}

variable "region" {
    description = "Project_location"
    default = "us-central1"
}

variable "bq_dataset_name" {
    description = "My_bigquery_dataset_name"
    default = "example_dataset"
}

variable "gcs_bucket_name" {
    description = "My_storage_bucket_name"
    default = "datacampproj_terra_bucket"
}

variable "gcs_storage_class" {
    description = "Bucket_storage_Class"
    default = "STANDARD"
}