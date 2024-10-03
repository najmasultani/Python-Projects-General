# Gamification of Exercise

This project implements a simulator to gamify exercise, awarding users points and stars for engaging in activities like running, resting, and carrying textbooks. The system tracks health points and hedons (fun points) to simulate how different rewards impact user behavior and motivation.

## Key Features:
1. **Health and Hedon Points**: Users gain health and hedon points based on activity type and duration.
2. **Star Rewards**: Stars increase hedons but can lose their effect if used too often.
3. **Activity Simulation**: Allows testing different strategies for awarding stars to optimize engagement.

## Main Functions:
- `get_cur_hedons()`: Returns total hedons accumulated.
- `get_cur_health()`: Returns total health points accumulated.
- `offer_star(activity)`: Offers a star to increase hedon points for the specified activity.
- `perform_activity(activity, duration)`: Simulates performing the given activity for the specified duration.
- `most_fun_activity_minute()`: Returns the activity that provides the most hedons per minute.
