CREATE TABLE IF NOT EXISTS account_data (
	Username VARCHAR(32) PRIMARY KEY,
	Password TEXT,
	Email TEXT,
	AvatarName TEXT,
	XP integer default 0,
	Level integer default 0
);