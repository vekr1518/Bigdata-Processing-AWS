from pyspark.sql import SparkSession
from pyspark.sql.functions import col

#S3 source and target location
S3_SOURCE_PATH = 's3://emr-bucket-vk/data-source/'
S3_OUTPUT_PATH = 's3://emr-bucket-vk/data-output/'

def main():
    spark = SparkSession.builder.appName('vkdemoapp').getOrCreate() #Initiate Spark Session
    data = spark.read.csv(S3_SOURCE_PATH,header=True)
    print('Total number of records in the source data: %s' % data.count())
    selected_data = data.where((col('review/score') > 4) & (col('Price') <= 10))
    print("Books with rating greater than 4 and below 10 dollars:  %s" % selected_data.count())
    selected_data.write.mode('overwrite').parquet(S3_OUTPUT_PATH)
    
    
if __name__ == '__main__':
    main()
    
    
    