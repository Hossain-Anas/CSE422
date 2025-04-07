import random

def gen_chrom():
    sl = random.randint(1,99)
    tp = random.randint(1,99)
    ts = random.randint(1,99)

    return {"stop_loss": sl, "take_profit": tp, "trade_size":ts}


initial_population = [gen_chrom() for _ in range(4)]
# print(initial_population)

# print("\n\n")

initial_capital = 1000
historical_prices = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
generations = 10

mutation_rate = 0.05
population_sz = 4

def eval_fitness(chromosome):

    capital = initial_capital
    stop_loss = chromosome["stop_loss"]
    take_profit = chromosome["take_profit"]
    trade_size_in_pct = chromosome["trade_size"]

    profit_loss = 0

    for i in historical_prices:
        actual_trade_sz = capital * (trade_size_in_pct/100)

        if i <= -stop_loss:
            profit_loss = -actual_trade_sz*(stop_loss/100)
        
        elif i >= take_profit:
            profit_loss = actual_trade_sz*(take_profit/100)
        
        else:
            profit_loss = actual_trade_sz*(i/100)
    
        capital += profit_loss

    fitness = capital - initial_capital

    return fitness


def single_point_crossover(p1,p2):

    temp_p1 = chrm_to_strng(p1)
    temp_p2 = chrm_to_strng(p2)

    crossover_point = random.randint(1,len(temp_p1)-1)

    c1 = temp_p1[:crossover_point] + temp_p2[crossover_point:]
    c2 = temp_p2[:crossover_point] + temp_p1[crossover_point:]


    return strng_to_chrm(c1), strng_to_chrm(c2)

def mutate(chromosome):
    temp=random.random()

    if temp<mutation_rate:
        parent=chrm_to_strng(chromosome)
        idx=random.randint(0,len(parent)-1)
        val=random.randint(0,9)
        child=parent[:idx]+str(val)+parent[idx+1:]
        return strng_to_chrm(child)
    
    return chromosome


def select_parent(population):
    return random.sample(population, 2)


#q-2
def two_point_crossover(p1,p2):
    temp_p1 = chrm_to_strng(p1)
    temp_p2 = chrm_to_strng(p2)

    point1 = random.randint(1,len(temp_p1)-2)
    point2 = random.randint(point1+1 ,len(temp_p1)-1)

    c1 = temp_p1[:point1] + temp_p2[point1:point2] + temp_p1[point2:]
    c2 = temp_p2[:point1] + temp_p1[point1:point2] + temp_p2[point2:]

    # return strng_to_chrm(c1), strng_to_chrm(c2)

    return c1,c2



def chrm_to_strng(chrm):
    sl = str(int(chrm["stop_loss"])).zfill(2)
    tp = str(int(chrm["take_profit"])).zfill(2)
    ts = str(int(chrm["trade_size"])).zfill(2)
    
    return sl+tp+ts

def strng_to_chrm(strng):
    
    sl = float(strng[0:2]) 
    tp = float(strng[2:4]) 
    ts = float(strng[4:6]) 

    return {"stop_loss" : sl, "take_profit": tp, "trade_size": ts}

    


population = initial_population.copy()

best_chromosome = -1
best_fitness = float('-inf')

for i in range(len(population)):
    temp_chromosome = population[i]
    temp_fitness = eval_fitness(temp_chromosome)

    if temp_fitness > best_fitness:
        best_fitness = temp_fitness
        best_chromosome = temp_chromosome


for i in range(generations):

    new_population = []
    # new_population.append(best_chromosome)

    # while len(new_population) < population_sz:

    p1,p2 = select_parent(population)
    population.remove(p1)
    population.remove(p2)

    c1,c2 = single_point_crossover(p1,p2)

    c1 = mutate(c1)
    c2 = mutate(c2)

    new_population.append(c1)
    new_population.append(c2)
        # if len(new_population) < population_sz:
        #     new_population.append(c2)
    p3,p4 = select_parent(population)
    population.remove(p3)
    population.remove(p4)

    c3,c4 = single_point_crossover(p3,p4)

    c3 = mutate(c3)
    c4 = mutate(c4)

    new_population.append(c3)
    new_population.append(c4)

    population = new_population

    for i in range(len(population)):
        temp_chromosome = population[i]
        temp_fitness = eval_fitness(temp_chromosome)

        if temp_fitness > best_fitness:
            best_fitness = temp_fitness
            best_chromosome = temp_chromosome


print(f'''best_strategy:
{best_chromosome}
Final_profit : {round(best_fitness,1)}''')

print("-------------------------------------------\n")
print("------------PART02-------------------") 

p1,p2 = random.sample(initial_population,2)

c1,c2 = two_point_crossover(p1,p2)


print(f'''Parent 1 : {chrm_to_strng(p1)}
Parent 2 : {chrm_to_strng(p2)}

Child 1 : {c1}
Child 2 : {c2}''')