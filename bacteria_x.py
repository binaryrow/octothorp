time = 0
slowMicrobes_population = 1000
growth_rate = 0.20

while slowMicrobes_population < 4000000:
    slowMicrobes_population = slowMicrobes_population + growth_rate * slowMicrobes_population
    print (round(slowMicrobes_population))
    time = time + 1

print ("It took", time, "years for the Slow Microbes to double.")

print ("The final poulation was", round(slowMicrobes_population), "Slow Microbes.")


time = 0
fastMicrobes_population = 1000
growth_rate = 0.4

while fastMicrobes_population < 4000000:
    fastMicrobes_population = fastMicrobes_population + growth_rate * fastMicrobes_population
    print (fastMicrobes_population)
    time = time + 1

print ("It took", time, "years for the Fast Microbes to double.")

print ("The final poulation was", round(fastMicrobes_population), "Fast Microbes.")
