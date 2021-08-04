## Notification System 
Send Notification to customers via SMS or Email or Push notification.
we have two services that communicate vai Rabbit mq message broker
* First service called `notification-producer` that  insert data in DB and send message to RabbitMQ.
* Second service called `notification-consumer` that listens to data in RabitMq and list All push notifications per user.

`
## Installation
1 - go to `notification-producer`  folder then run
* `docker network create rabbitmq_network`
* `docker-compose up -d`

2- go to `notification-consumer` folder and then run
* `docker-compose up -d`



## Documentation
1- notification-producer 
  * http://localhost:5000/doc

2- notification-producer 
 * http://localhost:4000/doc



## Architecture

* If you want  to add a new  provider you can go to
  `project/strategies/` and add new class extends Startegy class  and  register it in the factory `providerFactory` .
  

  

## Design Pattern Used

1- `Abstract Factory` pattern to encapsulate creation of the provider object  from the business logic

2- `Reposiotory` pattern  to get data form datasource (Apis).

3- `Service` pattern I added all business logic in separate classes.

4- `strategy` pattern for each provider that send notification 



<br>


## Testing
From  producer docker image
* `docker-compose exec producer bash`


Run

    pytest

From  producer docker image
* `docker-compose exec consumer bash`


Run

    pytest



## Tools
* Python3.8
* Rabbitmq
* redis







    
