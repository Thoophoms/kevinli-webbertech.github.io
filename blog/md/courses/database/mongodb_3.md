### MongoDB Programming

## Outline

* MongoDB Query Operators
* MongoDB Update Operators
* Aggregation Methods
* Schema Validation

## MongoDB Query Operators

There are many query operators that can be used to compare and reference document fields.

## Comparison

The following operators can be used in queries to compare values:

`$eq`: Values are equal

`$ne`: Values are not equal

`$gt`: Value is greater than another value

`$gte`: Value is greater than or equal to another value

`$lt`: Value is less than another value

`$lte`: Value is less than or equal to another value

`$in`: Value is matched within an array

- **$eq**: Matches documents where the value of a field is equal to the specified value.

`db.collection.find({ age: { $eq: 30 } })`

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

### Logical
The following operators can logically compare multiple queries.

`$and`: Returns documents where both queries match

`$or`: Returns documents where either query matches

`$nor`: Returns documents where both queries fail to match

`$not`: Returns documents where the query does not match

- **$and**: Matches documents that satisfy all of the specified queries.

`db.collection.find({$and: [{ age: { $gte: 30 } }, { status: "A" }] })`

- **$or**: Matches documents that satisfy at least one of the specified queries.

`db.collection.find({ $or: [{ age: { $gte: 30 } }, { status: "A }]})`

- **$not**: Matches documents that do not match the specified query.

`db.collection.find({ $not: { age: { $gte: 30 } } })`

- **$nor**: Matches documents that fail to match both of the specified queries.

`db.collection.find({ $nor: [{ age: { $gte: 30 } }, { status: "A" }] })`

### Projection Operators

These operators allow you to specify which fields to include or exclude from the query results:
- **$project**: Excludes or includes specified fields in the query results.

`db.collection.find({ $project: { _id: 0, name: 1 } })`

- **$elemMatch**: Includes the first element that matches the specified condition.

`db.collection.find({ items: { $elemMatch: { price: { $gt: 10} } } })`

- **$slice**: Includes a specified number of elements from an array.

`db.collection.find({ items: { $slice: 3 } })`

- **$redact**: Redacts (hides) fields in the query results based on a
  specified condition.

`db.collection.find({ $redact: { $cond: [ { $eq: [ "$age
", 30 ] }, "$$KEEP", "$$PRUNE" ] } })`

- **$meta**: Includes metadata about the query results.

`db.collection.find({ $meta: "textScore" })`

- **$addFields**: Adds new fields to the documents in the query results.

`db.collection.find({ $addFields: { newField: { $sum: [ "$field1
", "$field2" ] } } })`

- **$set**: Sets the value of a field in the documents in the query results.

`db.collection.find({ $set: { field: "value" } })`

- **$unset**: Removes a field from the documents in the query results.

`db.collection.find({ $unset: { field: "" } })`

- **$push**: Adds a value to an array in the documents in the query results.

`db.collection.find({ $push: { field: "value" } })`

- **$addToSet**: Adds a value to a set in the documents in the query results.

`db.collection.find({ $addToSet: { field: "value" } })`

- **$pop**: Removes the first or last element from an array in the documents in the query
  results.

`db.collection.find({ $pop: { field: 1 } })`

- **$pull**: Removes all occurrences of a value from an array in the documents in the query
  results.

`db.collection.find({ $pull: { field: "value" } })`

- **$pullAll**: Removes all occurrences of specified values from an array in the documents in
  the query results.

`db.collection.find({ $pullAll: { field: ["value1", "value2"] } })`

- **$pullAllFrom**: Removes all occurrences of specified values from an array in the documents in
  the query results.

`db.collection.find({ $pullAllFrom: { field: "array", values: ["value1", "value2"] } })`

- **$rename**: Renames a field in the documents in the query results.

`db.collection.find({ $rename: { field: "newField" } })`

- **$type**: Includes only documents where the specified field matches the specified type.

`db.collection.find({ field: { $type: "string" } })`

- **$mod**: Includes only documents where the specified field matches the specified modulo
  condition.

`db.collection.find({ field: { $mod: [ 1, 2 ] } })`

### Evaluation
The following operators assist in evaluating documents.

`$regex`: Allows the use of regular expressions when evaluating field values

`$text`: Performs a text search

`$where`: Uses a JavaScript expression to match documents

## MongoDB Update Operators
There are many update operators that can be used during document updates.

### Fields
The following operators can be used to update fields:

* $currentDate: Sets the field value to the current date
* $inc: Increments the field value
* $rename: Renames the field
* $min: Only updates the field if the specified value is less than the existing field value.
* $max: Only updates the field if the specified value is greater than the existing field value.
* $mul: Multiplies the value of the field by the specified amount.
* $set: Sets the value of a field
* $setOnInsert: Sets the value of a field if an update results in an insert of a document. Has no effect on update operations that modify existing documents.
* $unset: Removes the field from the document

### Array
The following operators assist with updating arrays.

$addToSet: Adds distinct elements to an array
$pop: Removes the first or last element of an array
$pull: Removes all elements from an array that match the query
$push: Adds an element to an array

All the examples of the above operators would be seen in the following section.

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

```shell
db.posts.aggregate([
  // Stage 1: Only find documents that have more than 1 like
  {
    $match: { likes: { $gt: 1 } }
  },
  // Stage 2: Group documents by category and sum each categories likes
  {
    $group: { _id: "$category", totalLikes: { $sum: "$likes" } }
  }
])
```

## Schema Validation with JSON Schema

MongoDB supports schema validation using JSON Schema. The `$jsonSchema` operator allows you to specify rules for document structure.

***Example***

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

### Atlas Feature

* https://www.w3schools.com/mongodb/mongodb_charts.php
* https://www.w3schools.com/mongodb/mongodb_indexing_search.php
* https://www.w3schools.com/mongodb/mongodb_data_api.php
* https://www.w3schools.com/mongodb/mongodb_aggregations_group.php

## Ref

https://www.mongodb.com/docs/manual/crud/