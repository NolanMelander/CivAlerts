# Civ Alerts
#### Version 0.0.2 - Alpha
Created by Nolan Melander

#### Latest Update Notes
- Fixed display issues for cinfo and linfo commands
- User Registration has been completed - Use command uregister [username]
- Restructured Image folder - Images now sorted into appropriate folders
- Added images for civilizations and leaders in prep for V 0.0.3 - Alpha
- Redesigned linfo command to display for leaders with alternate civilizations (Looking at you Eleanor)


## About

Civ Alerts is a discord bot currently in the early development stages. It is being created with the goal of being able 
to notify players who have not taken their turn after a specified amount of time, as set by the game host. The first 
release of Civ Alerts will require manual updates by the players, but the future goal is to integrate the bot to work 
directly with Civilization multiplayer games to automatically update without any need for user interaction.

## Progress
### Tasks Currently In Progress
- [ ] Test Register Game Commands
- [ ] Test Player Alert Commands
- [ ] Test Update Commands
- [ ] Transfer Bot to CivAlerts Server
- [ ] Finish Alert Logic
- [ ] Finish Game Update Logic
- [ ] Optimize Database Tables
- [ ] Redesign leader table in database
- [ ] Redesign civilization table in database
- [ ] Create three new tables for unique abilities, units, and infrastructure
- [ ] Rework linfo to show leader icons
- [ ] Rework cinfo to show civ icons

## Finished Tasks - Version 0.0.2 - Alpha
- [x] Setup Basic Bot Commands
- [x] Test Register User Commands
- [x] Rework linfo and cinfo commands
- [x] Add Leader Icons to Images/Leader
- [x] Add Civilization Icons to Images/Civilization

## Future Planned Tasks
- [ ] Add support for more than 8 players
- [ ] Add support for custom civilizations
- [ ] Direct integration with civilization games
- [ ] Score leader board
- [ ] Leagues

## Public Wireframes
### Bot Command Wireframe
![alt text](Images/Wireframe/CivAlert%20Commands.png "Bot Command Wireframe")
### Command Interaction Wireframe
![alt_text](Images/Wireframe/Flow%20Wireframe.png "Bot Command Interaction Wireframe")