-- CreateTable
CREATE TABLE "s2023" (
    "id" INTEGER NOT NULL,
    "player_name" TEXT NOT NULL,
    "age" INTEGER NOT NULL,
    "games" INTEGER NOT NULL,
    "games_started" INTEGER NOT NULL,
    "minutes" INTEGER NOT NULL,
    "field_goals" INTEGER NOT NULL,
    "field_attempts" INTEGER NOT NULL,
    "field_percent" DOUBLE PRECISION NOT NULL,
    "three_fg" INTEGER NOT NULL,
    "three_attempts" INTEGER NOT NULL,
    "three_percent" DOUBLE PRECISION NOT NULL,
    "two_fg" INTEGER NOT NULL,
    "two_attempts" INTEGER NOT NULL,
    "two_percent" DOUBLE PRECISION NOT NULL,
    "ft" INTEGER NOT NULL,
    "fta" INTEGER NOT NULL,
    "ft_percent" DOUBLE PRECISION NOT NULL,
    "ORB" INTEGER NOT NULL,
    "DRB" INTEGER NOT NULL,
    "TRB" INTEGER NOT NULL,
    "AST" INTEGER NOT NULL,
    "STL" INTEGER NOT NULL,
    "BLK" INTEGER NOT NULL,
    "TOV" INTEGER NOT NULL,
    "PTS" INTEGER NOT NULL,
    "team" TEXT NOT NULL,
    "season" INTEGER NOT NULL,

    CONSTRAINT "s2023_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "s2023_id_key" ON "s2023"("id");
