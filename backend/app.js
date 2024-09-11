const express = require('express')
const app = express()
const cors = require('cors')

const s2023Router = require('./routes/s2023')

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cors());

app.use('/2023', s2023Router)
app.get('/', (req, res) => res.send('hi miks'))

app.listen(3000, () => console.log("Server starting on port 3000..."));