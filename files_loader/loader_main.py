from load_path_from_files_dir import FilesLoader
from cretae_metadata_to_file import MetadataCreator
from kafka_pub import Publisher

def preprocessing():
    loader = FilesLoader()
    metadata_creator = MetadataCreator()
    publisher = Publisher()

    files_list = loader.load_files()

    for file in files_list:
        metadata = metadata_creator.create_metadata(file)
        publisher.publish_file_metadata(metadata)

preprocessing()

