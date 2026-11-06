# Understanding MongoDB: A Comprehensive Guide


## What is MongoDB?

MongoDB is a popular NoSQL database known for its flexibility, scalability, and ease of use. Unlike traditional relational databases, MongoDB stores data in a flexible, JSON-like format, allowing for more dynamic schemas. In this guide, we'll explore the core concepts, methods, operations, and advanced features you need to know to work effectively with MongoDB.

MongoDB provides a document-oriented data model, meaning data is stored in BSON (Binary JSON) format. It allows for the storage of complex data types, making it highly suitable for modern applications that require flexible and scalable data storage solutions.

## Key Concepts

### Collections

A collection is a group of MongoDB documents. Collections are analogous to tables in relational databases. However, unlike tables, collections do not enforce a schema, meaning each document within a collection can have a different structure.

### Documents

In MongoDB, data is stored as **documents**. A document is a key-value pair similar to JSON objects. Each document can have its own unique structure, but typically, similar documents are grouped together.

Example of a document:

```json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "name": "John Doe",
  "age": 29,
  "address": {
    "street": "123 Main St",
    "city": "New York"
  }
}
```

### Local Installation

- MongoDB can be installed locally, allowing you to host your own MongoDB server.
- This requires managing the server, including upgrades and maintenance.

## Setting Up MongoDB Atlas

1. **Create a Cluster**:
   - Set up a free "Shared Cluster" on MongoDB Atlas.
   - Choose your preferred cloud provider and region.

2. **Configure Access**:
   - Under **Database Access**, create a new user and note the username and password.
   - Under **Network Access**, add your current IP address to allow access from your computer.

## Installing MongoDB Shell (`mongosh`)

1. **Installation**:
   - Follow the official instructions to install `mongosh` on your operating system.
   - Verify the installation by running:
     ```bash
     mongosh --version
     ```
   - Ensure you have the latest version installed.

 ## Connecting to Your Database

1. **Get the Connection String**:
   - In the MongoDB Atlas dashboard, under **Databases**, click the **Connect** button for your Cluster.
   - Choose **Connect with the MongoDB Shell** and copy the provided connection string.

2. **Connect via Terminal**:
   - Paste your connection string into your terminal:
     ```bash
     mongosh "mongodb+srv://cluster0.ex4ht.mongodb.net/myFirstDatabase" --apiVersion 1 --username YOUR_USER_NAME
     ```
   - Enter the password for your database user when prompted.

3. **Success**:
   - You are now connected to your MongoDB database.

# MongoDB Query Operators

MongoDB provides various query operators that allow you to compare and reference document fields in your queries. These operators are categorized into comparison, logical, and evaluation operators.

## Comparison Operators

These operators are used to compare values in your MongoDB queries:

- **$eq**: Matches documents where the value of a field equals the specified value.

  ```javascript
  db.collection.find({ age: { $eq: 30 } })

- **$ne**: Matches documents where the value of a field is not equal to the specified value.

`db.collection.find({ age: { $ne: 30 } })`

- **$gt**: Matches documents where the value of a field is greater than the specified value.

`db.collection.find({ age: { $gt: 30 } })`

- **$gte**: Matches documents where the value of a field is greater than or equal to the specified value.

`db.collection.find({ age: { $gte: 30 } })`

- **$lt**: Matches documents where the value of a field is less than the specified value.

`db.collection.find({ age: { $lt: 30 } })`

- **$lte**: Matches documents where the value of a field is less than or equal to the specified value.

`db.collection.find({ age: { $lte: 30 } })`

- **$in**: Matches documents where the value of a field equals any value in the specified array.

`db.collection.find({ status: { $in: ["A", "B", "C"] } })`

### Logical Operators

These operators allow you to logically compare multiple queries:

- **$and**: Matches documents that satisfy all of the specified queries.

db.collection.find({
  $and: [{ age: { $gte: 30 } }, { status: "A" }]
})

- **$or**: Matches documents that satisfy at least one of the specified queries.

db.collection.find({
    $or: [{ age: { $gte: 30 } }, { status: "A }]
    })

- **$not**: Matches documents that do not match the specified query.

db.collection.find({ $not: { age: { $gte: 30 } } })

- **$nor**: Matches documents that fail to match both of the specified queries.

db.collection.find({
  $nor: [{ age: { $gte: 30 } }, { status: "A" }]
})

### Evaluation Operators

These operators assist in evaluating document fields during queries:

- **$regex**: Matches documents where the value of a field matches a specified regular expression.

db.collection.find({ name: { $regex: "^A" } })

- **$text**: Performs a text search on the content of the fields indexed with a text index.

db.collection.find({ $text: { $search: "search term" } })

- **$where**: Evaluates a JavaScript expression on the server.

db.collection.find({
  $where: function() { return this.age > 30; }
})

### Projection Operators

These operators allow you to specify which fields to include or exclude from the query results:
- **$project**: Excludes or includes specified fields in the query results.

db.collection.find({ $project: { _id: 0, name: 1 } })

- **$elemMatch**: Includes the first element that matches the specified condition.

db.collection.find({ items: { $elemMatch: { price: { $gt: 10
} } } })

- **$slice**: Includes a specified number of elements from an array.

db.collection.find({ items: { $slice: 3 } })

- **$redact**: Redacts (hides) fields in the query results based on a
specified condition.

db.collection.find({ $redact: { $cond: [ { $eq: [ "$age
", 30 ] }, "$$KEEP", "$$PRUNE" ] } })

- **$meta**: Includes metadata about the query results.

db.collection.find({ $meta: "textScore" })

- **$addFields**: Adds new fields to the documents in the query results.

db.collection.find({ $addFields: { newField: { $sum: [ "$field1
", "$field2" ] } } })

- **$set**: Sets the value of a field in the documents in the query results.

db.collection.find({ $set: { field: "value" } })

- **$unset**: Removes a field from the documents in the query results.

db.collection.find({ $unset: { field: "" } })

- **$push**: Adds a value to an array in the documents in the query results.

db.collection.find({ $push: { field: "value" } })

- **$addToSet**: Adds a value to a set in the documents in the query results.

db.collection.find({ $addToSet: { field: "value" } })

- **$pop**: Removes the first or last element from an array in the documents in the query
results.

db.collection.find({ $pop: { field: 1 } })

- **$pull**: Removes all occurrences of a value from an array in the documents in the query
results.

db.collection.find({ $pull: { field: "value" } })

- **$pullAll**: Removes all occurrences of specified values from an array in the documents in
the query results.

db.collection.find({ $pullAll: { field: ["value1", "value2"] }
})

- **$pullAllFrom**: Removes all occurrences of specified values from an array in the documents in
the query results.

db.collection.find({ $pullAllFrom: { field: "array", values: ["value1
", "value2"] } })

- **$rename**: Renames a field in the documents in the query results.

db.collection.find({ $rename: { field: "newField" } })

- **$type**: Includes only documents where the specified field matches the specified type.

db.collection.find({ field: { $type: "string" } })

- **$mod**: Includes only documents where the specified field matches the specified modulo
condition.

db.collection.find({ field: { $mod: [ 1, 2 ] } })

### CRUD Operations

### Create

The insertOne() and insertMany() methods are used to add documents to a collection.

* insertOne(): Inserts a single document into a collection.

```
db.users.insertOne({
  name: "John Doe",
  age: 29,
  address: {
    street: "123 Main St",
    city: "New York"
  }
});

```

* insertMany(): Inserts multiple documents into a collection

db.users.insertMany([
  { name: "Alice", age: 24 },
  { name: "Bob", age: 30 }
]);

### Read

* find(): Retrieves documents that match the query criteria. If no criteria are specified, all documents in the collection are returned.

db.users.find({ age: { $gt: 25 } });

* findOne(): Retrieves the first document that matches the query criteria.

db.users.findOne({ name: "John Doe" });

### Update

* updateOne(): Updates the first document that matches the query criteria.

db.users.updateOne(
  { name: "John Doe" },
  { $set: { age: 30 } }
);

* updateMany(): Updates all documents that match the query criteria.

db.users.updateMany(
  { age: { $lt: 25 } },
  { $set: { status: "inactive" } }
);

* replaceOne(): Replaces the entire document that matches the query criteria.

db.users.replaceOne(
  { name: "John Doe" },
  { name: "John Smith", age: 30 }
);

### Delete

The deleteOne() and deleteMany() methods are used to remove documents from a collection.

* deleteOne(): Deletes the first document that matches the query criteria.

db.users.deleteOne({ name: "John Doe" });

* deleteMany(): Deletes all documents that match the query criteria.

db.users.deleteMany({ age: { $gt: 30 } });

### Indexing

Indexes are used to improve the performance of queries by allowing MongoDB to quickly locate data.Without indexes, MongoDB must scan every document in a collection to find the ones that match the query criteria.

Here are some common indexing methods:

* createIndex(): Creates a new index on a field or a set of fields.

db.users.createIndex({ name: 1 });

db.users.createIndex({ age: 1, name: 1 });

Here, 1 indicates ascending order, and -1 would indicate descending order.

* dropIndex(): Drops an existing index.

# MongoDB Aggregation Methods

Aggregation is a powerful feature in MongoDB that allows you to perform complex data processing and analysis on large datasets. Here are some common aggregation methods with examples:

## Aggregation Methods

- **`$match`**: Filters the documents to include only those that match the specified criteria.

    ```javascript
    db.orders.aggregate([
      { $match: { status: "shipped" } }
    ]);
    ```

- **`$project`**: Selects the fields to include in the output. You can also rename fields and add computed fields.

    ```javascript
    db.orders.aggregate([
      { $project: { item: 1, quantity: 1, totalPrice: { $multiply: ["$quantity", "$price"] } } }
    ]);
    ```

- **`$group`**: Groups the documents by one or more fields and applies an aggregation operation to each group.

    ```javascript
    db.orders.aggregate([
      { $group: { _id: "$customerId", total: { $sum: "$amount" } } }
    ]);
    ```

- **`$sort`**: Sorts the documents in ascending or descending order.

    ```javascript
    db.orders.aggregate([
      { $sort: { orderDate: -1 } }
    ]);
    ```

- **`$limit`**: Limits the number of documents in the output.

    ```javascript
    db.orders.aggregate([
      { $limit: 5 }
    ]);
    ```

- **`$skip`**: Skips a specified number of documents in the output.

    ```javascript
    db.orders.aggregate([
      { $skip: 10 }
    ]);
    ```

- **`$unwind`**: Unwinds an array field into separate documents.

    ```javascript
    db.orders.aggregate([
      { $unwind: "$items" }
    ]);
    ```

- **`$lookup`**: Performs a left outer join with another collection.

    ```javascript
    db.orders.aggregate([
      {
        $lookup: {
          from: "products",
          localField: "productId",
          foreignField: "_id",
          as: "productDetails"
        }
      }
    ]);
    ```

- **`$out`**: Writes the output to a new collection.

    ```javascript
    db.orders.aggregate([
      { $match: { status: "shipped" } },
      { $out: "shippedOrders" }
    ]);
    ```

- **`$merge`**: Merges the output with an existing collection.

    ```javascript
    db.orders.aggregate([
      { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
      { $merge: { into: "customerTotals" } }
    ]);
    ```

- **`$replaceRoot`**: Replaces the root of the document with a new value.

    ```javascript
    db.orders.aggregate([
      {
        $replaceRoot: { newRoot: { item: "$item", totalAmount: "$amount" } }
      }
    ]);
    ```

- **`$addFields`**: Adds new fields to the document.

    ```javascript
    db.orders.aggregate([
      { $addFields: { totalPrice: { $multiply: ["$quantity", "$price"] } } }
    ]);
    ```

- **`$set`**: Sets the value of a field in the document. This is similar to `$addFields`, but `$set` is a more recent operator.

    ```javascript
    db.orders.aggregate([
      { $set: { totalPrice: { $multiply: ["$quantity", "$price"] } } }
    ]);
    ```

- **`$unset`**: Unsets a field in the document.

    ```javascript
    db.orders.aggregate([
      { $unset: "temporaryField" }
    ]);
    ```

## Example

Here is an example that combines several aggregation methods:

```javascript
db.orders.aggregate([
  { $match: { status: "shipped" } },        // Stage 1: Filter documents with status "shipped"
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },  // Stage 2: Group by customerId and sum the amount
  { $sort: { total: -1 } },                // Stage 3: Sort by total amount in descending order
  { $limit: 10 }                           // Stage 4: Limit the output to the top 10 customers
]);
```

### MongoDB Schema Validation

MongoDB is known for its flexible schema, meaning documents within a collection can have different structures. However, you can enforce a certain structure using schema validation. This ensures that documents conform to a defined schema.

## Schema Validation with JSON Schema

MongoDB supports schema validation using JSON Schema. The `$jsonSchema` operator allows you to specify rules for document structure.

## Example

Here’s how you can create a collection with schema validation:

```javascript
db.createCollection("posts", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["title", "body"],
      properties: {
        title: {
          bsonType: "string",
          description: "Title of post - Required."
        },
        body: {
          bsonType: "string",
          description: "Body of post - Required."
        },
        category: {
          bsonType: "string",
          description: "Category of post - Optional."
        },
        likes: {
          bsonType: "int",
          description: "Post like count. Must be an integer - Optional."
        },
        tags: {
          bsonType: ["string"],
          description: "Must be an array of strings - Optional."
        },
        date: {
          bsonType: "date",
          description: "Must be a date - Optional."
        }
      }
    }
  }
});
```

# MongoDB Advanced Concepts

## MongoDB Replication

Replication in MongoDB ensures that your data is duplicated across multiple servers to provide high availability and redundancy. MongoDB replication is achieved through replica sets.

### Replica Sets

- **Definition**: A replica set is a group of MongoDB servers that maintain the same data set. It consists of a primary server and one or more secondary servers.
- **Primary Server**: The primary server receives all write operations and replicates the changes to the secondary servers.
- **Secondary Servers**: Secondary servers replicate the data from the primary and can serve read operations. They can be promoted to primary if the current primary fails.

**Example of Initiating a Replica Set**:

```javascript
rs.initiate({
  _id: "myReplicaSet",
  members: [
    { _id: 0, host: "localhost:27017" },
    { _id: 1, host: "localhost:27018" },
    { _id: 2, host: "localhost:27019" }
  ]
});
```

# MongoDB Advanced Concepts

## MongoDB Sharding

Sharding is a method for distributing data across multiple servers to handle large amounts of data and high throughput operations.

### Shard Key

- **Definition**: A shard key is a field or set of fields that MongoDB uses to distribute documents across shards.
- **Choosing a Shard Key**: It should be chosen carefully to ensure even data distribution and to prevent hotspots.

**Example of Sharding a Collection**:

1. **Enable Sharding on the Database**:

    ```javascript
    sh.enableSharding("myDatabase");
    ```

2. **Shard the Collection**:

    ```javascript
    sh.shardCollection("myDatabase.myCollection", { shardKey: 1 });
    ```

## MongoDB Transactions

Transactions allow you to execute multiple operations in a single, atomic operation, ensuring data consistency.

### Multi-Document Transactions

- **Definition**: MongoDB supports multi-document transactions for replica sets and sharded clusters.
- **Usage**: Transactions are useful for operations that need to be executed atomically.

**Example of Using Transactions**:

```javascript
const session = await client.startSession();
session.startTransaction();

try {
  await db.collection("orders").insertOne({ orderId: 1 }, { session });
  await db.collection("inventory").updateOne({ itemId: 1 }, { $inc: { stock: -1 } }, { session });
  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
} finally {
  session.endSession();
}
```
### MongoDB Backup and Restore


MongoDB provides several methods for backing up and restoring data.

- **mongodump**: A command-line tool for backing up MongoDB data.

mongodump --db myDatabase --out /path/to/backup


- **mongorestore**: A command-line tool for restoring MongoDB data.

mongorestore --db myDatabase /path/to/backup/myDatabase


### Ref

- https://www.w3schools.com/mongodb/index.php