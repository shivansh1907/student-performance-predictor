import sys

from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            train_data,test_data=DataIngestion().initiate_data_ingestion()
            train_arr,test_arr,_=DataTransformation().initiate_data_transformation(train_data,test_data)
            return ModelTrainer().initiate_model_trainer(train_arr,test_arr)

        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    best_model_name,r2_square=TrainPipeline().run()
    print(f"Best model: {best_model_name}, r2 score on test set: {r2_square}")
