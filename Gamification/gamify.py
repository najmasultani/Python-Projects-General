# Project: Gamification of Exercise 
# Description: 
# This project simulates a system that encourages users to exercise by awarding "stars" 
# for performing activities like running, carrying textbooks, and resting. 
# The simulator models user behavior, tracking health points and hedons (fun points), 
# and allows testing of various strategies for awarding stars to optimize user engagement.

def initialize():
    global cur_hedons, cur_health, cur_time, cur_star, last_activity, last_activity_duration
    global tired, bored_with_stars, activities, cur_star_activity, last_finished
    global first_star_time, num_stars_given
    
    cur_hedons = 0
    cur_health = 0
    cur_time = 0
    cur_star = 0
    last_activity = None
    last_activity_duration = 0
    tired = False
    bored_with_stars = False
    activities = ['running', 'resting', 'textbooks']
    cur_star_activity = None
    last_finished = -1000
    num_stars_given = 0
    first_star_time = 0

# Check if the user is tired after recent activity.
def check_if_tired():
    global cur_time, last_finished, last_activity, tired
    tired = False
    if last_activity in ['running', 'textbooks']:
        tired = True
    elif last_finished - cur_time > 120 and last_activity == 'resting':
        tired = True

# Return the current number of hedons the user has accumulated.
def get_cur_hedons():
    global cur_hedons
    return cur_hedons

# Return the current number of health points the user has accumulated.
def get_cur_health():
    global cur_health
    return cur_health

# Offer a star for a specific activity and manage star availability.
def offer_star(activity):
    global cur_star, cur_star_activity, bored_with_stars, first_star_time, num_stars_given
    
    if activity in activities and not bored_with_stars:
        cur_star += 1
        cur_star_activity = activity
        if first_star_time == 0:
            first_star_time = cur_time
            num_stars_given = 1
        elif cur_time - first_star_time <= 120 and num_stars_given > 2:
            bored_with_stars = True
        elif cur_time - first_star_time <= 120:
            num_stars_given += 1
        elif cur_time - first_star_time > 120:
            first_star_time = cur_time
            num_stars_given = 1

# Simulate the user performing an activity for a specific duration.
def perform_activity(activity, duration):
    global cur_health, cur_hedons, cur_time, last_activity, last_finished, tired, cur_star, cur_star_activity, last_activity_duration

    if activity in activities:
        if activity == 'running':
            last_finished = cur_time + duration
            cur_time += duration
            total_duration = duration + last_activity_duration if last_activity == 'running' else duration

            # Calculate health points for running
            if total_duration <= 180:
                cur_health += 3 * duration
            else:
                extra_duration = total_duration - 180
                cur_health += 3 * (duration - extra_duration) + 1 * extra_duration

            # Calculate hedons for running
            if not tired:
                if star_can_be_taken(activity):
                    cur_hedons += 5 * min(10, duration) + max(0, duration - 10) * (-2)
                    cur_star -= 1
                else:
                    cur_hedons += 2 * min(10, duration) + max(0, duration - 10) * (-2)
            else:
                cur_hedons += 3 * min(10, duration) + (-2) * duration if star_can_be_taken(activity) else (-2) * duration
                cur_star -= 1 if star_can_be_taken(activity) else 0

        elif activity == 'textbooks':
            cur_health += 2 * duration
            last_finished = cur_time + duration
            cur_time += duration

            if not tired:
                cur_hedons += min(10, duration) + 3 * min(10, duration) + max(0, duration - 20) * (-1) if star_can_be_taken(activity) else 1 * min(20, duration) + (-1) * max(0, duration - 20)
                cur_star -= 1 if star_can_be_taken(activity) else 0
            else:
                cur_hedons += 3 * min(10, duration) + (-2) * duration if star_can_be_taken(activity) else (-2) * duration
                cur_star -= 1 if star_can_be_taken(activity) else 0

        elif activity == 'resting':
            tired = duration >= 120

    last_activity = activity
    last_activity_duration = duration
    cur_star = 0

# Check if the user can use the star for extra hedons.
def star_can_be_taken(activity):
    global cur_star, bored_with_stars, cur_star_activity, last_finished, cur_time
    return cur_star > 0 and activity == cur_star_activity and not bored_with_stars and last_finished - cur_time == 0

# Return the activity that would give the most hedons for one minute.
def most_fun_activity_minute():
    global tired, cur_star, bored_with_stars

    running_hedons = 2 + (3 if cur_star > 0 and not bored_with_stars else 0) if not tired else (-2 + (3 if cur_star > 0 and not bored_with_stars else 0))
    textbooks_hedons = 1 + (3 if cur_star > 0 and not bored_with_stars else 0) if not tired else (-2 + (3 if cur_star > 0 and not bored_with_stars else 0))

    return 'running' if running_hedons >= textbooks_hedons and running_hedons >= 0 else 'textbooks' if textbooks_hedons >= 0 else 'resting'

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # Test 1: -20
    print(get_cur_health())            # Test 2: 90
    print(most_fun_activity_minute())  # Test 3: resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # Test 4: running
    perform_activity("textbooks", 30)
    print(get_cur_health())            # Test 5: 150
    print(get_cur_hedons())            # Test 6: -80
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # Test 7: 210
    print(get_cur_hedons())            # Test 8: -90
    perform_activity("running", 170)
    print(get_cur_health())            # Test 9: 700
    print(get_cur_hedons())            # Test 10: -430
