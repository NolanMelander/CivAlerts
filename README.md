# Civ Alerts
#### Version 0.0.2 - Alpha
Created by Nolan Melander

## About

Civ Alerts is a discord bot currently in the early development stages. It is being created with the goal of being able 
to notify players who have not taken their turn after a specified amount of time, as set by the game host. The first 
release of Civ Alerts will require manual updates by the players, but the future goal is to integrate the bot to work 
directly with Civilization multiplayer games to automatically update without any need for user interaction.

##Known Bugs
-[x] cInfo does not display full list of civilizations
-[x] lInfo does not display full list of leaders

## Progress
### Tasks Currently In Progress
- [ ] Setup Basic Bot Commands
- [X] Test Register User Commands
- [ ] Test Register Game Commands
- [ ] Test Player Alert Commands
- [ ] Test Update Commands
- [ ] Transfer Bot to CivAlerts Server
- [ ] Finish Alert Logic
- [ ] Finish Game Update Logic
- [ ] Optimize Database Tables
- [x] Rework linfo and cinfo commands
- [ ] Redesign leader table in database
- [ ] Redesign civilization table in database
- [ ] Create three new tables for unique abilities, units, and infrastructure
- [ ] Add Leader Icons to Images/Leader
- [ ] Add Civilization Icons to Images/Civilization


## Finished Tasks - Version 0.0.1 - Alpha
- [x] Create Bot Interaction Wireframe
- [x] Creating Database Tables
- [x] Create Command Wireframe 
- [x] Setup Github Webhook (For Tracking Github Changes)
- [x] Setup Bot on Discord Test Server

## Future Planned Tasks
- [ ] Add support for more than 8 players
- [ ] Add support for custom civilizations
- [ ] Direct integration with civilization games
- [ ] Score leader board

## Public Wireframes
### Bot Command Wireframe
![alt text](Images/Wireframe/CivAlert%20Commands.png "Bot Command Wireframe")
### Command Interaction Wireframe
![alt_text](Images/Wireframe/Flow%20Wireframe.png "Bot Command Interaction Wireframe")