from google.cloud import bigquery

# flake8: noqa
DSI_ACTIVE_EMAIL_SCHEMA = [
    bigquery.SchemaField("SITE_CODE", "INTEGER"),
    bigquery.SchemaField("PRODUCT_CODE", "STRING"),
    bigquery.SchemaField("DOMAIN", "STRING"),
    bigquery.SchemaField("EMAIL", "STRING"),
    bigquery.SchemaField("SUBSCRIBER_ACCOUNT_ID", "INTEGER"),
    bigquery.SchemaField("LIST_SUBSCRIBERS", "STRING"),
    bigquery.SchemaField("FIRST_NAME", "STRING"),
    bigquery.SchemaField("LAST_NAME", "STRING"),
    bigquery.SchemaField("ADDRESS_LINE1", "STRING"),
    bigquery.SchemaField("ADDRESS_LINE2", "STRING"),
    bigquery.SchemaField("CITY", "STRING"),
    bigquery.SchemaField("STATE", "STRING"),
    bigquery.SchemaField("POSTAL_CODE", "STRING"),
    bigquery.SchemaField("COUNTRY", "STRING"),
    bigquery.SchemaField("MARKET", "STRING"),
    bigquery.SchemaField("SUBSCRIBER_STATUS", "STRING"),
    bigquery.SchemaField("SUBSCRIBER_SINCE_DATE", "DATE"),
    bigquery.SchemaField("SUBSCRIPTION_END_DATE", "DATE"),
    bigquery.SchemaField("SUBSCRIBER_TYPE", "STRING"),
    bigquery.SchemaField("EXPORT_DATE", "DATE"),
    bigquery.SchemaField("CIRC_SYSTEM", "STRING"),
]