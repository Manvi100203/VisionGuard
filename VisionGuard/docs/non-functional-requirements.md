# Non-Functional Requirements

## Performance
The system should process frames continuously and display an FPS value.

## Security
Known-face data should be stored locally and should only be populated with appropriate consent.

## Usability
The application should provide a simple live display and a single-key exit mechanism.

## Reliability
Camera and image-loading failures should be handled without silently continuing with invalid data.

## Maintainability
Detection, recognition, monitoring, camera handling, and visualization are separated into modules.

## Error Handling
Invalid camera input and unreadable images are detected and reported.

## Logging
Monitoring events can be stored in `logs/events.csv`.
