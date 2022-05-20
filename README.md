# Steam-Library-Manager
Manage your steam library across different drives and network attached storage

# TODO
## Command Line
- [ ] create appmanifest object
  - [ ] game name
  - [ ] file location
- [ ] read all appmanifests from directory and create a list / array of appmanifest objects
- [ ] copy game + appmanifest from dir to dir
  - [ ] robocopy
  - [ ] regular file transfer
- [ ] transfer over network
## GUI
- [ ] Games list
  - [ ] game names
  - [ ] last updated
  - [ ] filtering / sorting
    - [ ] location (which steam library folder)
    - [ ] size on disk (and which disk and how full said disk is)
    - [ ] alphabetical
    - [ ] last updated
- [ ] Settings
  - [ ] permanence
  - [ ] add / remove steam library folders
  - [ ] toggle if library is SSD or HDD
  - [ ] robocopy vs regular file transfer
- [ ] add option to copy manifest and game folder to user specified folder / removable media

# Stretch goals
- Check which location has most up to date version of game
- file compression when sending to specific folders / backup
- communicate to other PCs to check if the game is installed on another machine
- steam workshop files
- investigate if saving the list of appmanifests as a json or similar is faster than individually reading the appmanifests every boot
- steam API? / steamDB API
  - check if up to date (maybe even how large the update is)
  - get user data (e.g. last time user played xyz game)