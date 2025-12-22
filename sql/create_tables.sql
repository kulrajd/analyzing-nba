CREATE TABLE IF NOT EXISTS teams (
  team_id INTEGER PRIMARY KEY,
  city TEXT,
  team_name TEXT NOT NULL,
  team_abv TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS games (
  game_id INTEGER PRIMARY KEY,
  home_team_id INTEGER NOT NULL REFERENCES teams(team_id),
  away_team_id INTEGER NOT NULL REFERENCES teams(team_id),
  game_date TIMESTAMPTZ NOT NULL
);
