db = db.getSiblingDB("mongo");
db.mongo_table.drop();

db.mongo_table.insertMany([
  {
    id: 1,
    name: "Lion",
    type: "Wild",
  },
  {
    id: 2,
    name: "Cow",
    type: "Domestic",
  },
]);
