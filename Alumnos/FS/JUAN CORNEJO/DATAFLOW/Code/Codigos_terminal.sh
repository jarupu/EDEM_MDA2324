python EDEM_Dataflow_Streaming_Pipeline.py \
    --project_id entregables-edem \
    --input_subscription projects/entregables-edem/subscriptions/recepcion_datos-sub \
    --output_topic projects/entregables-edem/topics/salida_datos \
    --radar_id 17 \
    --cars_api https://europe-west1-long-flame-410209.cloudfunctions.net/car-license-plates-api \
    --runner DataflowRunner \
    --job_name prueba-entregable \
    --region europe-southwest1 \
    --temp_location gs://bucket_entregables/tmp \
    --staging_location gs://bucket_entregables/stg \
    --requirements_file requirements.txt



python generator.py \
    --project_id entregables-edem \
    --topic_name recepcion_datos \
    --initial_coordinates "39.47174511011894,-0.38791931453863654" \
    --final_coordinates "39.47223703396268,-0.38666755323885205"
