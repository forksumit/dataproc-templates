# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Common
PROJECT_ID_PROP = "project.id"

# Data
CSV_HEADER = "header"
CSV_INFER_SCHEMA = "inferSchema"
FORMAT_JSON = "json"
FORMAT_CSV = "csv"
FORMAT_AVRO = "avro"
FORMAT_PRQT = "parquet"
FORMAT_AVRO_EXTD = "com.databricks.spark.avro"
FORMAT_BIGQUERY = "com.google.cloud.spark.bigquery"
TABLE = "table"

# Output mode
OUTPUT_MODE_OVERWRITE = "overwrite"
OUTPUT_MODE_APPEND = "append"
OUTPUT_MODE_IGNORE = "ignore"
OUTPUT_MODE_ERRORIFEXISTS = "errorifexists"

# GCS to BigQuery
GCS_BQ_INPUT_LOCATION = "gcs.bigquery.input.location"
GCS_BQ_INPUT_FORMAT = "gcs.bigquery.input.format"
GCS_BQ_OUTPUT_DATASET = "gcs.bigquery.output.dataset"
GCS_BQ_OUTPUT_TABLE = "gcs.bigquery.output.table"
GCS_BQ_OUTPUT_MODE = "gcs.bigquery.output.mode"
GCS_BQ_TEMP_BUCKET = "temporaryGcsBucket"
GCS_BQ_LD_TEMP_BUCKET_NAME = "gcs.bigquery.temp.bucket.name"

# BigQuery to GCS
BQ_GCS_INPUT_TABLE = "bigquery.gcs.input.table"
BQ_GCS_OUTPUT_FORMAT = "bigquery.gcs.output.format"
BQ_GCS_OUTPUT_MODE = "bigquery.gcs.output.mode"
BQ_GCS_OUTPUT_LOCATION = "bigquery.gcs.output.location"