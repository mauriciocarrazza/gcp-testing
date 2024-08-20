import schemas

LOOKUP = {
    "customerio_dsi_active_subscriber_emails": {
        "schema": schemas.DSI_ACTIVE_EMAIL_SCHEMA,
        "load_table": "dsi_active_subscriber_emails",
        "merge": "dsi_merge_active_subscribers_table",
        "source": "DSI",
        "separator": "|",
        "quote_character": "",
    }
}