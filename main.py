import json


def play_game():
    draft_options = json.loads(input())
    draft = {}
    print(json.dumps(draft))

    while True:
        state = json.loads(input())
        message = "I move to center of galaxy"
        commands = []

        for ship in state['My']:
            commands.append({"Command": "MOVE", "Parameters": {"Id": ship['Id'], "Target": "15/15/15"}})

        print(json.dumps({"Message": message, "UserCommands": commands}))

play_game()