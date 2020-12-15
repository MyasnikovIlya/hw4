import pandas as pd
import pygad

raw_data = pd.read_csv('19.txt', sep = ' ', names = ['w','v','p'], header=None)

max_wei, max_vol, *_ = list(raw_data.iloc[0])
print(max_wei, max_vol)
raw_data = raw_data.drop([0])
length = raw_data.shape[0]
data = []
for i in range(0,length):
  data.append(list(raw_data.iloc[i]))

def fitness_func(solution, solution_idx):
    w = 0
    v = 0
    c = 0
    for (val, item) in zip(solution, data):
      if (val > 0):
        w += item[0]
        v += item[1]
        c += item[2]
    if w > max_wei or v > max_vol:
        c = 0
    return c

ga_instance = pygad.GA(num_generations=50,
                       num_parents_mating=2,
                       fitness_func=fitness_func,
                       sol_per_pop=100,
                       num_genes=30,
                       init_range_low=-1,
                       init_range_high=1
                       )

ga_instance.run()
solution, solution_fitness, _ = ga_instance.best_solution()

result = []
vals= [0,0,0]
for i in range(0, 30):
    if solution[i] > 0:
        result.append(data[i])
        vals[0] +=data[i][0]
        vals[1] +=data[i][1]
        vals[2] +=data[i][2]
result.append(['Ниже', 'сумма', 'значений'])
result.append(vals)
result_df = pd.DataFrame.from_records(result, columns=['w','v','c'])

print(solution_fitness)
print(result_df)
result_df.to_csv('res4.1.csv', index=False)