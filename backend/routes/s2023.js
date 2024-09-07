const express = require('express')
const router = express.Router()
const controller = require('../controllers/s2023Controller')

router.get('/:playerName', controller.getPlayerStats)

module.exports = router