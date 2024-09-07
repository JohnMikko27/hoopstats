const express = require('express')
const router = express.Router()
const controller = require('../controllers/s2023Controller')

router.get('/totals/:playerName', controller.getPlayerTotalStats)

router.get('/average/:playerName', controller.getPlayerAverageStats)

module.exports = router