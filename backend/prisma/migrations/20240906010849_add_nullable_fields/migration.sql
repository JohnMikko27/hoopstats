-- AlterTable
ALTER TABLE "s2023" ALTER COLUMN "games_started" DROP NOT NULL,
ALTER COLUMN "minutes" DROP NOT NULL,
ALTER COLUMN "field_goals" DROP NOT NULL,
ALTER COLUMN "field_attempts" DROP NOT NULL,
ALTER COLUMN "field_percent" DROP NOT NULL,
ALTER COLUMN "three_fg" DROP NOT NULL,
ALTER COLUMN "three_attempts" DROP NOT NULL,
ALTER COLUMN "three_percent" DROP NOT NULL,
ALTER COLUMN "two_fg" DROP NOT NULL,
ALTER COLUMN "two_attempts" DROP NOT NULL,
ALTER COLUMN "two_percent" DROP NOT NULL,
ALTER COLUMN "ft" DROP NOT NULL,
ALTER COLUMN "fta" DROP NOT NULL,
ALTER COLUMN "ft_percent" DROP NOT NULL,
ALTER COLUMN "ORB" DROP NOT NULL,
ALTER COLUMN "DRB" DROP NOT NULL,
ALTER COLUMN "TRB" DROP NOT NULL,
ALTER COLUMN "AST" DROP NOT NULL,
ALTER COLUMN "STL" DROP NOT NULL,
ALTER COLUMN "BLK" DROP NOT NULL,
ALTER COLUMN "TOV" DROP NOT NULL,
ALTER COLUMN "PTS" DROP NOT NULL;
