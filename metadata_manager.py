import json
import time


class MetadataManager:
    def save_metadata(self, metadata, output_file=None):
        if output_file is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_file = f"metadata_{timestamp}.json"

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=4)

        return True