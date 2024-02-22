# Exposición del caso

En este escenario, se lleva a cabo una entrada de datos procedentes de un conjunto de datos que refleja las diversas transacciones ocurridas en una empresa. La información detallada sobre las transacciones incluye la cantidad y tipo de productos, el precio por unidad, el precio total, así como características del cliente como edad y género, y datos específicos de la transacción.

La operación consiste en recibir en tiempo real los datos provenientes de un productor y depositarlos en el topic "ventas". Todos estos datos recibidos son consumidos por un script de consumidor (consumer.py), y posteriormente, a través de KSQL, se realiza una consulta sobre el topic "ventas" para identificar aquellas transacciones que generan mayores beneficios.

Se busca identificar las transacciones más beneficiosas para detectar las tendencias que está siguiendo el mercado así como para tomar decisiones informadas basadas en datos concretos y adaptarse ágilmente a las dinámicas del mercado. Además así se podrá optimizar mejor los precios y ofertas.
