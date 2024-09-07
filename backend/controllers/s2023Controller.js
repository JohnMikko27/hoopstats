const asyncHandler = require('express-async-handler')
const { PrismaClient } = require('@prisma/client')

const prisma = new PrismaClient()

exports.getPlayerTotalStats = asyncHandler(async(req, res, next) => {
    const name = req.params.playerName
    const player = await prisma.$queryRaw`SELECT * FROM s2023 
    WHERE unaccent(player_name) ILIKE unaccent(${name})`   

    res.json(player)
})

exports.getPlayerAverageStats = asyncHandler(async(req, res, next) => {
    const name = req.params.playerName
    const player = await prisma.$queryRaw`SELECT * FROM "s2023Average"
    WHERE unaccent(player_name) ILIKE unaccent(${name})`   
    
    res.json(player)
})