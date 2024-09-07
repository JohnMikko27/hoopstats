/*
  Warnings:

  - You are about to alter the column `age` on the `s2023Average` table. The data in that column could be lost. The data in that column will be cast from `DoublePrecision` to `Integer`.

*/
-- AlterTable
ALTER TABLE "s2023Average" ALTER COLUMN "age" SET DATA TYPE INTEGER;
