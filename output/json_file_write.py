from datetime import datetime as dt
from json import dumps


class JSONSerializer:
    @classmethod
    def to_file(self, payload, dir_path, file_name=None, **kwargs):
        logger = kwargs.get("logger")

        if file_name is None:
            now = dt.now().strftime("%Y-%m-%dT%H:%M:%S")
            file_name = f"varys_{now}.json"

        json_payload = dumps(payload, indent=4)

        with open(f"{dir_path}/{file_name}", "w") as outfile:
            outfile.write(json_payload)

        logger.info("")
