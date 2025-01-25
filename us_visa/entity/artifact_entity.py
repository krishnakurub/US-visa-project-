from dataclasses import dataclass 

@dataclass
class DataIngestionArtifact:    ## below two files neeed to recive n next componet ie validation
    trained_file_path:str
    test_file_path:str
