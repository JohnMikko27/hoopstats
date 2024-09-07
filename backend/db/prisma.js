const { PrismaClient } = require('@prisma/client')

const prisma = new PrismaClient()

// the tofixed work for the field_percent and other percents but not the other ones, gotta fix that
// also fix the type of age in schema.prisma

async function main() {
  let url = "https://nba-stats-db.herokuapp.com/api/playerdata/season/2023/"
  while (url !== null) {
    const response = await fetch(url)
    const data = await response.json()
    url = data.next
    for (let i = 0; i < data.results.length; i++) {
      const gamesPlayed = data.results[i].games
      await prisma.s2023Average.create({
        data: {
          id: data.results[i].id,
          player_name: data.results[i].player_name,
          age: data.results[i].age,
          games: gamesPlayed,
          games_started: data.results[i].games_started,
          minutes: parseFloat((data.results[i].minutes_played / gamesPlayed).toFixed(1)),
          field_goals: parseFloat((data.results[i].field_goals / gamesPlayed).toFixed(1)),
          field_attempts: parseFloat((data.results[i].field_attempts / gamesPlayed).toFixed(1)),
          field_percent: parseFloat(data.results[i].field_percent).toFixed(1),
          three_fg: parseFloat((data.results[i].three_fg / gamesPlayed).toFixed(1)),
          three_attempts: parseFloat((data.results[i].three_attempts / gamesPlayed).toFixed(1)),
          three_percent: parseFloat(data.results[i].three_percent).toFixed(1),
          two_fg: parseFloat((data.results[i].two_fg / gamesPlayed).toFixed(1)),
          two_attempts: parseFloat((data.results[i].two_attempts / gamesPlayed).toFixed(1)),
          two_percent: parseFloat(data.results[i].two_percent).toFixed(1),
          ft: parseFloat((data.results[i].ft / gamesPlayed).toFixed(1)),
          fta: parseFloat((data.results[i].fta / gamesPlayed).toFixed(1)),
          ft_percent: parseFloat(data.results[i].ft_percent).toFixed(1),
          ORB: parseFloat((data.results[i].ORB / gamesPlayed).toFixed(1)),
          DRB: parseFloat((data.results[i].DRB / gamesPlayed).toFixed(1)),
          TRB: parseFloat((data.results[i].TRB / gamesPlayed).toFixed(1)),
          AST: parseFloat((data.results[i].AST / gamesPlayed).toFixed(1)),
          STL: parseFloat((data.results[i].STL / gamesPlayed).toFixed(1)),
          BLK: parseFloat((data.results[i].BLK / gamesPlayed).toFixed(1)),
          TOV: parseFloat((data.results[i].TOV / gamesPlayed).toFixed(1)),
          PTS: parseFloat((data.results[i].PTS / gamesPlayed).toFixed(1)),
          team: data.results[i].team,
          season: data.results[i].season
        }
      })
    }
  }
 
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