# Scrubba.py

Scrubba.py is a script created to demonstrate how to parse PII (Personally Identifiable Information) out of a mock endpoint (e.g., a GitHub repository) utilizing Python 3.

## How to Run

```sh
python3 scrubba.py

dict_keys(['data_info', 'pii_instances', 'processing_time', 'processing_details'])
{
    "data_info": {
        "pii_type": "passport",
        "severity": "high",
        "file_format": "pdf",
        "archive_name": "passport_2022.tar.gz",
        "file_name": "bob_p_scanned.pdf",
        "ingest_source": "s3://backups/bob/2022/12/Documents/",
        "file_size": "2.5 MB",
        "created_date": "2022-12-15T10:00:00Z",
        "last_modified_date": "2023-01-10T15:30:00Z"
    },
    "pii_instances": {
        "full_name": "Bob Foo-Bar",
        "date_of_birth": "1975-08-15",
        "ssn": "123-45-6789",
        "personal_photo": true,
        "home_address": "1 Liberty Plaza, New York City, NY",
        "sex": "M",
        "marital_status": "married",
        "personal_signature": true,
        "passport_number": "A12345678",
        "nationality": "US"
    },
    "processing_time": "80.6 ms",
    "processing_details": {
        "timestamp": "2024-05-16T12:34:56Z",
        "processor_id": "proc-78901",
        "processing_status": "completed",
        "checksum": "d41d8cd98f00b204e9800998ecf8427e",
        "encryption_status": "encrypted"
    }
}
