def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    games = []
    cards = [1]*len(lines)
    total = 0

    for line in lines:
        game, numbers = line.split(": ")
        winning, yours = [x.strip() for x in numbers.split("|")]
        winning = set(winning.split())

        matches = sum(num in winning for num in yours.split())
        games.append(matches)
    
    for i in range(len(games)):
        k = games[i]
        for j in range(i+1,i+k+1):
            cards[j]+=cards[i]

    print(cards)
    print(sum(cards))
        

        

        
if __name__ == "__main__":
    run()