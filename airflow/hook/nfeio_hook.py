from airflow.providers.http.hooks.http import HttpHook
import requests

class NfeiotHook(HttpHook):
    def __init__(self, end_time,query, conn_id=None):
        self.end_time = end_time
        self.query = query
        self.conn_id = conn_id or "nfeio_default"
        super().__init__(http_conn_id=self.conn_id)
    
    def create_url(self):
        query = ""

        url_raw = f""

        return url_raw

    def connect_to_endpoint(self, url, session):
        request = requests.Request('GET', url)
        prep = session.prepare_request(request)
        self.log.info(f"URL: {url}")
        return self.run_and_check(session, prep, {})
        ...
