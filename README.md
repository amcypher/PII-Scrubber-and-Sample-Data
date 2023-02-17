# Scrubba.py
Scrubba.py example of a script created to demenstrate how to parse pii out of an a mock endpoint(github repo) utilizing python3.

# To run.
python3 scrubba.py

# Expected print out.

```dict_keys(['data_info', 'pii_instances', 'processing_time'])
{'data_info': [{'pii_type': 'passport'},
               {'severity': 'high'},
               {'file_format': 'pdf'},
               {'archive_name': 'passport 2022.tar.gz'},
               {'file_name': 'bob_p_scanned.pdf'},
               {'ingest_source': 's3://backups/bob/2022/12/Documents/'}],
 'pii_instances': [{'name': 'bob foo-bar'},
                   {'date_of_birth': 'xxxx/xx/xx'},
                   {'ssn': 'xxx-xx-xxxx'},
                   {'personal_photo': True},
                   {'home_address': '1 Liberty Plaza, New York City, NY'},
                   {'sex': 'M'},
                   {'marital_status': 'married'},
                   {'personal_signature': True}],
 'processing_time': '80.6 ms'}```
