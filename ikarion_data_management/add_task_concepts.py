import pymongo
import sys
import pathlib as pl
import json

from ikarion_data_management.config import ProductionConfig


def write_concepts(task_prefix, concept_list):
    client = pymongo.MongoClient(ProductionConfig.MONGO_URI)
    db = client.ikarion
    task_concepts = {
        "task_prefix": task_prefix,
        "concepts": concept_list,
    }
    db.task_concepts.insert_one(task_concepts)

def main():
    folder_path = sys.argv[1]
    concept_folder = pl.Path(folder_path)
    concept_files = list(concept_folder.glob("**/*.json"))
    for c_file in concept_files:
        task_prefix = c_file.stem
        concept_list = json.load(str(c_file))
        write_concepts(task_prefix, concept_list)



if __name__ == "__main__":
    main()