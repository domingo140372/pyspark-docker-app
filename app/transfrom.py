from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit, when

def process_truck_traffic(df: DataFrame) -> DataFrame:
    """
    Transformación ejemplo para tráfico de camiones:
    - Filtra registros con trucks_count nulos o negativos
    - Convierte trucks_count a integer y avg_weight_tons a float
    - Crea categorías de carga (light, medium, heavy) según avg_weight_tons
    - Calcula un campo estimated_total_tonnage = trucks_count * avg_weight_tons
    - Devuelve columnas: timestamp, state, highway, location_id, trucks_count (int),
      avg_weight_tons (float), load_category, estimated_total_tonnage
    """
    df2 = (
        df
        .filter(col("trucks_count").isNotNull())
        .withColumn("trucks_count", col("trucks_count").cast("int"))
        .withColumn("avg_weight_tons", col("avg_weight_tons").cast("double"))
        .filter(col("trucks_count") > 0)
        .withColumn("load_category",
            when(col("avg_weight_tons") < 5, lit("light"))
            .when((col("avg_weight_tons") >= 5) & (col("avg_weight_tons") < 15), lit("medium"))
            .otherwise(lit("heavy"))
        )
        .withColumn("estimated_total_tonnage", col("trucks_count") * col("avg_weight_tons"))
        .select("timestamp", "state", "highway", "location_id", "trucks_count", "avg_weight_tons", "load_category", "estimated_total_tonnage")
    )
    return df2