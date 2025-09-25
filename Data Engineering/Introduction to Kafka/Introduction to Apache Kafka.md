# Apache Kafka

Apache Kafka is an open-source distributed event-streaming platform. It is designed for high-throughput, fault-tolerant, real-time data pipelines and event-driven applications.

**Event-Streaming** means obtaining information from various sources, storing and distributing to clients.

## Common Uses
1. Ecommerce
2. Order Tracking
3. Ride Share / Food Delivery
4. Sensor data networks
5. Cybersecurity: Spam monitoring

---

# Core Concepts

- **Producer (Publishers)**: Sends records (messages) to Kafka topics.
- **Topic**: Category or feed name to which records are published.
- **Partition**: Subdivision of a topic for parallelism and scalability.
- **Consumer (Subscribers)**: Reads records from topics.
- **Broker**: Kafka server that stores and serves data.
- **Cluster**: Group of brokers working together.
- **Zookeeper** (older versions): Manages cluster metadata; now replaced by KRaft mode in newer versions. Provides necessary services to run distributed apps.
    - `config/zookeeper.properties`

---

# Commands

## Required Command Options
1. `--bootstrap-server`: Specifies which server to use
    - `--bootstrap-server localhost:9092`
2. `--topic`
    - `--topic phishing-sites`

## Topics
- **Find Existing Topics**
    - `bin/kafka-topics.sh --list --bootstrap-server localhost:9092`
- **Create Topics**
    - `bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic <server> --create --replication-factor 3 --partitions 3`
    - `--replication-factor <x>`: How many copies of topics within the cluster.
    - `--partitions <x>`
    - `--describe`: Gives details of kafka topic configuration.
- **Delete Topics**
    - `bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic <server> --delete`

## Write to Topic (2 ways)
- `bin/kafka-console-producer.sh --topic topic-name --bootstrap-server localhost:9092`
- `echo "This is a message" | bin/kafka-console-producer.sh --topic topic-name --bootstrap-server localhost:9092`

## Read from Topic
- `bin/kafka-console-consumer.sh --topic topic-name --from-beginning --bootstrap-server localhost:9092`
- `bin/kafka-console-consumer.sh --topic topic-name --max-messages <number> --bootstrap-server localhost:9092`

---

# Kafka Components

## Kafka Server
- Cluster of one or more computers.
- Stores Data.
- Manages Communications.
- Can integrate with other systems.
- Server acts as a "Broker". Handles communication between consumers & producers.
- **Broker Count**: `/home/repl/check_broker.sh`
- **Primary Server Config**: `config/server.properties`

## Kafka Cluster
- Started in 2 steps:
    1. `bin/zookeeper-server-start.sh config/zookeeper.properties`
    2. `bin/kafka-server-start.sh config/server.properties`
- **Stop Server**:
    - `bin/kafka-server-stop.sh`
    - `bin/zookeeper-server-stop.sh`
    - *Reverse order of shutdown*

## Kafka Topics
- Logical Grouping of events. Where each event refers to the same kind of thing.
- Similar to a table in relational database.
- Like an Event log.
- Messages are immutable. Can read or written but not changed.

---

# Kafka Troubleshooting

- Topic does not need to exist for producer to write to. It just creates that new topic.
- Networking issues can cause problems with kafka communications.
    - Best way to identify this problem is to look at output of commands.
    - Check Firewall.
    - Verify correct port/IP.
- Use `--help` for command assistance.