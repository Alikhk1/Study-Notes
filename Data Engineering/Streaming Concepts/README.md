# Batch Processing

**Batch Processing**: Processing in Groups, Improves performance.

## Delays in Batch Processing
1. Waiting for source data.
2. Time until process begins.
3. Process time.
4. Time until data available for users.

## Scaling
Scaling is the idea of improving performance of our processes.

### 1. Vertical Scaling
- Running on a better computing platform.
- Easiest Kind of Scaling.
- Inherently Limited.
- Can be Expensive.
- Faster I/O, Memory, CPU, RAM.

### 2. Horizontal Scaling
- Splitting Task across multiple systems.
- Adding cores/CPUs.
- Near Linear Performance improvement.
- Complex: Spark/Dask.

---

# Queuing & Streaming

## Event-Based Computing/Processing

### Queuing
- Process Tasks in Order. FIFO. Sometimes referred to as Buffer.
- Can be disconnected from the pipeline.
- Are batches with size 1.

### Streaming
- Doesn't Stop until data is processed.
- Open ended (no specific event or size).
- Is Defined by flow of data and not necessarily the contents.
- Doesn't have a Defined end.
- Streaming Data usually represent events which have been completed.

### Logs
Store event information. (System to export information to multiple clients → Apache Kafka)

---

# Real Time Streaming

**Real Time Streaming**: Definition varies by context.
- Typically a response timeframe.

## Horizontal Scaling Approaches
- Copy Pipelines
- Shorten Pipeline + Add Batch

## Communication Issues
- **Missing**: Sequence Identifier.
- **Delayed**
- **Out of Order**: Sequence Identifier, For Audio/Video → DROP them.
- **Repeated**

---

# Tools & Frameworks for Streaming

## Celery: Distributed Task queue / FIFO
- Used primarily as a job or task queue.
- Real-Time processing of large quantity of messages.
- Functionality for Vertical & Horizontal Scaling.
- **Asynchronous Tasks**:
    - Sending Passwords.
    - Resizing Images.

## Kafka: Distributed Event streaming system
- Send events between producers & consumers.
- Different consumers can handle different aspects such as logging, transformation, etc.
- Handles storing of events.

## Spark Streaming: Component of Apache Spark
- Large amounts of data and in ML scenarios.
- Able to transition from batch to stream.
- Not designed to store or log.
