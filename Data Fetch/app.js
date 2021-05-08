const express = require("express");
const app = express();
const port = 3000;

const {
  MongoClient
} = require("mongodb");
// Replace the uri string with your MongoDB deployment's connection string.
const url =
  "mongodb+srv://anupamAdmin:anupamAdmin@cluster0.2c2zj.mongodb.net/student_db";
const client = new MongoClient(url, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"))

app.get("/", (req, res) => {
  res.render("welcome.ejs");
});

app.get("/records", (req, res) => {
  //   let std_list = [{ name: "suraj" }, { name: "anupam" }, { name: "yash" }];
  //   let std_list = fetchData();
  //   console.log(std_list);

  const database = client.db("student_db");
  const students = database.collection("student_records");
  students.find({}).toArray(function (err, std_record) {
    // console.log(std_record);
    res.render("records", {
      records: std_record
    });
  });
});


app.get("/stdTable", (req, res) => {
  // res.render("stdTable");
  const database = client.db("student_db");
  const students = database.collection("student_records");
  students.find({}).toArray(function (err, std_record) {
    // console.log(std_record);
    res.render("stdTable", {
      records: std_record
    });
  });
});



function fetchData() {
  const database = client.db("student_db");
  const students = database.collection("student_records");
  students.find({}).toArray(function (err, std_record) {
    // console.log(std_record);
    return std_record;
  });
}

async function run() {
  try {
    await client.connect();
    console.log("MongoDB connected");
  } finally {
    // Ensures that the client will close when you finish/error
    // await client.close();
  }
}
run().catch(console.dir);


app.listen(port, () => {
  console.log('App listening at http://localhost:'+ port);
});