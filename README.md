# HackKU2023 - ZenLog

## Inspiration
I took inspiration from those paper print-out bubble sheets of the year where you mark down your emotion for the day every day, and then at the end of the year you can see patterns and trends. I thought that I could take that concept and transform it into something a little more useful and sharable.

## What it does
ZenLog is a tool that lets you visualize your mental health over the span of days, months, and years. It is very useful for finding patterns and allowing yourself to find health solutions to tougher times.

Features:
- Day rating
- Day emotion selection
- Logging/journaling system
- Daily desktop notification
- Interactive tray icon
- Built-in graphing system with 3 modes
- Very flexible settings page
- Saving, exporting, and loading of data files
- "Help" page to walk users through step-by-step each area
- "Resources" page to help users explore their mental health further and/or get them in contact with mental health facilities
- Lots of docstrings and comments
- Very upgradable

## How we built it
The back-end was coded entirely in Python. The front-end used PyQt for the GUI framework. I was able to use Qt to create the UIs very easily and quickly, and they exported into very neat XML and CSS-ish files.

## Challenges we ran into
Stylesheets. Stylesheets. Stylesheets. The Qt designer doesn't allow importing of Qt stylesheet files (cmon, really??), and only has a tiny stylesheet parameter line for each individual widget. That isn't scalable at all, so we had to remove all of the applied styles and implement the styles within the program's runtime.

## Accomplishments that we're proud of
The UI quality and object oriented expansiveness. I made sure that this is not a one-and-done project, and instead can be expanded upon with great ease (I added LOTS of docstrings and comments). 

## What we learned
I learned how to connect XML files and the Qt design software to base-level python. I will most certainly be using this GUI framework in future projects, as it's very quick and also very versatile for custom widgets and customization.

## What's next for ZenLog
**A mobile app!** That was my initial idea, however I found that it would probably be far too much of an undertaking for 36 hours to get it as polished as I would be satisfied with (plus, the computing power to emulate a smartphone is something my laptop is not capable of yet, ha!). I also had an idea for a digital pet reward system, like a tomogachi. Every day that you log, you receive food or coins. It's very much a concept right now.
