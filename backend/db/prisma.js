const { PrismaClient } = require('@prisma/client')

const prisma = new PrismaClient()

async function main() {
  let url = "https://nba-stats-db.herokuapp.com/api/playerdata/season/2023/"
  while (url !== null) {
    const response = await fetch(url)
    const data = await response.json()
    url = data.next
    for (let i = 0; i < data.results.length; i++) {
      await prisma.s2023.create({
        data: {
          id: data.results[i].id,
          player_name: data.results[i].player_name,
          age: data.results[i].age,
          games: data.results[i].games,
          games_started: data.results[i].games_started,
          minutes: data.results[i].minutes_played,
          field_goals: data.results[i].field_goals,
          field_attempts: data.results[i].field_attempts,
          field_percent: data.results[i].field_percent,
          three_fg: data.results[i].three_fg,
          three_attempts: data.results[i].three_attempts,
          three_percent: data.results[i].three_percent,
          two_fg: data.results[i].two_fg,
          two_attempts: data.results[i].two_attempts,
          two_percent: data.results[i].two_percent,
          ft: data.results[i].ft,
          fta: data.results[i].fta,
          ft_percent: data.results[i].ft_percent,
          ORB: data.results[i].ORB,
          DRB: data.results[i].DRB,
          TRB: data.results[i].TRB,
          AST: data.results[i].AST,
          STL: data.results[i].STL,
          BLK: data.results[i].BLK,
          TOV: data.results[i].TOV,
          PTS: data.results[i].PTS,
          team: data.results[i].team,
          season: data.results[i].season
        }
      })
    }
  }
  // const rows = await prisma.s2023.findMany()
  // console.log(rows)
}

main()
  .then(async () => {
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })