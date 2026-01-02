import os
from pyspark.sql import SparkSession
from app.transform import process_truck_traffic

def main():
    input_path = os.environ.get("INPUT_PATH", "/data/input_truck_traffic.csv")
    output_path = os.environ.get("OUTPUT_PATH", "/data/output")

    spark = SparkSession.builder \
        .appName("pyspark-truck-traffic") \
        .master("local[*]") \
        .getOrCreate()

    print(f"Leyendo datos desde {input_path}")
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_path)

    print("Procesando tráfico de camiones...")
    out_df = process_truck_traffic(df)

    print(f"Escribiendo resultados en {output_path}")
    out_df.write.mode("overwrite").parquet(output_path)

    spark.stop()
    print("Finalizado")
    
if __name__ == "__main__":
    main()