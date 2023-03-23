# YOUR IMPLEMENTATION OF LotterySimulation GOES HERE
import matplotlib.pyplot as pl
import random

class LotterySimulation:
    # initializes the function for the variables required
    def __init__(self, ticket_cost = 2, odds_of_winning = 0.0000000300347201, jackpot_value = 40000000, weeks_to_simulate = 520):
        self.ticket_cost = ticket_cost
        self.odds_of_winning = odds_of_winning
        self.jackpot_value = jackpot_value
        self.weeks_to_simulate = weeks_to_simulate
        self.money_spent = 0
        self.money_won = 0
        self.weeks_simulated = 0

    def run_simulation(self):
        # checks if weeks to simulate is not 0
        if self.weeks_to_simulate != 0:
            # runs the for loop weeks needed to simulate
            for x in range(self.weeks_to_simulate):
                # adds 1 to the week simulated
                self.weeks_simulated += 1
                # adds the ticket cost to the money spent
                self.money_spent += self.ticket_cost
                # checks if play_lottery is true and adds the jackpot value if true 
                if self.play_lottery() == True:
                    self.money_won += self.jackpot_value

        # checks if weeks simulated is 0
        if self.weeks_to_simulate == 0:
            won = False
            # runs the while loop while won is false
            while won == False:
                # adds the ticket cost to the money spent
                self.money_spent += self.ticket_cost
                # adds 1 to the weeks simulated
                self.weeks_simulated += 1
                # checks if the play_lottery is true and adds jackpot value if true
                if self.play_lottery() == True:
                    self.money_won += self.jackpot_value
                    won = True

    def play_lottery(self):
        # generates random generator and checks if it is greater than or equal to the odds of winning
        rand = random.random()
        if rand <= self.odds_of_winning:
            return True
        else:
            return False

    def get_summary(self):
        # returns the values
        return ("Money spent:     " + str(self.money_spent) + "\nMoney won:       " + str(self.money_won) + "\nWeeks simulated: " + str(self.weeks_simulated))

# Test code
sim = LotterySimulation(weeks_to_simulate = 52000)
sim.run_simulation()
summary = sim.get_summary()
print(summary)


sim = LotterySimulation(odds_of_winning=.00000300347201, weeks_to_simulate=0)
sim.run_simulation()
summary = sim.get_summary()
print(summary)



# YOUR IMPLEMENTATION OF THE PROFIT PLOT GOES HERE

# creates variables
money_spent = 0
money_won = 0
get_weeks_simulated = 52000000
profit = []
spent = []
won = []
num = 0

sim1 = LotterySimulation()
# runs throught the for loop 52 000 000 weeks
for i in range(get_weeks_simulated):
    sim1.play_lottery()
    money_spent += 2
    # checks if play_lottery is true
    if sim1.play_lottery() == True:
        # adds the jackpot money to the money won
        money_won += 40000000

    num += 1
    if num == 5200:
        # appends the money_spent, money_won, and profit
        prof = money_won - money_spent
        spent.append(money_spent)
        won.append(money_won)
        profit.append(prof)
        num = 0

# creates the interval range for the x-axis
x_label = list(range(10000))

# plots the line for profit, spent, and won
pl.plot(x_label, profit, 'r-', label = "Profit")
pl.plot(x_label, spent, 'b-', label = "Spent")
pl.plot(x_label, won, 'g-', label = "Won")

# labels the axis
pl.title("Lottery Simulations")
pl.xlabel("Years")
pl.ylabel("Money")

# sets the parameters and size
fig = pl.gcf()
fig.set_size_inches(8, 6)
pl.legend(loc = "upper left")
# saves the figure as a png
fig.savefig('lottery_profit.png')
# displays the graph
pl.show()