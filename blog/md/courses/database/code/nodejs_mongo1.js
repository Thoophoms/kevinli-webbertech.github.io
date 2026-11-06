const { MongoClient } = require("mongodb");
// Replace the uri string with your connection string.
const url = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.1";
const client = new MongoClient(url);

async function run() {
  try {
    const database = client.db('sample_mflix');
    console.log("debugging1: ");
    const movies = database.collection('movies');
    console.log("debugging2: ");
    
    // Query for a movie that has the title 'Back to the Future'
    const query = { title: 'Back to the Future' };
    console.log("debugging3: " + JSON.stringify(query));

    // I added this part as there was no entry before
    await movies.insertOne(query, function(err, res) {
       if (err) throw err;
        console.log("1 document inserted");
       db.close();
    });

    // this is a query
    const movie = await movies.findOne(query);
    console.log("debugging4: " + JSON.stringify(movie));
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);