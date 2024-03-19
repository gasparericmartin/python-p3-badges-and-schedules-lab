def badge_maker(name):
    badge = f'Hello, my name is {name}.'
    return badge

def batch_badge_creator(names):
    # badge_list = []
    # for name in names:
    #     badge_list.append(badge_maker(name))
    # return badge_list

    return [badge_maker(name) for name in names]

def assign_rooms(names):
    rooms_list = []
    for name in names:
        rooms_list.append(f'Hello, {name}! You\'ll be assigned to room {names.index(name) + 1}!')
    return rooms_list


def printer(names):
    # badge_list = batch_badge_creator(names)
    # rooms_list = assign_rooms(names)
    
    # for badge in badge_list:
    #     print(badge)
    
    # for room in rooms_list:
    #     print(room)

    [print(badge) for badge in batch_badge_creator(names)]
    [print(room) for room in assign_rooms(names)]
    
