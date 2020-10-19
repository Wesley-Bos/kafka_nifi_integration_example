# kafka_nifi_integration_example
A simple example on how to use Kafka and Nifi. View my [Medium post](https://medium.com/@wesleybos99/kafka-and-nifi-integration-d0431b540f37?source=friends_link&sk=05684bcce29dfe47a817071d4bff6b96) for a more comprehensive explanation.

**To-do:**
* Write Readme.
* Add configuration of the processors in Nifi.

1. Execute the build_project.sh script
2. Wait for Nifi to set up. Visit http://localhost:8080/nifi/.
3. Upload the template 'nifi_kafka_template.xml'
4. Drag in the template to the workspace.
5. Ctrl+a and press Start.
6. Execute the python scripts (Producer and Consumers)
7. This project can be **removed** by executing the remove_project.sh script or **stopped** by running the stop_project.sh script.

The final result will look like this:
![final result](https://github.com/Wesley-Bos/kafka_nifi_integration_example/blob/main/working_producers_consumers.png)

***
**NOTE:** currently there is an issue with the format at which Nifi publishes the message to Kafka. If you look at the message in the [Control Center](http://localhost:9021/) they look fine. However, as you can see in the screenshot there are additional characters added, this isn't JSON anymore.

*This will be looked into later. I'm pretty sure it has to do with the syntax used by the OnRouteContent processor.*
***
