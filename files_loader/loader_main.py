from load_path_from_files_dir import FilesLoader
from cretae_metadata_to_file import MetadataCreator
from kafka_pub import Publisher
from logger_dir.logger import Logger

logger = Logger.get_logger()

def preprocessing():
    logger.info('The muezzin system started.')

    loader = FilesLoader()
    metadata_creator = MetadataCreator()
    publisher = Publisher()

    files_list = loader.load_files()

    for file in files_list:
        metadata = metadata_creator.create_metadata(file)
        publisher.publish_file_metadata(metadata)

preprocessing()

