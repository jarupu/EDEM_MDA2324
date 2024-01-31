![Logo](https://n3m5z7t4.rocketcdn.me/wp-content/plugins/edem-shortcodes/public/img/logo-Edem.png)

# Serverless Data Processing in GCP: Dataflow
EDEM 2024

- Professor: [Javi Briones](https://github.com/jabrio)

#### Case description

<img src="https://logos-world.net/wp-content/uploads/2023/02/NYC-Symbol.png" alt="WFM" width="130" height="70"/>


The New York City Hall, of which we are part of its Data team, has identified a significant increase in the number of traffic accidents in the Manhattan district due to vehicle speed. To address this issue, it has been decided to implement cameras equipped with Artificial Intelligence to monitor the speed of vehicles in specific sections. 

#### Business challenges

- Each camera will be set up in a particular section and must calculate the **average speed** of each vehicle.
- The average speed in the section should not exceed **25 miles** per hour (40 km/h).
- An **image** must be captured, the license plate number obtained, and the analyzed photo of all fined vehicles stored.

#### Case Requirements

- The data captured by different cameras should be sent to the **provided topic** during class for the proper visualization of the data.

- The data should also be stored in the **Data Warehouse** for subsequent analysis by the Analyst team. **[Homework Assignment]**.

- The notification message for fines should now include the **URL of the Google Cloud Storage Bucket where the image of the vehicle is stored**, to verify that the model has correctly captured the license plate text. **[Homework Assignment (optional)]**.

#### Deployment instructions

- Check [here](https://github.com/jabrio/Serverless_EDEM_2024) for the necessary steps to deploy this architecture.
- [Code](https://github.com/jabrio/Serverless_EDEM_2024/tree/main/02_Code)
